
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# -------------------------------
# PAGE CONFIGURATION
# -------------------------------

st.set_page_config(
    page_title="Netflix Analytics",
    page_icon="🎬",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "output" / "netflix_cleaned.csv"

# -------------------------------
# CUSTOM CSS
# -------------------------------

st.markdown("""
<style>
.stApp {
    background-color: #141414;
    color: white;
}

h1, h2, h3 {
    color: #E50914;
}

[data-testid="stMetric"] {
    background-color: #240303;
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #550000;
}

[data-testid="stMetricValue"] {
    color: #E50914;
}

section[data-testid="stSidebar"] {
    background-color: #1c1c1c;
}
</style>
""", unsafe_allow_html=True)


# -------------------------------
# LOAD CLEANED DATA
# -------------------------------

@st.cache_data
def load_data():
    if not DATA_PATH.exists():
        return None

    data = pd.read_csv(DATA_PATH)
    return data


df = load_data()

st.title("🎬 NETFLIX DATA ANALYTICS")
st.caption("Explore Netflix Movies and TV Shows")

if df is None:
    st.error(
        "Cleaned dataset not found. "
        "Run the Jupyter Notebook first."
    )
    st.stop()


# -------------------------------
# SIDEBAR FILTERS
# -------------------------------

st.sidebar.title("Dashboard Filters")

types = sorted(df["type"].dropna().unique())

selected_types = st.sidebar.multiselect(
    "Select Content Type",
    types,
    default=types
)

year_values = pd.to_numeric(
    df["release_year"],
    errors="coerce"
).dropna()

min_year = int(year_values.min())
max_year = int(year_values.max())

selected_years = st.sidebar.slider(
    "Release Year Range",
    min_year,
    max_year,
    (min_year, max_year)
)

# Apply filters
filtered = df[
    (df["type"].isin(selected_types)) &
    (df["release_year"].between(
        selected_years[0],
        selected_years[1]
    ))
].copy()


# -------------------------------
# KPI CARDS
# -------------------------------

total_shows = len(filtered)

total_directors = filtered.loc[
    filtered["director"] != "Unknown",
    "director"
].nunique()

total_countries = (
    filtered.loc[
        filtered["country"] != "Unknown",
        "country"
    ]
    .str.split(", ")
    .explode()
    .nunique()
)

total_genres = (
    filtered["listed_in"]
    .dropna()
    .str.split(", ")
    .explode()
    .nunique()
)

total_ratings = filtered.loc[
    filtered["rating"] != "Not Rated",
    "rating"
].nunique()

st.markdown("### Netflix Overview")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Total Shows", f"{total_shows:,}")
c2.metric("Directors", f"{total_directors:,}")
c3.metric("Countries", f"{total_countries:,}")
c4.metric("Genres", f"{total_genres:,}")
c5.metric("Ratings", f"{total_ratings:,}")


# -------------------------------
# MOVIE VS TV SHOW
# -------------------------------

st.markdown("---")

left, right = st.columns(2)

with left:

    type_data = (
        filtered["type"]
        .value_counts()
        .reset_index()
    )

    type_data.columns = ["Type", "Count"]

    fig = px.pie(
        type_data,
        names="Type",
        values="Count",
        title="Movies vs TV Shows",
        hole=0.35,
        color_discrete_sequence=[
            "#E50914",
            "#850000"
        ]
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#180000",
        font_color="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# -------------------------------
# TOP GENRES
# -------------------------------

with right:

    genre_data = (
        filtered["listed_in"]
        .dropna()
        .str.split(", ")
        .explode()
        .value_counts()
        .head(10)
        .reset_index()
    )

    genre_data.columns = ["Genre", "Count"]

    fig = px.bar(
        genre_data,
        x="Count",
        y="Genre",
        orientation="h",
        title="Top 10 Genres",
        color_discrete_sequence=["#E50914"]
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#180000",
        yaxis={"categoryorder": "total ascending"}
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# -------------------------------
# RELEASE YEAR ANALYSIS
# -------------------------------

st.markdown("---")

year_data = (
    filtered.groupby(["release_year", "type"])
    .size()
    .reset_index(name="Count")
)

fig = px.line(
    year_data,
    x="release_year",
    y="Count",
    color="type",
    title="Content Distribution by Release Year",
    markers=True,
    color_discrete_sequence=[
        "#E50914",
        "#FF7777"
    ]
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="#180000"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# -------------------------------
# RATINGS ANALYSIS
# -------------------------------

left, right = st.columns(2)

with left:

    rating_data = (
        filtered["rating"]
        .value_counts()
        .reset_index()
    )

    rating_data.columns = ["Rating", "Count"]

    fig = px.bar(
        rating_data,
        x="Rating",
        y="Count",
        title="Ratings Distribution",
        color_discrete_sequence=["#E50914"]
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#180000"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# -------------------------------
# COUNTRY ANALYSIS
# -------------------------------

with right:

    country_data = (
        filtered.loc[
            filtered["country"] != "Unknown",
            "country"
        ]
        .dropna()
        .str.split(", ")
        .explode()
        .value_counts()
        .head(10)
        .reset_index()
    )

    country_data.columns = ["Country", "Count"]

    fig = px.bar(
        country_data,
        x="Count",
        y="Country",
        orientation="h",
        title="Top 10 Content Producing Countries",
        color_discrete_sequence=["#E50914"]
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#180000",
        yaxis={"categoryorder": "total ascending"}
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# -------------------------------
# FOOTER
# -------------------------------

st.markdown("---")

st.caption(
    "Netflix Data Analytics Project | "
    "Built using Python, Pandas, Streamlit and Plotly"
)
