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
    """Plotting a distribution of 911 fire calls by hour of day. Assumes df is filtered upstream"""
    if df.empty:
        st.warning("No data available for selected filters.")
        return
    # Count calls by hour
    hour_counts = (
        df["hour"]
        .value_counts()
        .sort_index()
        .reset_index()
    )
    hour_counts.columns = ["hour", "call_count"]

    # Adding dynamic title based on incident categories present
    categories = df["Incident_Category"].unique()
    if len(categories) == 1:
        title = f"Call Volume by Hour — {categories[0]}"
    else:
        title = "Call Volume by Hour — All Incident Categories"

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
    fig.update_layout(xaxis=dict(dtick=1))
    st.plotly_chart(fig, use_container_width=True)

def plot_incident_count_by_date(df: pd.DataFrame) -> None:
    """Plot daily incident count over time. Assuming df is already filtered (by category, date, etc)."""
    if df.empty:
        st.warning("No data available for selected filters.")
        return
    df = df.copy()

    # Aggregate by date
    daily_counts = (
        df
        .groupby(df["Datetime"].dt.date)
        .size()
        .reset_index(name="incident_count")
    )

    daily_counts.columns = ["date", "incident_count"]
    fig = px.line(
        daily_counts,
        x="date",
        y="incident_count",
        title="Daily Incident Count",
        labels={
            "date": "Date",
            "incident_count": "Number of Incidents"
        }
    )

    fig.update_layout(hovermode="x unified")
    st.plotly_chart(fig, use_container_width=True)

def plot_incident_category_distribution(df: pd.DataFrame) -> None:
    """Plot distribution of incidents by Incident_Category. Again, assumes df is already filtered upstream."""
    if df.empty:
        st.warning("No data available for selected filters.")
        return

    # Remove missing categories
    df = df.dropna(subset=["Incident_Category"])

    # Count incidents by category
    category_counts = (
        df["Incident_Category"]
        .value_counts()
        .reset_index()
    )

    category_counts.columns = ["Incident_Category", "incident_count"]

    fig = px.bar(
        category_counts,
        x="incident_count",
        y="Incident_Category",
        orientation="h",
        title="Incident Distribution by Category",
        labels={
            "incident_count": "Number of Incidents",
            "Incident_Category": "Incident Category"
        }
    )

    # Sort largest at top
    fig.update_layout(
        yaxis={"categoryorder": "total ascending"}
    )

    st.plotly_chart(fig, use_container_width=True)