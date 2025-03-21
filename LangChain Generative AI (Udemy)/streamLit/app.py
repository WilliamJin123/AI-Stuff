import streamlit as st
import pandas as pd
import numpy as np

# RUN WITH COMMAND: streamlit run {filename}


## Title
st.title("Hello Streamlit")
#text
st.write("text")
#dataframe
df = pd.DataFrame({
    'first' : [1,2,3,4],
    'second': [5,6,7,8]
    
})

#display dataframe
st.write("Here is the dataframe")
st.write(df)

#line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns = ['a','b','c']
)
st.line_chart(chart_data)