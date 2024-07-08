# BIX-Tecnologia-Desafio-Tecnico: Projeto de Data Science

Este repositório contém o código e os dados utilizados para resolver o desafio técnico de Data Science proposto pela BIX Tecnologia, relacionado à otimização do planejamento de manutenção.

### Tecnologias
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

## Descrição do Projeto

A BIX Tecnologia contratou uma consultoria de Data Science para melhorar o planejamento de manutenção de uma frota terceirizada de transportes. O foco do projeto é reduzir os custos de manutenção do sistema de ar dos caminhões, identificando falhas de forma preditiva.

## Conteúdo do Repositório

- `air_system_previous_years.csv`: Dados históricos de manutenção dos anos anteriores.
- `air_system_present_year.csv`: Dados de manutenção do ano presente para validação.
  
## Passos Realizados

1. **Preparação dos Dados:**
   - Carregamento dos dados.
   - Transformação da coluna `'class'` para valores numéricos.
   - Tratamento de valores ausentes.

2. **Modelagem:**
   - Utilização do modelo de machine learning: Random Forest.
   - Treinamento dos modelos nos dados históricos.
   - Avaliação dos modelos utilizando métricas como acurácia, matriz de confusão e relatório de classificação.

3. **Avaliação no Conjunto de Dados do Ano Presente:**
   - Utilização do modelo treinado com Random Forest para fazer previsões nos dados do ano presente.
   - Avaliação da capacidade de generalização do modelo.

## Resultados
- **Modelo de Random Forest:**
  - Acurácia: 99.16875%
  - Matriz de Confusão
    
      ![image](https://github.com/EastBeng/Bix-Projeto/assets/44300759/9d24ee24-a8f9-4113-80b6-7c3fae74f2ca)
    

## Conclusão

O projeto demonstrou uma redução potencial nos custos de manutenção do sistema de ar dos caminhões através da aplicação de técnicas de Data Science.
