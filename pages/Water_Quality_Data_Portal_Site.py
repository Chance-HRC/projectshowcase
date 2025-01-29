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
st.title("Water Quality Data Portal")
st.divider()
st.write("This site currently isn't live")
st.divider()
st.write("The purpose of this site is to create an online site in which the public can see Horizons water quality data they collect,"
         "currently there is on easy way to access it, so this site will let you see it in graph form and download the data. There will"
         "lots of room for growth")
st.divider()
st.image("images/WQDPhome.png")
st.write("This section of the site simply explains its uses as well as giving a disclaimer")
st.divider()
st.image("images/WQDPsite.png")
st.write("This section of the site lets the user search through a table or map of the region, letting you choose a site you want data for")
st.divider()
st.image("images/WQDPsitezoom.png")
st.write("We can see we can also zoom into the map and more sites open to make it easier to understand with all points not popping out at you")
st.divider()
st.image("images/WQDOvisualisation.png")
st.write("This section lets you see the name of the site, a iframe explaining the current water quality type and a button to download it. "
         "We can also see it represents the data in a scatter graph to let the user see any trends, also letting the user select specific dates")
st.divider()
st.image("images/WQDOvisualisation2.png")
st.write("There is also a function to see it in bargraph form if ther prefer")
st.divider()
# --------------------------------------------------------------------------------