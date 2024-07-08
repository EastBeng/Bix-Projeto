# BIX-Tecnologia-Desafio-Tecnico: Detalhes Projeto de Data Science e Respostas Desafio

Este repositório contém o código e os dados utilizados para resolver o desafio técnico de Data Science proposto pela BIX Tecnologia, relacionado à otimização do planejamento de manutenção.

## Descrição do Projeto

A BIX Tecnologia contratou uma consultoria de Data Science para melhorar o planejamento de manutenção de uma frota terceirizada de transportes. O foco do projeto é reduzir os custos de manutenção do sistema de ar dos caminhões, identificando falhas de forma preditiva.

## Tecnologias Utilizadas
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

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

## Repostas - Desafio

1. What steps would you take to solve this problem? Please describe as completely and clearly as possible all the steps that you see as essential for solving the problem.

2. Which technical data science metric would you use to solve this challenge? Ex: absolute error, rmse, etc. 

3. Which business metric  would you use to solve the challenge?

4. How do technical metrics relate to the business metrics?

5. What types of analyzes would you like to perform on the customer database?

6. What techniques would you use to reduce the dimensionality of the problem? 

7. What techniques would you use to select variables for your predictive model?

8. What predictive models would you use or test for this problem? Please indicate at least 3.

9. How would you rate which of the trained models is the best?

10. How would you explain the result of your model? Is it possible to know which variables are most important?

11. How would you assess the financial impact of the proposed model?

12. What techniques would you use to perform the hyperparameter optimization of the chosen model?

13. What risks or precautions would you present to the customer before putting this model into production?

14. If your predictive model is approved, how would you put it into production?

15. If the model is in production, how would you monitor it?

16. If the model is in production, how would you know when to retrain it?

