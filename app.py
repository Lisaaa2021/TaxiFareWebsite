import streamlit as st
import requests

st.markdown("""
    # TaxiFareModel

    ## Version 1.0
    developed by robotlisa
""")

st.text("") # add a empty line

date = st.text_input('Date and time. Format: 2012-10-06 12:10:20')
p_lat = st.text_input('Pickup Latitude')
p_lon = st.text_input('Pickup Longtitude')
d_lat = st.text_input('Dropoff Latitude')
d_lon = st.text_input('Dropoff Longtitude')
passenger = st.text_input("Passanger_count")

url = f'''https://taxifare.lewagon.ai/predict?pickup_datetime={date}&pickup_longitude={p_lat}&pickup_latitude={p_lon}&dropoff_longitude={d_lat}&dropoff_latitude={d_lon}&passenger_count={passenger}'''

all_inputs = date and p_lat and p_lon and d_lat and d_lon and passenger
if all_inputs:
    st.json(dict(date = date, p_lat=p_lat,p_lon = p_lon, d_lat=d_lat, d_lon = d_lon, passenger = passenger))
    pred_clicked = st.button('Predict')
    fare = 0
    if pred_clicked:
        res = requests.get(url)
        prediction = res.json()['prediction']
        if res.status_code == 200:
            st.write('Predicted Price')
            st.write(prediction)
        else:
            st.write('Sorry, something went wrong 😢 Please try again')
st.write('Sorry, something went wrong 😢 Please try again')
