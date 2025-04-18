import streamlit as st
import folium
from streamlit_folium import folium_static
import random

# Function to simulate fetching real-time data
def fetch_real_time_data():
    # Simulate some data
    return {
        "transaction_id": random.randint(1000, 9999),
        "amount": round(random.uniform(10, 500), 2),
        "location": {
            "lat": random.uniform(37.7, 37.8),  # Random latitude
            "lon": random.uniform(-122.5, -122.4)  # Random longitude
        }
    }

# Function to create a map
def create_map(location):
    # Create a map centered at the transaction location
    m = folium.Map(location=[location['lat'], location['lon']], zoom_start=12)
    folium.Marker([location['lat'], location['lon']], popup=f"Transaction ID: {transaction['transaction_id']}").add_to(m)
    return m

# Main app
st.title("Credit Card Fraud Detection Dashboard")

# Real-time data section
st.header("Real-Time Fraud Alerts")

# Create a button to fetch new data
if st.button("Fetch New Transaction"):
    # Fetch real-time data
    transaction = fetch_real_time_data()
    
    # Display transaction details
    st.write(f"Transaction ID: {transaction['transaction_id']}")
    st.write(f"Amount: ${transaction['amount']}")
    
    # Create and display the map
    map = create_map(transaction['location'])
    folium_static(map)