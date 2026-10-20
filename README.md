# Associação Cruzada e Mineração de Dados: CSC 2.0 × SDSS DR15

Este repositório reúne os códigos, dados e resultados do projeto de Iniciação Científica que aplicou o algoritmo Apriori para minerar dados do catálogo cruzado entre o Chandra Source Catalog (CSC 2.0) e o Sloan Digital Sky Survey (SDSS DR15).

## Informações do Projeto
* Autoras: Heloisa de Souza Ortiz e Vitória Gabriela Mohr de Lima
* Orientação: Profª. Rosanete Grassiani dos Santos
* Instituição: UNIFACEAR

## Sobre o Projeto
O trabalho analisou 35.771 pares de fontes astronômicas para identificar inconsistências (matches rotulados como definitivos, mas com baixa probabilidade estatística) e padrões astrofísicos entre estrelas e galáxias. Após a etapa de limpeza, o algoritmo Apriori foi aplicado a 32.386 pares, gerando 449 regras de associação. O principal achado indica que galáxias, por serem fontes extensas, tendem a apresentar maior ambiguidade posicional (matches mais frouxos) em comparação às estrelas.

## Estrutura do Repositório

### Documentação e Resultados
* `artigo_final.pdf`: Artigo completo com a fundamentação, metodologia e discussão.
* `regras_associacao_setembro.csv`: Planilha com as 449 regras geradas.

### Banco de Dados e Mineração
* `agosto_banco.sql`: Scripts SQL usados para consultas, discretização e limpeza no PostgreSQL.
* `mineracao_apriori_setembro.py`: Código Python (mlxtend) principal para execução do Apriori.

### Códigos para Geração de Figuras (Python)
* `figura1_confusao_astrometrica.py`: Gera o esquema ilustrativo da confusão astrométrica.
* `figura2_separacao_angular.py`: Gera o gráfico de distribuição da separação angular.
* `figura3_separacao_probabilidade.py`: Gera o gráfico de barras agrupadas (Separação x Probabilidade).
* `figura4_inconsistencias_D.py`: Gera o gráfico de inconsistências dos matches definitivos.

## Como Executar
Para rodar o script principal de mineração ou os scripts das figuras, instale as dependências executando no terminal:

```bash
pip install pandas mlxtend matplotlib numpy
```
Em seguida, execute o arquivo Python desejado. Exemplo:

```bash
python mineracao_apriori_setembro.py
```
Se utilizar este material, por favor cite:
ORTIZ, H. S.; LIMA, V. G. M. Associação Cruzada e Mineração de Dados: Padrões entre o CSC 2.0 e o SDSS DR15. 2026. Trabalho de Iniciação Científica (IV EIC) - UNIFACEAR, 2026.
