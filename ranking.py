import pandas as pd
from rapidfuzz import process, utils

def carregar_e_preparar_dados(caminho_csv):
    """
    1. Importa o dataset utilizando Pandas.
    2. Limpar e tratar os dados.
    """
    # index_col=0 evita que o pandas crie uma coluna extra
    df = pd.read_csv(caminho_csv, index_col=0)
    
    # - LIMPEZA DE DADOS -
    # Esta linha limpa parênteses ou textos e converte o ano para número (float).
    df['Year of Release'] = df['Year of Release'].astype(str).str.extract(r'(\d+)').astype(float)
    
    # Remove linhas onde o nome do filme esteja vazio para evitar erros na pesquisa
    df = df.dropna(subset=['Movie Name'])
    
    return df

def pesquisar_filmes(consulta_utilizador, dataset):
    """
    Implementa a pesquisa aproximada com RapidFuzz.
    """
    if not consulta_utilizador:
        return []

    # Realiza a pesquisa aproximada
    # processor=utils.default_process: ignora maiúsculas/minúsculas (ex: Star = star)
    # score_cutoff=80: limite mínimo de semelhança exigido
    resultados = process.extract(
        consulta_utilizador, 
        dataset["Movie Name"], 
        processor=utils.default_process, 
        score_cutoff=80
    )
    
    lista_resultados = []
    for nome, score, indice in resultados:
        # Recupera a linha completa do filme usando o índice
        dados_filme = dataset.loc[indice].to_dict()
        dados_filme['score'] = score
        lista_resultados.append(dados_filme)
        
    return lista_resultados

# Bloco de execução MAIN
if __name__ == "__main__":
    print("A testar lógica de limpeza e pesquisa...")
    try:
        # Teste
        dados = carregar_e_preparar_dados("top_1000_imdb_movies.csv")
        print(f"Dataset carregado com {len(dados)} filmes.")
        
        teste = pesquisar_filmes("star wars", dados)
        if teste:
            print(f"Sucesso! Encontrado: {teste[0]['Movie Name']}")
    except Exception as e:
        print(f"Erro no teste: {e}")