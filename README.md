# BIX-Tecnologia-Desafio-Tecnico: Projeto de Data Science

Este repositório contém o código e os dados utilizados para resolver o desafio técnico de Data Science proposto pela BIX Tecnologia, relacionado à otimização do planejamento de manutenção.

![image](https://github.com/EastBeng/Bix-Projeto/assets/44300759/8af2befb-ff2d-4207-80b1-a8c57de29c3f)
![image](https://github.com/EastBeng/Bix-Projeto/assets/44300759/b97bf403-cd3a-4ba7-85a0-8c06914cbe9e)
![image](https://github.com/EastBeng/Bix-Projeto/assets/44300759/f53794d1-90d8-433a-94d8-4bea7a41f60c)
![image](https://github.com/EastBeng/Bix-Projeto/assets/44300759/45194ce5-468a-47ac-b556-87fce5c03caf)
![image](https://github.com/EastBeng/Bix-Projeto/assets/44300759/d0b38882-8c83-471f-8267-413fa2aa42db)
<div height = "20px"><img src="//github.com/EastBeng/Bix-Projeto/assets/44300759/d56bb6eb-7237-4e52-8bfc-5073b6de3de7"/></div>




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
    
    ![image](https://github.com/EastBeng/BIX-Tecnologia-Desafio-Tecnico/assets/44300759/d9865a0d-0e15-4629-978b-001d4be9e238)

## Conclusão

O projeto demonstrou uma redução potencial nos custos de manutenção do sistema de ar dos caminhões através da aplicação de técnicas de Data Science.
