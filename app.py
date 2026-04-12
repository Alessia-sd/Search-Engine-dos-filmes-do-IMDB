import streamlit as st
from ranking_dos_1000.ranking import carregar_e_preparar_dados, pesquisar_filmes

# 1. Implementação de Cache
@st.cache_data
def carregar_dados_cache():
    return carregar_e_preparar_dados("top_1000_imdb_movies.csv")

def main():
    # Configuração da Interface
    st.set_page_config(page_title="IMDb Search", page_icon="🎬")
    st.title("🎬🍿 Search Engine de filmes do IMDB")
    st.write("🔎Encontra o filme que procuras mesmo sem te lembrares do nome exato!🍿📽️")

    # Carregar os dados usando a função de cache
    try:
        df = carregar_dados_cache()
    except Exception:
        st.error("Erro: O ficheiro 'top_1000_imdb_movies.csv' não foi encontrado.")
        return

    # Campo de entrada
    query = st.text_input("🔎De que filme estás à procura?", "")

    if query:
        resultados = pesquisar_filmes(query, df)
        
        if resultados:
            st.subheader(f"✅Resultados para: '{query}'")
            for filme in resultados:
                # 2. Utilização de Expander (Componente interativo para mostrar detalhes apenas quando o usuario quiser)
                # O título do expander já mostra o nome e o match
                with st.expander(f"🎥 {filme['Movie Name']} (Match: {filme['score']:.1f}%)"):
                    
                    # 3. Utilização de colunas com métricas para melhor visualização
                    col1, col2, col3 = st.columns(3)
                    col1.metric("📅 Ano", int(filme['Year of Release']))
                    col2.metric("⭐ Nota", filme['Movie Rating'])
                    col3.metric("⏳ Duração", f"{filme['Watch Time']} min")
                    
                    st.write(f"📖 **Sinopse:** {filme['Description']}")
        else:
            st.warning("❌Nenhum filme encontrado! Tente escrever algo diferente.")

# O comando MAIN para executar a aplicação
if __name__ == "__main__":
    main()
