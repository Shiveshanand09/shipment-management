import streamlit as st
import json

# Load extracted information from the JSON file
with open('extracted_data.json', 'r') as file:
    extracted_info = json.load(file)

# Streamlit app
st.title('Delivery Instructions Dashboard')

st.header('Pickup Details')
st.write(f"**Pick-up Date:** {extracted_info.get('pickup_date', 'Not found')}")
st.write(f"**Pick-up Address:** {extracted_info.get('pickup_address', 'Not found')}")
st.write(f"**Shipment Type:** {extracted_info.get('shipment_type', 'Not found')}")
st.write(f"**Commodity:** {extracted_info.get('commodity', 'Not found')}")

st.header('Contact Information')
st.write(f"**Contact Person:** {extracted_info.get('contact_person', 'Not found')}")
st.write(f"**Contact Number:** {extracted_info.get('contact_number', 'Not found')}")

st.header('Delivery Details')
st.write(f"**Delivery Address:** {extracted_info.get('delivery_address', 'Not found')}")
st.write(f"**Note:** {extracted_info.get('note', 'Not found')}")
