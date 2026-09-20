import streamlit as st
import pandas as pd
import requests



BACKEND_URL = "http://api:8000/decisions"


@st.cache_data(ttl=60)
def fetch_data(url, relevant_only=False):
    try:
        if relevant_only:
            url += "?relevant_only=true"

        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None


is_relevant_only = st.toggle("Show only relevant decisions", value=False)

data = fetch_data(BACKEND_URL, relevant_only=is_relevant_only)

if data is not None:
    if len(data) == 0:
        st.info("No decisions found.")
    else:
        df = pd.DataFrame(data)

        # 2. Apply the LinkColumn configuration
        st.dataframe(
            df,
            column_config={
                "link": st.column_config.LinkColumn(
                    "Website Link",                 # Changes the column header 
                    help="Klikkaa tästä avataksesi sivu",  # Adds a hover tooltip
                    display_text="Avaa sivun"        # Hides the raw URL behind clickable text
                )
            },
            hide_index=True
        )