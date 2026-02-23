import streamlit as st
import pandas as pd
import geopandas as gpd


@st.cache_data(show_spinner=False)
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    #parsing Datetime
    df["Datetime"] = pd.to_datetime(df["Datetime"], errors="coerce")
    
    #parsing in more detail for visualizations
    df["Formatted Datetime"] = pd.to_datetime(df["Datetime"], format="%Y %b %d %I:%M:%S %p")
    df["hour"] = df["Datetime"].dt.hour
    df["day_of_week"] = df["Datetime"].dt.day_name()
    df["month"] = df["Datetime"].dt.month
    return df

def augment_data(df: pd.DataFrame) -> pd.DataFrame:
    """Load and augment data."""

    type_categories = {
    "Medical": [
        "Aid Response",
        "Aid Response Yellow",
        "Major Aid Response",
        "Single Medic Unit",
        "Medic Response",
        "Medic Response Freeway",
        "BC Medic Response",
        "BC Medic Response- 6 per rule",
        "BC Medic Response- 7 per Rule",
        "Medic Response- 6 per Rule",
        "Medic Response- 7 per Rule",
        "Medic Response- Overdose",
        "Aid Resp Infectious",
        "Triaged Incident",
        "NurselineAMR",
        "Trans to AMR",
        "Poison Control",
        "Scenes Of Violence",
        "Scenes Of Violence Aid",
        "Scenes Of Violence 7",
        "Scenes Of Violence 14",
        "Crisis Center" # Validate

    ],
    "Vehicle Incidents": [
        "MVI - Motor Vehicle Incident",
        "MVI Freeway",
        "MVI Freeway Medic",
        "MVI Freeway Automatic",
        "MVI Freeway Fast Back Up",
        "Tunnel MVI",
        "Train Derailment wFireHzmt",
        "Primary Incident",
        "Link - Link Control Center"
    ],
    "Fires": [
        "Fire in Building",
        "Fire In A Highrise",
        "Garage Fire",
        "Shed Fire",
        "Chimney Fire",
        "Major Chimney Fire"
        "Car Fire",
        "Car Fire Freeway",
        "Car Fire RV Fire",
        "Car Fire WExp.",
        "RV Fire",
        "Brush Fire",
        "Brush Fire Freeway",
        "Brush Fire WExp.",
        "Brush Fire Major",
        "Brush Fire Encampment Fire",
        "Bark Fire",
        "Dumpster Fire",
        "Dumpster Fire WExp.",
        "Rubbish Fire",
        "Bark Fire Freeway",
        "Encampment Fire",
        "Furnace Problem",
        "Fire On Shore",
        "Transformer Fire",
        "Tranformer Fire"
        "Food On The Stove",
        "Vault Advised"

    ],
    "Fire Alarms": [
        "Auto Fire Alarm",
        "Automatic Fire Alarm",
        "Automatic Fire Alarm Resd",
        "Auto Alarm 1 1 1",
        "AFA4 - Auto Alarm 2 1 1",
        "Alarm Bell",
        "Automatic Fire Alarm False",
        "FIREWATCH",
        "Investigate Out Of Service"
    ],

    "Rescue": [
        "Rescue Elevator",
        "Code Yellow Rescue",
        "Rescue Extrication",
        "Rescue Heavy Major",
        "Rescue Rope",
        "Rescue Confined Space",
        "Rescue Trench",
        "Rescue Standby",
        "Rescue Rope Standby",
        "Rescue Confined Space Standby",
        "Rescue Tunnel Standby",
        "Rescue Tunnel",
        "Rescue Heavy",
        "Rescue Trench 4RED - 2 1 1"
    ],
    "Marine Incidents": [
        "Water Rescue Response",
        "Water Rescue Standby",
        "Water Job",
        "Water Job Major",
        "Marine Fire On Shore",
        "Marine Fire On Water",
        "Vessel Sinking On Shore",
        "Vessel Sinking On Water",
        "Marine Service Response",
        "Mutual Aid- Marine"
    ],
    "HazMat and Gas": [
        "Hazardous Mat- Spill-Leak",
        "HazMat Reduced",
        "HazMat Alarm",
        "Mutual Aid- Hazmat",
        "HAZADV - Hazmat Advised",
        "Fuel Spill",
        "Spill- Non-Hazmat",
        "Natural Gas Leak",
    ],
    "Utilities": [
        "Electrical Problem",
        "Energy Response",
        "Energy Advised",
        "Wires Down"
    ],
    "Alarm levels, codes, and chief responses": [
        "0 - MVI Medic",
        "0 - Mutual Aid- Medic",
        "1RED 1 Unit",
        "1YELLOW 1 Unit",
        "2RED - 1 1",
        "3RED - 1 1 1",
        "4RED - 2 1 1",
        "Engine Code Red",
        "Engine Code Yellow",
        "Ladder Code Red",
        "Ladder Code Yellow",
        "BC Aid Response",
        "BC Aid Response Yellow",
        "RMC Chief"
    ],
    "Low Acuity": [
        "Low Acuity Response",
        "Low Acuity Referral"

    ],
    "Minor service": [
        "EVENT - Special Event",
        "Rescue Lock InOut",
        "Hang-Up- Aid",
        "Hang-Up- Fire",
        "Help the Fire Fighter",
        "Poss Patient",
        "Food On The Stove Out",
        "Unk Odor"
    ],

    "Mutual aid": [
        "Mutual Aid- Engine",
        "Mutual Aid- Ladder",
        "Mutual Aid- Medic",
        "Mutual Aid- Aid",
        "Mutual Aid- Hazmat",
        "Mutual Aid- Marine",
        "Mutual Aid- Task Force",
        "Mutual Aid- Strike Eng.",
        "Law Enforcement Standby"
    ],
    "Testing":["TEST - MIS TEST"]
}
    df["Incident_Category"] = df["Type"].map(lambda x: next((cat for cat, types in type_categories.items() if x in types), "Other"))

    #remove rows on Jan 1 2026
    df = df[df["Datetime"] < "2026-01-01"]

    # TODO - Augment with neighborhood names or geofences

    return df

@st.cache_data(show_spinner=False)
def load_geospatial_data(path: str) -> gpd.GeoDataFrame:
    data = pd.read_csv(path)
    gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data['Longitude'], data['Latitude']))
    gdf.set_crs(epsg=4326, inplace=True) 
    return gdf