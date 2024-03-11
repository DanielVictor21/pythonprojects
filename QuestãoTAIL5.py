import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('https://raw.githubusercontent.com/franklinthony/dataset/master/titanic_disaster.csv', sep = ',')

# Primeiro, vou renomear os tipos de dados para português, apenas para melhorar a visualização geral, usando a função rename por colunas do pandas.
dataset = dataset.rename(columns={
    'Survived': 'Sobreviveu',
    'Pclass': 'Tipo_passagem',
    'SibSp': 'Irmaos_conjuges_a_bordo',
    'Parch': 'Pais_filhos_a_bordo',
    'Ticket': 'Numero_do_ticket',
    'Fare': 'Tarifa',
    'Cabin': 'Cabine',
    'Embarked': 'Porto_embarque',
    'Sex': 'Genero',
    'Age': 'Idade',
    'male': 'Homem',
    'female': 'Mulher'
})

contagem_sexo = dataset['Genero'].value_counts()

contagem_sexo.plot(kind='bar', color=['blue', 'pink'])
plt.title('Quantidade de Homens e Mulheres no Titanic')
plt.xlabel('Sexo')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)  # Ajusta a rotação dos rótulos no eixo x
plt.show()
print(contagem_sexo)
# contagem_tipo_passagem = dataset.groupby(['Genero', 'Tipo_passagem'])['Tipo_passagem'].count()
# print(contagem_tipo_passagem)
# media_idade_por_tipo_passagem = dataset.groupby(['Genero', 'Tipo_passagem'])['Idade'].mean().unstack()
# print(media_idade_por_tipo_passagem)
# sobrevivencia_por_genero_e_classe = dataset.groupby(['Genero', 'Tipo_passagem', 'Sobreviveu'])[''].count()
# print(sobrevivencia_por_genero_e_classe)