import streamlit as st
import pyshorteners

st.set_page_config(page_title="Encurtador de Links", page_icon="🔗")
st.title("🔗 Encurtador de Links")
st.markdown("Cole aqui o seu link longo e receba uma versão curta!")

url = st.text_input("Insira o link aqui:")

if st.button("Encurtar"):
    if url:
        try:
            s = pyshorteners.Shortener()
            short_url = s.isgd.short(url)
            st.success("✅ Link encurtado com sucesso!")
            st.code(short_url, language='text')
        except Exception as e:
            st.error(f"Erro ao encurtar o link: {e}")
    else:
        st.warning("Por favor, insira um link válido.")
