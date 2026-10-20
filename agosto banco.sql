-- ============================================================
-- AGOSTO (3º mês) — Análise dos registros astronômicos:
-- identificação de inconsistências, tendências e padrões
-- entre CSC 2.0 e SDSS DR15
--
-- Segue a etapa "2. Exploração e limpeza" da metodologia:
-- discretização de separação angular e probabilidade de match
-- em categorias, seguida de cruzamentos para achar padrões
-- e inconsistências.
-- ============================================================

-- ------------------------------------------------------------
-- 1. Discretização: separação angular em categorias
--    (<1", 1-2", >2")
-- ------------------------------------------------------------
ALTER TABLE csc2_sdss_dr15 ADD COLUMN sep_categoria TEXT;

UPDATE csc2_sdss_dr15
SET sep_categoria = CASE
    WHEN csc2_sdssdr15_separation < 1 THEN '<1"'
    WHEN csc2_sdssdr15_separation <= 2 THEN '1-2"'
    ELSE '>2"'
END;

SELECT
    sep_categoria,
    COUNT(*) AS quantidade,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS percentual
FROM csc2_sdss_dr15
GROUP BY sep_categoria
ORDER BY quantidade DESC;

-- ------------------------------------------------------------
-- 2. Discretização: probabilidade de match em categorias
--    (alta >=0.99, média 0.9-0.99, baixa <0.9)
-- ------------------------------------------------------------
ALTER TABLE csc2_sdss_dr15 ADD COLUMN prob_categoria TEXT;

UPDATE csc2_sdss_dr15
SET prob_categoria = CASE
    WHEN match_probability >= 0.99 THEN 'alta (>=0.99)'
    WHEN match_probability >= 0.9  THEN 'média (0.9-0.99)'
    ELSE 'baixa (<0.9)'
END;

SELECT
    prob_categoria,
    COUNT(*) AS quantidade,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS percentual
FROM csc2_sdss_dr15
GROUP BY prob_categoria
ORDER BY quantidade DESC;

-- ------------------------------------------------------------
-- 3. Cruzamento separação x tipo SDSS
--    (posições estão mais próximas para estrelas ou galáxias?)
-- ------------------------------------------------------------
SELECT
    sep_categoria,
    sdssdr15_type,
    COUNT(*) AS quantidade
FROM csc2_sdss_dr15
GROUP BY sep_categoria, sdssdr15_type
ORDER BY sep_categoria, sdssdr15_type;

-- ------------------------------------------------------------
-- 4. Cruzamento probabilidade x tipo SDSS
-- ------------------------------------------------------------
SELECT
    prob_categoria,
    sdssdr15_type,
    COUNT(*) AS quantidade
FROM csc2_sdss_dr15
GROUP BY prob_categoria, sdssdr15_type
ORDER BY prob_categoria, sdssdr15_type;

-- ------------------------------------------------------------
-- 5. Cruzamento separação x probabilidade
--    (a discordância aqui aponta casos onde o modelo bayesiano
--    usa mais informação do que a simples distância — reforça
--    a justificativa do projeto contra métodos de distância fixa)
-- ------------------------------------------------------------
SELECT
    sep_categoria,
    prob_categoria,
    COUNT(*) AS quantidade
FROM csc2_sdss_dr15
GROUP BY sep_categoria, prob_categoria
ORDER BY sep_categoria, prob_categoria;

-- ------------------------------------------------------------
-- 6. Match_grade x categorias (D deveria concentrar prob alta e
--    separação pequena; L deveria concentrar o oposto)
-- ------------------------------------------------------------
SELECT match_grade, sep_categoria, COUNT(*) AS quantidade
FROM csc2_sdss_dr15
GROUP BY match_grade, sep_categoria
ORDER BY match_grade, sep_categoria;

SELECT match_grade, prob_categoria, COUNT(*) AS quantidade
FROM csc2_sdss_dr15
GROUP BY match_grade, prob_categoria
ORDER BY match_grade, prob_categoria;

-- ------------------------------------------------------------
-- 7. IDENTIFICAÇÃO DE INCONSISTÊNCIAS
-- ------------------------------------------------------------

-- 7.1 Separação pequena (<1") mas probabilidade baixa (<0.9)
--     -> contraintuitivo à primeira vista; existem porque o modelo
--        bayesiano pondera também densidade local de fontes e
--        elipses de erro, não só a distância.
SELECT COUNT(*) AS inconsistencia_sep_pequena_prob_baixa
FROM csc2_sdss_dr15
WHERE sep_categoria = '<1"'
  AND prob_categoria = 'baixa (<0.9)';

-- 7.2 Separação grande (>2") mas probabilidade alta (>=0.99)
--     -> não deveria ocorrer sob o modelo; útil para auditoria.
SELECT COUNT(*) AS inconsistencia_sep_grande_prob_alta
FROM csc2_sdss_dr15
WHERE sep_categoria = '>2"'
  AND prob_categoria = 'alta (>=0.99)';

-- 7.3 Match_grade = 'D' (match "definitivo") mas com evidência
--     estatística fraca (probabilidade baixa E separação grande)
--     -> PRINCIPAL achado de agosto: 3.385 pares (≈10,5% de todos
--        os "D") são rotulados como confiáveis mas discordam dos
--        próprios indicadores probabilísticos. Candidatos a caso
--        de estudo / possível efeito de confusão astrométrica em
--        campos densos (Hogg, 2001; Freire, Porto & De Macêdo, 2017).
SELECT COUNT(*) AS inconsistencia_grade_D_fraco
FROM csc2_sdss_dr15
WHERE match_grade = 'D'
  AND prob_categoria = 'baixa (<0.9)'
  AND sep_categoria = '>2"';

-- 7.4 Lista dos próprios registros inconsistentes (para inspeção manual /
--     possível remoção ou reclassificação antes da mineração de regras)
SELECT csc2_id, sdssdr15_id, sdssdr15_type, csc2_sdssdr15_separation,
       match_probability, match_type, match_grade
FROM csc2_sdss_dr15
WHERE match_grade = 'D'
  AND prob_categoria = 'baixa (<0.9)'
  AND sep_categoria = '>2"'
ORDER BY match_probability ASC
LIMIT 50;

-- ------------------------------------------------------------
-- 8. Match_type x separação (E = single/estimado, R = múltiplo/
--    recalculado — checar se tipo R concentra separações maiores,
--    o que indicaria maior ambiguidade posicional nesses casos)
-- ------------------------------------------------------------
SELECT match_type, sep_categoria, COUNT(*) AS quantidade
FROM csc2_sdss_dr15
GROUP BY match_type, sep_categoria
ORDER BY match_type, sep_categoria;
