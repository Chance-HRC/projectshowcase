# --------------------------------------------------------------------------------
# Imports
import streamlit as st
import io
# --------------------------------------------------------------------------------
#sidebar
st.sidebar.title("IF THERE ARE ANY BUGS PLEASE CONTACT")
st.sidebar.markdown("@ChanceDehar@hotmail.com")
# --------------------------------------------------------------------------------
#website explanation
st.title("PDF Site")
st.divider()
st.write("The link to the site is f@https://chance-hrc.github.io/PDF-Tools/")
st.divider()
st.write("The purpose of this site is to create a server based website. This means the site doesnt require any internal downloads"
         "as well as not saving anything once submitted. This means for Horizons which has some documents they might want to keep"
         "secure, they can use this website without any stress")
st.divider()
st.image("images/pdf_index.png")
st.write("This section of the site simply explains its uses")
st.divider()
st.image("images/pdf_combine.png")
st.write("This section of the site lets the user combine different PDF(s) and there pages, letting you combine"
         "or get rid of pages between documents")
st.divider()
st.image("images/pdf_compress.png")
st.write("This section lets you compress pdf files so you can store them easier with less storage taken")
st.divider()
st.image("images/pdf_encrypt.png")
st.write("This section lets you encrypt the pdf file with a password, so when you send it, only specific people will be able to"
         "open it")
st.divider()
# --------------------------------------------------------------------------------