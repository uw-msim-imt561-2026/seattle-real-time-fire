import streamlit as st

from src.data import load_data, load_geospatial_data, augment_data
from src.layout import header_metrics, body_layout_tabs
from src.filters import render_filters, apply_filters

def main() -> None:
    st.set_page_config(
      page_title="Seattle Fire 911 Calls in 2025",
      layout="wide",
    )

    st.title("Seattle Fire 911 Calls in 2025")
    st.caption("This dashboard provides insights into the fire-related 911 calls in Seattle for the year 2025.")


    # Load data
    df = load_data("./data/cleaned_augmented_real_time_fire_2025.csv")
    df = augment_data(df)
    
    # filter data
    selections = render_filters(df)
    df_f = apply_filters(df, selections)

    # HEADER KPIs
    header_metrics(df_f)

    st.divider()

    # BODY LAYOUT (Tabs)
    body_layout_tabs(df_f)

if __name__ == "__main__":
    main()
