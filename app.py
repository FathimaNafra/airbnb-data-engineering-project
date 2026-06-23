import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Airbnb Market Dashboard",
    page_icon="🏠",
    layout="wide"
)

# ----------------------------------
# LOAD DATA
# ----------------------------------

@st.cache_data
def load_data():

    return pd.read_csv(
        "data/processed/listing_master.csv"
    )

master = load_data()

# ----------------------------------
# TITLE
# ----------------------------------

st.title(
    "🏠 Airbnb Market Intelligence Dashboard"
)

st.markdown(
    """
    Interactive dashboard for exploring
    Airbnb market dynamics.
    """
)

# ----------------------------------
# SIDEBAR
# ----------------------------------

st.sidebar.header(
    "Filters"
)

room_types = st.sidebar.multiselect(
    "Room Type",
    options=master["room_type"]
        .dropna()
        .unique(),
    default=master["room_type"]
        .dropna()
        .unique()
)

master = master[
    master["room_type"]
    .isin(room_types)
]

# ----------------------------------
# KPI SECTION
# ----------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Listings",
    f"{len(master):,}"
)

col2.metric(
    "Average Price",
    f"${master['price'].mean():.2f}"
)

col3.metric(
    "Average Rating",
    f"{master['review_scores_rating'].mean():.2f}"
)

if "occupancy_rate" in master.columns:

    col4.metric(
        "Average Occupancy",
        f"{master['occupancy_rate'].mean():.2f}%"
    )

else:

    col4.metric(
        "Average Occupancy",
        "N/A"
    )

# ----------------------------------
# PRICE DISTRIBUTION
# ----------------------------------

st.subheader(
    "Price Distribution"
)

fig = px.histogram(
    master,
    x="price",
    nbins=50
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------------
# ROOM TYPE ANALYSIS
# ----------------------------------

st.subheader(
    "Average Price by Room Type"
)

room_price = (
    master.groupby(
        "room_type"
    )["price"]
    .mean()
    .reset_index()
)

fig = px.bar(
    room_price,
    x="room_type",
    y="price"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------------
# TOP NEIGHBOURHOODS
# ----------------------------------

st.subheader(
    "Top 10 Neighbourhoods by Price"
)

neighbourhood_price = (
    master.groupby(
        "neighbourhood_cleansed"
    )["price"]
    .mean()
    .sort_values(
        ascending=False
    )
    .head(10)
    .reset_index()
)

fig = px.bar(
    neighbourhood_price,
    x="neighbourhood_cleansed",
    y="price"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------------
# MAP
# ----------------------------------

st.subheader(
    "Listing Locations"
)

map_df = master[
    [
        "latitude",
        "longitude",
        "price"
    ]
].dropna()

st.map(
    map_df
)

# ----------------------------------
# HOST ANALYSIS
# ----------------------------------

st.subheader(
    "Superhost Analysis"
)

if "host_is_superhost" in master.columns:

    superhost_stats = (
        master.groupby(
            "host_is_superhost"
        )["price"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        superhost_stats,
        x="host_is_superhost",
        y="price"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ----------------------------------
# REVIEW ANALYSIS
# ----------------------------------

st.subheader(
    "Review Count vs Price"
)

fig = px.scatter(
    master,
    x="number_of_reviews",
    y="price",
    opacity=0.5
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------------
# DATA TABLE
# ----------------------------------

st.subheader(
    "Listing Data"
)

st.dataframe(
    master.head(100)
)