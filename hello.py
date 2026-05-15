# código de geração do gráfico 
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o csv
df = pd.read_csv(r"gasolina.csv")

# Exibir as primeiras linhas
print(df.head())

# Gráfico
sns.lineplot(data=df, x="dia", y="venda")

# Salvar imagem
plt.savefig("grafico.png", dpi=300, bbox_inches="tight")

# mostrar gráfico
plt.show()