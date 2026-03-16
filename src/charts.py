import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import plotly.figure_factory as ff

def plot_calls_map(df: pd.DataFrame) -> None:
    """Plot a map of fire calls."""
    
    fig = ff.create_hexbin_map(
        df,
        lat="Latitude",
        lon="Longitude",
        nx_hexagon=50,
        opacity=0.6,
        labels={"color": "Number of Incidents"},
        title="Geographic Density of Fire Calls",
        color_continuous_midpoint=(len(df)*0.005),  # Adjust midpoint based on data size
        color_continuous_scale="balance",
        map_style="dark",
        template="plotly_dark",
        height=700,
        min_count=1  # Only show hexagons with at least 1 incident
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
        title="Distribution of 911 Fire Incidents by Hour",
        labels={
            "hour": "Hour of Day",
            "call_count": "Number of Incidents"
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
    
    if len(df["Incident_Category"].unique()) == 1:
        category = "Type"
    else: 
        category = "Incident_Category"

    # Remove missing categories
    df = df.dropna(subset=[category])

    # Count incidents by category
    category_counts = (
        df[category]
        .value_counts()
        .reset_index()
    )

    category_counts.columns = [category, "incident_count"]

    fig = px.bar(
        category_counts,
        x="incident_count",
        y=category,
        orientation="h",
        title="Incident Distribution by Category",
        labels={
            "incident_count": "Number of Incidents",
            category: "Incident Category"
        }
    )

    # Sort largest at top
    fig.update_layout(
        yaxis={"categoryorder": "total ascending"}
    )

    st.plotly_chart(fig, use_container_width=True)