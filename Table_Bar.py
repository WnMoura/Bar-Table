import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Tabela do Campeonato Brasileiro.xlsx')

df['Pontos'] = df['Pontos'].astype(int)


df = df.head(20)

plt.figure(figsize=(10,6))
plt.barh(df['Time'], df['Pontos'], color='skyblue')
plt.xlabel('Pontos')
plt.ylabel('Time')
plt.title('Pontuação dos times no Campeonato Brasileiro')
plt.gca().invert_yaxis()
plt.show()
