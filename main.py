import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

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

# Substituir valores ausentes representados como 'na' por NaN e depois preencher com a média
previous_years_data.replace('na', np.nan, inplace=True)
present_year_data.replace('na', np.nan, inplace=True)

# Converter todas as colunas para tipo float, exceto a coluna 'class'
previous_years_data = previous_years_data.apply(pd.to_numeric, errors='coerce')
present_year_data = present_year_data.apply(pd.to_numeric, errors='coerce')

# Preencher valores ausentes com a média das colunas
previous_years_data.fillna(previous_years_data.mean(), inplace=True)
present_year_data.fillna(present_year_data.mean(), inplace=True)

# Separar features e target
X = previous_years_data.drop('class', axis=1)
y = previous_years_data['class']

# Normalizar os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Subamostragem para desenvolvimento e testes rápidos (10% dos dados)
X_sample, _, y_sample, _ = train_test_split(X_scaled, y, test_size=0.9, random_state=42)

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_sample, y_sample, test_size=0.2, random_state=42)

# Treinar o modelo de Regressão Logística
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train, y_train)

# Avaliar o modelo
y_pred = log_reg.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f"Acurácia do modelo de Regressão Logística:\n {accuracy*100} %")
print("Matriz de Confusão:\n", conf_matrix)
print("Relatório de Classificação:\n", class_report)

# Treinar o modelo de Random Forest com GridSearchCV
param_grid = {
    'n_estimators': [100, 200], 
    'max_depth': [None, 10], 
    'min_samples_split': [2, 10]
}
rf_clf = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(rf_clf, param_grid, cv=3, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

best_rf_clf = grid_search.best_estimator_

# Avaliar o modelo
y_pred_rf = best_rf_clf.predict(X_test)
accuracy_rf = accuracy_score(y_test, y_pred_rf)
conf_matrix_rf = confusion_matrix(y_test, y_pred_rf)
class_report_rf = classification_report(y_test, y_pred_rf)

print(f"Acurácia do modelo de Random Forest:\n {accuracy_rf * 100} %")
print("Matriz de Confusão:\n", conf_matrix_rf)
print("Relatório de Classificação:\n", class_report_rf)

# Importância das características
importances = best_rf_clf.feature_importances_
indices = np.argsort(importances)[::-1]

print("Importâncias das características:")
for f in range(X.shape[1]):
    print(f"{X.columns[indices[f]]}: {importances[indices[f]]}")

# Avaliar o modelo treinado no conjunto de dados do ano presente
X_present = scaler.transform(present_year_data.drop('class', axis=1))
y_present = present_year_data['class']

y_pred_present = best_rf_clf.predict(X_present)
accuracy_present = accuracy_score(y_present, y_pred_present)
conf_matrix_present = confusion_matrix(y_present, y_pred_present)
class_report_present = classification_report(y_present, y_pred_present)

print(f"Acurácia do modelo no conjunto de dados do ano presente:\n {accuracy_present * 100} %\n")
print(f"Matriz de Confusão:\n {conf_matrix_present}\n")
print(f"Relatório de Classificação:\n {class_report_present}\n")

sns.heatmap(conf_matrix_present, cmap='coolwarm', annot=True, linewidth=1, fmt='d')
plt.show()
