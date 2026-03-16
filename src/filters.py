import pandas as pd
import streamlit as st
from streamlit_dynamic_filters import DynamicFilters


def render_filters(df: pd.DataFrame) -> dict:
    """Render filters for the dashboard."""
    st.sidebar.header("Filters")


    # Filter by Incident Category levels
    dynamic_filters = DynamicFilters(df, filters=["Incident_Category", "Type"])
    dynamic_filters.display_filters(location="sidebar")

    # Filter by date range
    min_date = df["Datetime"].min()
    max_date = df["Datetime"].max()
    date_range = st.sidebar.date_input("Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)

    # Filter by time range
    col1, col2 = st.sidebar.columns(2)
    start_time = col1.time_input( "Start time", value=pd.to_datetime("00:00").time() )
    end_time = col2.time_input("End time", value=pd.to_datetime("23:59").time())
        
    # Filter by Address / Neighborhood / Location
    # TODO - Augment with neighborhood names or geofences


    selected_filters ={
    "dynamic_category": dynamic_filters,
    "date_range": date_range,
    "max_date": max_date,
    "time_range": [start_time, end_time]
    }
    return selected_filters

def apply_filters(df: pd.DataFrame, selections: dict) -> pd.DataFrame:
    """Apply filters to the dataframe."""
  
    
    # Apply dynamic category filters
    dynamic_category = selections["dynamic_category"]
    out = dynamic_category.filter_df()

    # Apply date range filter
    date_range = selections["date_range"]
    lo_date = date_range[0]
    hi_date = date_range[1] if len(date_range) > 1 else selections["max_date"].date()
    out = out[(out["Datetime"].dt.date >= lo_date) & (out["Datetime"].dt.date <= hi_date)]

    # Apply time range filter
    time_range = selections["time_range"]
    lo_time = time_range[0]
    hi_time = time_range[1] if len(time_range) > 1 else pd.to_datetime("23:59").time()
    out = out[(out["Datetime"].dt.time >= lo_time) & (out["Datetime"].dt.time <= hi_time)]

    #apply address / neighborhood / location filters - TODO

    return out