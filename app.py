import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Airbnb Intelligence",
    page_icon="🏠",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
    padding-bottom:0rem;
    max-width:100%;
}

[data-testid="stSidebar"]{
    background:#111827;
}

.main{
    background:#0b1020;
    color:white;
}

h1,h2,h3{
    color:white;
}

.metric-card{
    background:linear-gradient(
    135deg,
    #8b5cf6,
    #06b6d4
    );
    padding:18px;
    border-radius:18px;
    text-align:center;
    color:white;
    box-shadow:0 4px 20px rgba(0,0,0,0.4);
}

.metric-value{
    font-size:32px;
    font-weight:bold;
}

.metric-label{
    font-size:14px;
}

.chart-card{
    background:#111827;
    padding:12px;
    border-radius:18px;
    box-shadow:0 4px 20px rgba(0,0,0,0.4);
}

</style>
""", unsafe_allow_html=True)

# =====================================
# LOAD DATA
# =====================================

@st.cache_data
def load_data():
    return pd.read_csv(
        "data/processed/listing_master.csv"
    )

df = load_data()

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("Filters")

room_types = st.sidebar.multiselect(
    "Room Type",
    df["room_type"].dropna().unique(),
    default=df["room_type"].dropna().unique()
)

price_range = st.sidebar.slider(
    "Price Range",
    int(df["price"].min()),
    int(df["price"].quantile(0.99)),
    (
        int(df["price"].min()),
        int(df["price"].quantile(0.99))
    )
)

df = df[
    (df["room_type"].isin(room_types))
    &
    (df["price"] >= price_range[0])
    &
    (df["price"] <= price_range[1])
]

# =====================================
# HEADER
# =====================================

st.markdown(
"""
# 🏠 Airbnb Market Intelligence Dashboard
Real-time analytics for Airbnb listings, pricing, reviews and host performance.
"""
)

# =====================================
# KPI CARDS
# =====================================

k1,k2,k3,k4 = st.columns(4)

with k1:
    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-label">Listings</div>
    <div class="metric-value">{len(df):,}</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-label">Avg Price</div>
    <div class="metric-value">${df['price'].mean():.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-label">Avg Rating</div>
    <div class="metric-value">{df['review_scores_rating'].mean():.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-label">Reviews</div>
    <div class="metric-value">{df['number_of_reviews'].sum():,}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================
# ROW 1
# =====================================

left,right = st.columns([2,1])

with left:

    fig1 = px.histogram(
        df,
        x="price",
        nbins=40,
        template="plotly_dark"
    )

    fig1.update_layout(
        height=250,
        margin=dict(l=10,r=10,t=30,b=10)
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with right:

    room_price = (
        df.groupby("room_type")
        ["price"]
        .mean()
        .reset_index()
    )

    fig2 = px.bar(
        room_price,
        x="room_type",
        y="price",
        template="plotly_dark"
    )

    fig2.update_layout(
        height=250,
        margin=dict(l=10,r=10,t=30,b=10)
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# =====================================
# ROW 2
# =====================================

c1,c2,c3 = st.columns(3)

with c1:

    top_hosts = (
        df.groupby("host_id")
        .size()
        .sort_values(ascending=False)
        .head(10)
        .reset_index(name="listings")
    )

    fig3 = px.pie(
        top_hosts,
        values="listings",
        names="host_id",
        hole=0.6
    )

    fig3.update_layout(
        height=250,
        margin=dict(l=10,r=10,t=20,b=10)
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

with c2:

    fig4 = px.scatter(
        df.sample(
            min(
                2000,
                len(df)
            )
        ),
        x="number_of_reviews",
        y="price",
        template="plotly_dark"
    )

    fig4.update_layout(
        height=250,
        margin=dict(l=10,r=10,t=20,b=10)
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

with c3:

    neighbourhood = (
        df.groupby(
            "neighbourhood_cleansed"
        )["price"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig5 = px.bar(
        neighbourhood,
        x="price",
        y="neighbourhood_cleansed",
        orientation="h",
        template="plotly_dark"
    )

    fig5.update_layout(
        height=250,
        margin=dict(l=10,r=10,t=20,b=10)
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

# =====================================
# ROW 3
# =====================================

m1,m2 = st.columns([2,1])

with m1:

    map_df = df[
        ["latitude","longitude"]
    ].dropna()

    st.map(
        map_df,
        height=280
    )

with m2:

    if "host_is_superhost" in df.columns:

        superhost = (
            df.groupby(
                "host_is_superhost"
            )["price"]
            .mean()
            .reset_index()
        )

        fig6 = px.bar(
            superhost,
            x="host_is_superhost",
            y="price",
            template="plotly_dark"
        )

        fig6.update_layout(
            height=280,
            margin=dict(l=10,r=10,t=20,b=10)
        )

        st.plotly_chart(
            fig6,
            use_container_width=True
        )