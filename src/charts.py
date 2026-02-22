import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st


def plot_calls_map(df: pd.DataFrame) -> None:
    """Plot a map of fire calls."""
    fig = px.scatter_mapbox(
        df,
        lat="Latitude",
        lon="Longitude",
        color='Incident_Category',
        hover_name="Type",
        hover_data=["Incident_Category", "Address", "Datetime"],
        zoom=10,
        center={"lat": 47.6062, "lon": -122.3320},
        mapbox_style="open-street-map"
        )
    st.plotly_chart(fig, use_container_width=True)