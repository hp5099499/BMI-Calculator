import streamlit as st

from PIL import Image


st.title("This is a header")
st.text('hello guys')
st.markdown('###This is a markdown')
st.success("data added successfully")
st.warning("data set is not accurate")
st.error("enemy is ahead")
st.info("whats the news?")
exp=ZeroDivisionError("TRYING TO DIVIDE THE ZERO")
st.exception(exp)
st.write("text withj rule")
st.write(range(10))
  
#checkbox with if condition
if st.checkbox("Show/Hide"):
   img = Image.open("pie.png")
   st.image(img,width=500) 

# radio button

# first argument is the title of the radio button
# second arguement is the options for the radio button
status=st.radio("select the gender:",("Male","female"))
if status=="Male":
   st.success("You are male")
else:
   st.success("You are Female")

# Selection box

# first arguement takes the title of the selectionbox
# second arguement take option
hobby=st.selectbox("Hobbies:",['Dancing','Reading','Sports'])
st.write(" Your hobby is :",hobby)

# Multiselect box

# First arguement takes the box title 
# Second arguement takes the box title
Hobbies=st.multiselect("Hobbies: ",["Dancing",'reading','running'])
st.write("You have selected ",len(Hobbies),'Hobbies')

# Button that does something
st.button("Click me  for no reason")
# create  a button ,that when clicked ,shows the text
if st.button("About"):
   st.text("Welcome to the world of analysis")

# text input
# SAVE the input text in the variable 'name'
# first arguement displays a default test inside the text input area
name =st.text_input("enter the name","TYPE here.......")

# display the name when the submit button is clicked
# .title() is used tto get the input text string
if st.button('SUBMIT'):
   result=name.title()
   st.success(result)

# slider 
# first arguement takes the title  of the slider
# last arguement te=akes the end number
level=st.slider("select the level",1,4)

# print the level 
# format() is used to print the value of a variable at a specific postion
st.text('Selected: {}'.format(level))