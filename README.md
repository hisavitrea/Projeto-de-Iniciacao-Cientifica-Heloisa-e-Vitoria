Projeto de Iniciação Científica
# Associação Cruzada e Mineração de Dados: CSC 2.0 × SDSS DR15

Este repositório reúne os códigos, dados e resultados do projeto de Iniciação Científica que aplicou o algoritmo Apriori para minerar dados do catálogo cruzado entre o Chandra Source Catalog (CSC 2.0) e o Sloan Digital Sky Survey (SDSS DR15).

## Informações do Projeto
* Autoras: Heloisa de Souza Ortiz e Vitória Gabriela Mohr de Lima
* Orientação: Profª. Rosanete Grassiani dos Santos
* Instituição: Centro Universitário UNIFACEAR

## Sobre o Projeto
O trabalho analisou 35.771 pares de fontes astronômicas para identificar inconsistências (matches rotulados como definitivos, mas com baixa probabilidade estatística) e padrões astrofísicos entre estrelas e galáxias. Após a etapa de limpeza, o algoritmo Apriori foi aplicado a 32.386 pares, gerando 449 regras de associação. O principal achado indica que galáxias, por serem fontes extensas, tendem a apresentar maior ambiguidade posicional (matches mais frouxos) em comparação às estrelas.

## Estrutura do Repositório
* `artigo_final.pdf`: Artigo completo com a fundamentação, metodologia e discussão.
* `agosto_banco.sql`: Scripts SQL usados para consultas, discretização e limpeza no PostgreSQL.
* `mineracao_apriori_setembro.py`: Código Python (mlxtend) para execução do Apriori.
* `regras_associacao_setembro.csv`: Planilha com as 449 regras geradas.

## Como Executar
Para rodar o script de mineração, instale as dependências e execute o arquivo Python:
```bash
pip install pandas mlxtend
python mineracao_apriori_setembro.py

Se utilizar este material, por favor cite:
ORTIZ, H. S.; LIMA, V. G. M. Associação Cruzada e Mineração de Dados: Padrões entre o CSC 2.0 e o SDSS DR15. 2026. Trabalho de Iniciação Científica (IV EIC) - UNIFACEAR, 2026.
