#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[5]:


import pandas as pd
import streamlit as st
import pickle


with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
 

# Set the title for your Streamlit app
st.title('Prediction Of CO2 Emissions')

# Create a sidebar for input features
st.sidebar.header('Input Features')

# Define a function to collect user input features
def input_features():
    Engine_Size=st.sidebar.number_input('Insert The Engine Size')
    Cylinders=st.sidebar.selectbox('Select No of Cylinders',('3','4','5','6','8','10','12','16'))
    Fuel_Consumption_Comb1=st.sidebar.number_input('Insert The fuel Consumption')
    data={'Engine Size':Engine_Size,
          'Cylinders':Cylinders,
          'Fuel_Consumption_Comb1':Fuel_Consumption_Comb1}
    features=pd.DataFrame(data,index=[0])
    return features
# Call the input_features() function to collect user input
df=input_features()

# Display the user input features as a subheader and a DataFrame
st.subheader('User Input Features')
st.write(df)

st.subheader('Prediction Result')

if st.button("Predict"):
    if input_features:
        # Make predictions using the loaded model
        predictions = model.predict(df)
        st.write(predictions)
        

    


# In[ ]:





# In[ ]:




