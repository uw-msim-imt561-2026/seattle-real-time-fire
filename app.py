import streamlit as st
from src.data import load_data, load_geospatial_data
from src.layout import header_metrics, body_layout_tabs


def main() -> None:
    st.set_page_config(
      page_title="Seattle Fire 911 Calls in 2025",
      layout="wide",
    )

    st.title("Seattle Fire 911 Calls in 2025")
    st.caption("This dashboard provides insights into the fire-related 911 calls in Seattle for the year 2025.")


    # Load data
    df = load_data("./data/cleaned_augmented_real_time_fire_2025.csv")

    # HEADER KPIs
    header_metrics(df)

    st.divider()

    # BODY LAYOUT (Tabs)
    body_layout_tabs(df)

if __name__ == "__main__":
    main()
