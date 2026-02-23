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
        hover_name="Type",
        hover_data=["Incident_Category", "Address", "Datetime"],
        zoom=10,
        center={"lat": 47.6062, "lon": -122.3320},
        mapbox_style="open-street-map"
        )
    st.plotly_chart(fig, use_container_width=True)


def plot_call_volume_by_hour(df: pd.DataFrame) -> None:
    """Plotting a distribution of 911 fire calls by hour of day."""
    # Count calls by hour
    hour_counts = (
        df["hour"]
        .value_counts()
        .sort_index()
        .reset_index()
    )
    hour_counts.columns = ["hour", "call_count"]
    # Create Plotly bar chart
    fig = px.bar(
        hour_counts,
        x="hour",
        y="call_count",
        title="Distribution of 911 Fire Calls by Hour",
        labels={
            "hour": "Hour of Day",
            "call_count": "Number of Calls"
        }
    )
    st.plotly_chart(fig, use_container_width=True)