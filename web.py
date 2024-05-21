import stream as st
import pandas as pd
# import pillow as pil
import matplotlib.pyplot as plt

st.title('MYweb app')
st.subheader('Dataset')
st.success('datasets')

# a=st.text_input("name")
df=pd.read_csv("p.csv")
fig=plt.figure()
plt.line(df)
st.pyplot(fig)