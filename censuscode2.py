import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
st.set_page_config(page_title = 'Census Evaluation',
                    page_icon = 'random',
                    layout = 'wide',
                    initial_sidebar_state = 'collapsed'
                    )

st.set_option('deprecation.showPyplotGlobalUse', False)
@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race', 'gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()




st.title('Census Visualisation App')

st.text('''
This app allows the user to visualise 
the census income''')


st.header('View data')
with st.beta_expander('View dataset'):
	st.table(census_df.head(300))
st.subheader('Column description')
if st.checkbox('Show summary'):
	st.table(census_df.describe())




beta_col1,beta_col2,beta_col3 = st.beta_columns(3)
with beta_col1:
	if st.checkbox('Show column names'):
		st.table(census_df.columns)
with beta_col2:
	if st.checkbox('Show column datatypes'):
		st.table(census_df.dtypes)
with beta_col3:
	if st.checkbox('View column data'):
		cols = st.selectbox('Select column',(census_df.columns))
		st.table(census_df[cols])	