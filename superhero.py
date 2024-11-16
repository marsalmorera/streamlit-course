import streamlit as pt


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