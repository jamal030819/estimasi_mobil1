import pickle
import streamlit as st
import pandas as pd

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

# Load the data
df = pd.read_csv('toyota.csv')

st.title('Estimasi Harga Mobil Bekas')

# Filter by year

unique_years = df['year'].unique()
selected_year = st.selectbox('Pilih Tahun:', unique_years)

unique_mileage = df['mileage'].unique()
selected_mileage = st.selectbox('Pilih KM Mobil:', unique_mileage)

unique_tax = df['tax'].unique()
selected_tax = st.selectbox('Pilih Pajak Mobil:', unique_tax)

unique_mpg = df['mpg'].unique()
selected_mpg = st.selectbox('Pilih Konsumsi BBM:', unique_mpg)

unique_engine = df['engineSize'].unique()
selected_engine = st.selectbox('Pilih Konsumsi BBM:', unique_engine)


# Display filtered data
filtered_data = df[df['year']==selected_year]

# Additional option to filter by model
selected_model = st.sidebar.multiselect('Select model(s)', df['model'].unique(), default=df['model'].unique())
filtered_data_by_model = filtered_data[filtered_data['model'].isin(selected_model)]

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[selected_year, selected_mileage, selected_tax, selected_mpg, selected_engine]]
    )
    st.write ('Estimasi Harga Mobil Bekas dalam Ponds :', predict)
    st.write ('Estimasi Harga Mobil Bekas dalam IDR :', predict*19000)
    st.write (f"Showing data for the year {selected_year}")
    st.dataframe(filtered_data)
    st.write(f"Showing data for the year {selected_year} and selected model(s)")
    st.dataframe(filtered_data_by_model)