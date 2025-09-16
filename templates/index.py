import streamlit as st


st.header("Streamlit em Python")

if st.button("Clique Aqui"):
    st.write("Minha primeira página me python")


from templates.manterclienteUI import ManterClienteUI

class IndexUI:
 def main():
  ManterClienteUI.main()

IndexUI.main()