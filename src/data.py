import streamlit as st
import pandas as pd
import geopandas as gpd

@st.cache_data(show_spinner=False)
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    #parsing Datetime
    df["Datetime"] = pd.to_datetime(df["Datetime"], errors="coerce")
    #parsing in more detail for visualizations
    data["Datetime"] = pd.to_datetime(data["Datetime"], format="%Y %b %d %I:%M:%S %p")
    data["hour"] = data["Datetime"].dt.hour
    data["day_of_week"] = data["Datetime"].dt.day_name()
    data["month"] = data["Datetime"].dt.month
    return df

@st.cache_data(show_spinner=False)
def load_geospatial_data(path: str) -> gpd.GeoDataFrame:
    data = pd.read_csv(path)
    gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data['Longitude'], data['Latitude']))
    gdf.set_crs(epsg=4326, inplace=True) 
    return gdf