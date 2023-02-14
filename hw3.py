import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#data 

data=pd.read_csv('gapminder_with_codes.csv')
data_2007=data[data['year']==2007]


#name details 

st.header("Name: MAXWELL CHANZU MIHIGA")
st.header("Reg No: SCT211-0722/2021")
st.header("B.Sc COMPUTER SCIENCE")
st.header(" SCIENTIFIC COMPUTING")
st.header("ICS2207")
st.header("VIOLIN PLOT FOR DATA FOR 2007")

fg = plt.figure(figsize=(10,8))
plt.title("Life Expectancy")

sns.violinplot(data=data_2007,x='lifeExp',scale='count')
#show plots
st.pyplot(fg)


plt.title("Populaton")
sns.violinplot(data=data_2007,x='pop',scale='count')
st.pyplot(fg)


plt.title("GDP")
sns.violinplot(data=data_2007,x='gdpPercap',scale='count')
st.pyplot(fg)

