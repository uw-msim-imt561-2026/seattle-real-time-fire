import pandas as pd
import streamlit as st

from src.charts import (
    plot_calls_map,
    plot_call_volume_by_hour,
    plot_incident_count_by_date,
    plot_incident_category_distribution
)

# Header KPI Section
def header_metrics(df: pd.DataFrame) -> None:
    """Rendering KPI metrics"""

    if df.empty:
        st.warning("No data available for selected filters.")
        return

    total_incidents = len(df)

    # Peak Hour
    peak_hour_series = df["hour"].value_counts()
    peak_hour = peak_hour_series.idxmax()
    peak_hour_count = peak_hour_series.max()

    # Most Common Category
    top_category_series = df["Incident_Category"].dropna().value_counts()
    top_category = top_category_series.idxmax()
    top_category_pct = round(
        (top_category_series.max() / total_incidents) * 100, 1
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Total Incidents", f"{total_incidents:,}")

    with c2:
        st.metric(
            "Peak Hour",
            f"{peak_hour}:00",
            help=f"{peak_hour_count:,} incidents during this hour"
        )

    with c3:
        st.metric(
            "Top Category",
            f"{top_category} ({top_category_pct}%)"
        )


# Body Layout (to add three default tabs)
def body_layout_tabs(df: pd.DataFrame) -> None:
    """Main dashboard body organized into tabs."""

    t1, t2, t3 = st.tabs([
        "Time Patterns",
        "Incident Categories",
        "Geographic View"
    ])

# Tab 1: Time Patterns
    with t1:
        st.subheader("Call Volume by Hour")
        plot_call_volume_by_hour(df)

        st.subheader("Daily Incident Trend")
        plot_incident_count_by_date(df)

        st.caption(
            "These charts show temporal distribution and daily trends "
            "for incidents within the selected filters."
        )
# Tab 2: Incident Distribution
    with t2:
        st.subheader("Incident Distribution by Category")
        plot_incident_category_distribution(df)

        st.caption(
            "This view highlights which incident categories "
            "drive overall call demand."
        )
# Tab 3:
    with t3:
        st.subheader("Map of Incidents")

        # Drop missing lat/lon for map only
        map_df = df.dropna(subset=["Latitude", "Longitude"])

        plot_calls_map(map_df)

        st.caption(
            "Geographic distribution of incidents based on available coordinates."
        )

        st.subheader("Filtered Data Preview")
        st.dataframe(df, use_container_width=True, height=400)

        st.download_button(
            label="Download filtered data as CSV",
            data=df.to_csv(index=False),
            file_name="filtered_fire_calls.csv",
            mime="text/csv"
        )