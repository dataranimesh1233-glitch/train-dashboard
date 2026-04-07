import streamlit as st
import pandas as pd

# API response (given)
api_response = {
    "train_name": "Rajdhani Express",
    "train_number": "12301",
    "route": [
        {"station": "New Delhi",      "arrival": "Source",      "departure": "07:05"},
        {"station": "Kanpur Central", "arrival": "10:10",       "departure": "10:15"},
        {"station": "Allahabad Jn",   "arrival": "12:00",       "departure": "12:10"},
        {"station": "Patna Jn",       "arrival": "16:30",       "departure": "16:40"},
        {"station": "Howrah Jn",      "arrival": "21:30",       "departure": "Destination"}
    ]
}

# ----------------------------
# Task 1 — Parse Data
# ----------------------------
data = []

for stop in api_response["route"]:
    data.append({
        "Station": stop["station"],
        "Arrival": stop["arrival"],
        "Departure": stop["departure"]
    })

df = pd.DataFrame(data)

# ----------------------------
# Task 2 — Streamlit UI
# ----------------------------

# Title
st.markdown(f"## 🚆 {api_response['train_name']} ({api_response['train_number']})")

# Table
st.dataframe(df)

# Station selector
station_list = df["Station"].tolist()
selected_station = st.selectbox("Select a station:", station_list)

# Show details
station_data = df[df["Station"] == selected_station].iloc[0]

st.text(f"Arrival Time: {station_data['Arrival']}")
st.text(f"Departure Time: {station_data['Departure']}")