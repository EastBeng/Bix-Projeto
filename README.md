# BIX-Technology-Technical-Challenge: Data Science Project Details and Challenge Responses
This repository contains the code and data used to solve the technical Data Science challenge proposed by BIX Tecnologia, related to optimizing maintenance planning.

## Project Description
BIX Tecnologia has hired a Data Science consultancy to improve the maintenance planning of an outsourced transport fleet. The project focuses on reducing maintenance costs of the trucks' air system by identifying failures predictively.

## Technologies Used
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

## Repository Contents

- `air_system_previous_years.csv`: Historical maintenance data from previous years.
- `air_system_present_year.csv`: Maintenance data from the current year for validation.
- `main.py`: Code used to load, preprocess, model, and evaluate the data.
  
## Steps Taken

1. **Data Preparation:**
   - Data loading.
   - Transformation of the 'class' column to numeric values.
   - Handling missing values.

2. **Modeling:**
   - Use of the Random Forest machine learning model.
   - Training the models on historical data.
   - Evaluation of models using metrics such as accuracy, confusion matrix, and classification report.

3. **Evaluation on the Present Year Dataset:**
   - Use of the trained Random Forest model to make predictions on the present year's data.
   - Evaluation of the model's generalization ability.

## Results
- **Random Forest Model:**
  - Accuracy: 98.8%
  - Confusion Matrix
    
      ![image](https://github.com/EastBeng/Bix-Projeto/assets/44300759/9fc44ce3-86aa-4b28-82e8-cf91f5bca63f)

    
  - Classification Report
  
               precision    recall  f1-score   support

           0       0.99      1.00      0.99     15625
           1       0.89      0.56      0.69       375
        accuracy                       0.99     16000
        macro avg  0.94      0.78      0.84     16000
        weighted   0.99      0.99      0.99     16000



## Conclusion

This project demonstrates the successful application of Data Science techniques to optimize the maintenance planning of a third-party transport fleet's air system. Using machine learning, particularly the Random Forest model, we achieved an accuracy of 98.8% in predicting maintenance needs. This high accuracy underscores the effectiveness of predictive analytics in identifying potential failures preemptively, aiming to reduce maintenance costs and enhance operational efficiency. These findings establish a robust foundation for future advancements in maintenance strategies, ensuring continuous improvements in fleet management and reliability.

## Challenge Answer

1. What steps would you take to solve this problem? Please describe as completely and clearly as possible all the steps that you see as essential for solving the problem.
- To solve this problem, I would start by thoroughly understanding the data, including examining the features, the target variable, and identifying any missing values. Preprocessing would follow, where I’d handle missing values and convert categorical data into numerical formats. Then, I’d explore various machine learning models to identify the best fit. Hyperparameter tuning using GridSearchCV would optimize the chosen model. Finally, validation on the present year's data would ensure the model’s generalization.

2. Which technical data science metric would you use to solve this challenge? Ex: absolute error, rmse, etc. 
- Accuracy, precision, recall, and F1-score are crucial metrics. Accuracy gives an overall performance snapshot, while precision and recall provide insights into the model’s ability to distinguish between positive and negative cases. F1-score is particularly important when dealing with imbalanced classes.

3. Which business metric  would you use to solve the challenge?
- The primary business metric would be the reduction in maintenance costs. Accurate predictions of maintenance needs can help avoid unnecessary repairs and reduce downtime, leading to cost savings.
  
4. How do technical metrics relate to the business metrics?
- Technical metrics ensure the model performs well in predicting outcomes, which directly impacts the business metric by reducing maintenance costs through precise predictions.
  
5. What types of analyzes would you like to perform on the customer database?
- I would perform exploratory data analysis to understand the data distribution, detect patterns, and identify correlations. Feature importance analysis would help in understanding which factors most influence the maintenance needs.
  
6. What techniques would you use to reduce the dimensionality of the problem? 
- Techniques like Principal Component Analysis (PCA) and feature selection methods such as Recursive Feature Elimination (RFE) would be used to reduce dimensionality.
  
7. What techniques would you use to select variables for your predictive model?
- I’d use feature importance scores from models like Random Forest, as well as correlation analysis and statistical tests to select the most relevant variables.
  
8. What predictive models would you use or test for this problem? Please indicate at least 3.
- I would test Logistic Regression, Random Forest, and Gradient Boosting models to find the best predictive model for this problem.
  
9. How would you rate which of the trained models is the best?
- By comparing their performance metrics like accuracy, precision, recall, and F1-score on a validation dataset, as well as evaluating their performance on unseen data.
  
10. How would you explain the result of your model? Is it possible to know which variables are most important?
- The results can be explained using performance metrics and confusion matrices. Feature importance scores from models like Random Forest can help identify the most influential variables.
  
11. How would you assess the financial impact of the proposed model?
- By calculating the reduction in maintenance costs and comparing it to the current maintenance expenditure, I can assess the financial impact.
  
12. What techniques would you use to perform the hyperparameter optimization of the chosen model?
- I’d use GridSearchCV or RandomizedSearchCV to systematically search for the best hyperparameters for the model.
  
13. What risks or precautions would you present to the customer before putting this model into production?
- I would highlight the importance of monitoring the model’s performance over time, the need for regular retraining with new data, and potential changes in the data distribution that could affect model accuracy.
  
14. If your predictive model is approved, how would you put it into production?
- I would use a robust deployment pipeline, possibly involving Docker for containerization and a cloud service like AWS or Azure for scalability. Monitoring and logging would be set up to track model performance.
  
15. If the model is in production, how would you monitor it?
- Continuous monitoring of performance metrics, setting up alerts for significant drops in accuracy, and regular evaluations with new data would be essential.
  
16. If the model is in production, how would you know when to retrain it?
- Monitoring for performance degradation over time and significant changes in data patterns would signal the need for retraining. Setting a predefined schedule for retraining based on new data influx could also be a strategy.

