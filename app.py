import streamlit as st

############ PAGE SETUP ############ 
# This is that the page title that changes. 
st.set_page_config(
    page_title="Superhero APP",
    layout="centered", # or wide
    page_icon="🚗", # choose your favorite icon
    initial_sidebar_state="collapsed" # or expanded
)

############ HEADER ############ 

# User input 

favorite_color = st.text_input('Enter your favorite color:')
favorite_animal = st.text_input('Enter your favorite animal:')
random_number = st.number_input('Enter your lucky number:', step=1)
#Check superheroes. 
superpower= st.selectbox("Choose your superpower:",
                         ['Flying', "Invisibility", "Super Strength"])

# More inputs. 


st.text(f'My favorite color is {favorite_color}')
st.text(f'My favorite animal is {favorite_animal}')
st.text(f'My lucky number is {random_number}')
st.text(f'Superpower: {superpower}')

#Display a motto
st.subheader('Your Superhero Motto:')
st.write(f'With great power comes great {superpower.lower()}!')