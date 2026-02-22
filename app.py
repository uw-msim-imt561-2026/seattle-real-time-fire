import streamlit as st
from src.data import load_data, load_geospatial_data
from src.charts import plot_calls_map


def main() -> None:
    st.set_page_config(
      page_title="Seattle Fire 911 Calls in 2025",
      layout="wide",
    )

    st.title("Seattle Fire 911 Calls in 2025")
    st.caption("This dashboard provides insights into the fire-related 911 calls in Seattle for the year 2025.")


    # Load data
    df = load_data("./data/cleaned_augmented_real_time_fire_2025.csv")

    #display Map: 

    col1, col2 = st.columns(2)
    with col1:
      st.subheader("Map of Fire Calls")
      plot_calls_map(df)
    with col2:
      st.subheader("911 Call Details")
      st.dataframe(df[["Datetime", "Type", "Incident_Category", "Address"]], height=500)


if __name__ == "__main__":
    main()
