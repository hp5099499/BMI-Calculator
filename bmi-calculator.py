import streamlit as st

st.title('Welcome to BMI Calculator')

weight=st.number_input("Enter the weight (in kgs)")

# status take height input 
# radio button to choose the height format
status=st.radio('Select your height format:',('cms','meters',"feet"))

# compare the state value
if(status == 'cms'):
    # take height input in centimeters
    height = st.number_input('Centimeters')
 
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")
 
elif(status == 'meter'):
    # take height input in meters
    height = st.number_input('Meters')
 
    try:
        bmi = weight / (height**2)
    except:
        st.text("Enter some value of height")

else:
    # take height input in feet
    height = st.number_input('Feet')
 
    try:
        bmi = weight / ((height/3.28)**2)
    except:
        st.text("Enter some value of height")
 
if(st.button('Calculate BMI')):
 
    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(bmi))
 


    if bmi<16:
        st.error("YOU are extremely Under Weight")
    elif bmi>=16 and bmi<18.5:
        st.error("YOU are Under Weight")
    elif bmi>=18.5 and bmi<25:
        st.success("YOU are Healthy") 
    elif bmi>=25 and bmi<30:
        st.error("YOU are Over Weight") 
    elif bmi>=30:
        st.error("YOU are extremly  OverWeight")