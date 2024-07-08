import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
previous_years_data = pd.read_csv('air_system_previous_years.csv')
present_year_data = pd.read_csv('air_system_present_year.csv')

# Exibir as primeiras linhas dos datasets
print("Primeiras linhas do conjunto de dados de anos anteriores:")
print(previous_years_data.head())

print("\nPrimeiras linhas do conjunto de dados do ano presente:")
print(present_year_data.head())

# Informações básicas sobre os datasets
print("\nInformações do conjunto de dados de anos anteriores:")
print(previous_years_data.info())

print("\nInformações do conjunto de dados do ano presente:")
print(present_year_data.info())

# Verificar os valores únicos na coluna 'class'
print("\nValores únicos em 'class' no conjunto de dados anterior:")
print(previous_years_data['class'].unique())

print("\nValores únicos em 'class' no conjunto de dados presente:")
print(present_year_data['class'].unique())


# Transformar a coluna 'class'
previous_years_data['class'] = previous_years_data['class'].map({'pos': 1, 'neg': 0})
present_year_data['class'] = present_year_data['class'].map({'pos': 1, 'neg': 0})

# Substituir valores ausentes representados como 'na' por 0
previous_years_data.replace('na', 0, inplace=True)
present_year_data.replace('na', 0, inplace=True)

# Verificar o tipo de dados e converter colunas para float
previous_years_data = previous_years_data.astype(float)
present_year_data = present_year_data.astype(float)

# Separar features e target
X = previous_years_data.drop('class', axis=1)
y = previous_years_data['class']

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo de Regressão Logística
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train, y_train)

# Avaliar o modelo
y_pred = log_reg.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print("Acurácia do modelo de Regressão Logística:", accuracy)
print("Matriz de Confusão:\n", conf_matrix)
print("Relatório de Classificação:\n", class_report)

# Treinar o modelo de Random Forest
rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
rf_clf.fit(X_train, y_train)

# Avaliar o modelo
y_pred_rf = rf_clf.predict(X_test)
accuracy_rf = accuracy_score(y_test, y_pred_rf)
conf_matrix_rf = confusion_matrix(y_test, y_pred_rf)
class_report_rf = classification_report(y_test, y_pred_rf)

print("Acurácia do modelo de Random Forest:", accuracy_rf)
print("Matriz de Confusão:\n", conf_matrix_rf)
print("Relatório de Classificação:\n", class_report_rf)



X_present = present_year_data.drop('class', axis=1)
y_present = present_year_data['class']

# Avaliar o modelo treinado no conjunto de dados do ano presente
y_pred_present = rf_clf.predict(X_present)
accuracy_present = accuracy_score(y_present, y_pred_present)
conf_matrix_present = confusion_matrix(y_present, y_pred_present)
class_report_present = classification_report(y_present, y_pred_present)

print(f"Acurácia do modelo no conjunto de dados do ano presente:\n {accuracy_present* 100 } %\n")

print(f"Matriz de Confusão:\n {conf_matrix_present}\n")

print(f"Relatório de Classificação:\n {class_report_present}\n")


sns.heatmap(conf_matrix_present, cmap='coolwarm', annot=True, linewidth=1, fmt='d')
plt.show()