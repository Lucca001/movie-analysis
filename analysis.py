import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset
data = pd.read_csv('movies.csv')

# Contagem de filmes por gênero
genre_count = data['genre'].value_counts()

plt.figure(figsize=(8, 5))
genre_count.plot(kind='bar', color='skyblue')
plt.title('Quantidade de Filmes por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Quantidade')
plt.savefig('genre_count.png')
plt.show()

# Nota média por ano
avg_rating_per_year = data.groupby('year')['rating'].mean()

plt.figure(figsize=(10, 5))
avg_rating_per_year.plot(color='orange')
plt.title('Nota Média por Ano')
plt.xlabel('Ano')
plt.ylabel('Nota Média')
plt.savefig('avg_rating_per_year.png')
plt.show()
