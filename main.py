import streamlit as st
import plotly.express as px
from weather import get_data

st.title("Weather forecast for the Next days")
place = st.text_input("Place:")
days = st.slider("Forcast days: ", min_value=1, max_value=5,
                 help="Select the number of days you want the forecast for?")
data = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{data} for the next {days} days in {place}")

if place:
    weather_data = get_data(place, days)
    if data == "Temperature":
        temperatures_kelvin = [item["main"]["temp"] for item in weather_data]
        temp_celsius = [item - 273.15 for item in temperatures_kelvin]
        dates = [item["dt_txt"] for item in weather_data]
        figure = px.line(x=dates, y=temp_celsius, labels={"x": "Dates", "y": "Temperatures"})
        st.plotly_chart(figure)
    if data == "Sky":
        sky_data = [item["weather"][0]["main"] for item in weather_data]
        images_dict = {"Rain": "images/rain.png", "Clouds": "images/cloud.png", "Clear": "images/clear.png",
                       "Snow": "images/snow.png"}
        images_data = [images_dict[item] for item in sky_data]
        st.image(images_data, width=115)

