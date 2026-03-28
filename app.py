import streamlit as st
from ranking_dos_1000.ranking import carregar_e_preparar_dados, pesquisar_filmes

def main():
    # Configuração da Interface
    st.set_page_config(page_title="IMDb Search", page_icon="🎬")
    st.title("🎬🍿 Search Engine de filmes do IMDB")
    st.write("🔎Encontra o filme que procuras mesmo sem te lembrares do nome exato!🍿📽️")

    # Carregar os dados
    try:
        df = carregar_e_preparar_dados("top_1000_imdb_movies.csv")
    except FileNotFoundError:
        st.error("Erro: O ficheiro 'top_1000_imdb_movies.csv' não foi encontrado.")
        return

    # Campo de entrada
    query = st.text_input("🔎De que filme estás à procura?", "")

    if query:
        resultados = pesquisar_filmes(query, df)
        
        if resultados:
            st.subheader(f"✅Resultados para: '{query}'")
            for filme in resultados:
                with st.container():
                    st.markdown(f"### {filme['Movie Name']} (Match: {filme['score']:.1f}%)")
                    
                    col1, col2, col3 = st.columns(3)
                    col1.write(f"📅 **Ano:** {int(filme['Year of Release'])}")
                    col2.write(f"⭐ **Nota:** {filme['Movie Rating']}")
                    col3.write(f"⏳ **Duração:** {filme['Watch Time']} min")
                    
                    st.write(f"📖 **Sinopse:** {filme['Description']}")
                    st.divider()
        else:
            st.warning("❌Nenhum filme encontrado! Tente escrever algo diferente.")

# O comando MAIN para executar a aplicação
if __name__ == "__main__":
    main()