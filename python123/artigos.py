import pandas as pd

# Ler a planilha Excel com os dados
df = pd.read_excel('artigos.xlsx')

# Suponha que as colunas RQ1, RQ2, RQ3, RQ4, RQ5 e RQ6 contenham as respostas
perguntas = ['RQ1', 'RQ2', 'RQ3', 'RQ4', 'RQ5', 'RQ6']

# Função para transformar textos em 1 e vazios em 0
def texto_para_binario(valor):
    if pd.isna(valor) or str(valor).strip() == "":
        return 0  # Campo vazio ou NaN vira 0
    else:
        return 1  # Qualquer texto vira 1

# Aplicar a função em todas as colunas de perguntas
df[perguntas] = df[perguntas].applymap(texto_para_binario)

# Verifique se a transformação foi feita corretamente
print(df[perguntas].head())

# Substituir os valores numéricos por \checkmark ou vazio
df[perguntas] = df[perguntas].replace({1: '\\checkmark', 0: ''})

# Função para gerar cada linha em LaTeX
def gerar_linha_latex(row):
    return f"\\texttt & {{{row['title']}}} & {row['author']} & {row['RQ1']} & {row['RQ2']} & {row['RQ3']} & {row['RQ4']} & {row['RQ5']} & {row['RQ6']} & {{{row['year']}}} \\\\"

# Gerar as linhas da tabela
linhas_latex = df.apply(gerar_linha_latex, axis=1)

# Cabeçalho e rodapé da tabela LaTeX
cabecalho = r'''
\begin{longtable}{p{0.5cm}p{5cm}p{5cm}p{0.5cm}p{0.5cm}p{0.5cm}p{0.5cm}p{0.5cm}p{1.0cm}}
\caption{Papers Selected}
\label{tab:selected}\\
\toprule
ID & Title & Authors & RQ1 & RQ2 & RQ3 & RQ4 & RQ5 & RQ6 & Year\\
\midrule
\endfirsthead

\multicolumn{9}{c}%
{{\tablename\ \thetable{} -- \small Continued from previous page}} \\
\toprule
ID & Title & Authors & RQ1 & RQ2 & RQ3 & RQ4 & RQ5 & RQ6 & Year\\
\midrule
\endhead

\midrule
\multicolumn{9}{r}{{Continued on next page}} \\
\endfoot

\bottomrule
\endlastfoot
'''

rodape = r'''
\end{longtable}
'''

# Juntar tudo
conteudo_tabela = cabecalho + '\n'.join(linhas_latex) + rodape

# Salvar em arquivo .tex
with open('tabela_longtable.tex', 'w') as f:
    f.write(conteudo_tabela)

print("Tabela LaTeX gerada com sucesso!")
