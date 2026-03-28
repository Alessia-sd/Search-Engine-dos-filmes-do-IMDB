#### Construção de um Search Engine dos filmes do IMDB
 
Neste projeto final, irei construir uma aplicação interativa que permite pesquisar filmes do ranking dos 1000 melhores filmes do IMDb.
Para isso, irei utilizar duas bibliotecas muito poderosas em Python: 

- RapidFuzz – biblioteca para fuzzy matching, ou seja, correspondência 
aproximada entre strings. 
- Streamlit – ferramenta simples para criar interfaces web interativas em Python. 

A aplicação permitirá que os utilizadores encontrem filmes, mesmo que não se lembrem do seu nome exato, recorrendo à correspondência aproximada de texto. 

Tópicos do desafio: 
1. Importar o dataset (top_1000_imdb_movies.csv). 
2. Limpar e preparar os dados. 
3. Criar uma função de pesquisa que utilize RapidFuzz para encontrar filmes semelhantes. 
4. Construir uma interface interativa com Streamlit.

Para executar no terminal: stremilt run app.py

#### Conclusão
- Tratamento de Dados: Limpeza completa via Pandas, incluindo a normalização da coluna de anos e remoção de registos incompletos.

- Motor de Busca: Implementação de lógica fuzzy com a biblioteca RapidFuzz, configurada para aceitar variações de escrita e ignorar a diferença entre maiúsculas e minúsculas.

- Interface: Desenvolvimento de uma UI interativa em Streamlit, organizada com containers e colunas para uma visualização clara dos resultados e metadados dos filmes.
