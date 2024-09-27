import pandas as pd

# Carregue seus dados, substitua 'seu_arquivo.csv' pelo caminho do seu arquivo
# e 'nome_da_coluna' pelo nome da coluna que contém os nomes dos journals
df = pd.read_excel('/home/astro/python123/artigos12.xlsx')

# Contar o número de ocorrências de cada journal
journal_counts = df['journal'].value_counts()

# Gerar o código LaTeX da tabela
table_latex = r"""
\begin{table}[H] 
\centering
\caption{Distribution of Papers by Conference}
\label{tab:conferences}
\begin{tabular}{p{10.5cm}p{2cm}}
\toprule
Conference & \multicolumn{1}{c}{Papers} \\
\midrule
"""

# Adicionar cada journal e seu respectivo número de ocorrências na tabela
for journal, count in journal_counts.items():
    table_latex += f'{journal} & \\multicolumn{{1}}{{c}}{{{count}}} \\\\\n'

# Finalizar a tabela
table_latex += r"""
\bottomrule
\end{tabular}
\end{table}
"""

# Exibir o código gerado
print(table_latex)
