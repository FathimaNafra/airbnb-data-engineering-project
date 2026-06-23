# Airbnb Market Intelligence Platform

## Project Overview

This project was developed as part of the Expernetic Data Engineering Internship Assignment.

The objective was to transform raw Airbnb data into a complete analytics platform capable of supporting business intelligence, statistical analysis, machine learning, and interactive market exploration.

The solution covers the full data lifecycle:

- Data Ingestion
- Data Profiling
- Data Cleaning & Standardization
- Data Enrichment
- Data Warehouse Modeling
- Automated Pipeline Design
- Exploratory Data Analysis
- Statistical Analysis
- Machine Learning
- Interactive Dashboard

Dataset Source:

Inside Airbnb

https://insideairbnb.com/

---

# Business Problem

Stakeholders such as product managers, revenue strategists, and operations teams require reliable market intelligence from Airbnb data.

This project provides:

- Pricing insights
- Host performance analysis
- Demand indicators
- Neighbourhood comparisons
- Revenue estimation
- Predictive pricing models
- Interactive business dashboards

---

# Project Architecture

Raw Data
(listings, calendar, reviews)

↓

Data Ingestion

↓

Data Cleaning & Validation

↓

Data Enrichment & Feature Engineering

↓

Master Dataset

(listing_master.csv)

↓

DuckDB Warehouse

↓

EDA + Statistical Analysis

↓

Machine Learning Models

↓

Streamlit Dashboard

---

# Repository Structure
airbnb-data-engineering-project/

├── data/

│ ├── raw/London/

│ │ ├── listings.csv

│ │ ├── calendar.csv

│ │ ├── reviews.csv

│ │ └── neighbourhoods.csv

│

│ ├── processed/

│ │ ├── listings_clean.csv

│ │ ├── reviews_clean.csv

│ │ ├── calendar_clean.csv

│ │ ├── occupancy.csv

│ │ └── listing_master.csv

│

│ └── metadata/

│ ├── metadata_log.csv

│ └── last_run.txt

│

├── database/

│ └── airbnb_warehouse.duckdb

│

├── logs/

│ └── pipeline.log

│

├── notebooks/

│ ├── Data_engineering.ipynb

│ ├── Dataset_exploration.ipynb

│ ├── eda.ipynb

│ ├── statistical.ipynb

│ └── machine_learning.ipynb

│

├── reports/

│ ├── summary_statistics.csv

│ ├── listings_schema.csv

│ ├── calendar_schema.csv

│ ├── reviews_schema.csv

│ ├── neighbourhoods_schema.csv

│ ├── price_distribution.png

│ ├── listing_density_map.png

│ └── lineage.md

│

├── sql/

│ └── analytics.sql

│

├── src/

│ ├── config.py

│ ├── ingest.py

│ ├── cleaning.py

│ ├── enrichment.py

│ ├── validation.py

│ ├── profiling.py

│ ├── metadata.py

│ ├── modeling.py

│ └── pipeline.py

│

├── app.py

├── requirements.txt

├── .gitignore

└── README.md


---

---

# Dataset Description

## listings.csv

Contains listing information including:

- Price
- Room Type
- Property Type
- Host Information
- Availability
- Review Scores

## calendar.csv

Contains daily availability and pricing information for each listing.

## reviews.csv

Contains review history and review dates.

## neighbourhoods.csv

Contains neighbourhood reference information.

---

# Data Engineering Implementation

## 1. Data Ingestion

Implemented reusable ingestion functions for:

- Listings
- Calendar
- Reviews

Features:

- Repeatable loading process
- Configurable city selection

---

## 2. Data Profiling

Generated:

- Row counts
- Null percentages
- Cardinality statistics
- Schema documentation

Outputs:

- listings_schema.csv
- calendar_schema.csv
- reviews_schema.csv
- neighbourhoods_schema.csv

---

## 3. Data Cleaning

Implemented:

- Price standardization
- Date parsing
- Text normalization
- Missing value treatment
- Validation checks

---

## 4. Data Enrichment

Created:

### Review Aggregates

- Total Reviews
- First Review Date
- Last Review Date

### Occupancy Metrics

- Occupancy Rate
- Estimated Revenue

### Neighbourhood Metrics

- Median Price
- Listing Density
- Average Rating

### Derived Features

- Host Tenure
- Review Frequency
- Price Per Bedroom

Output:

listing_master.csv

---

## 5. Data Warehouse Modeling

Implemented a Star Schema using DuckDB.

### Fact Table

fact_listings

Measures:

- Price
- Revenue
- Occupancy
- Review Frequency

### Dimension Tables

dim_host

dim_listing

dim_neighbourhood

---

## 6. Automated Pipeline

Features:

- Configuration-driven execution
- Logging
- Error handling
- Retry mechanism
- Incremental processing
- Metadata tracking

Metadata files:

- metadata_log.csv
- last_run.txt

---

# Exploratory Data Analysis

Performed:

### Summary Statistics

- Price Distribution
- Availability Distribution
- Review Distribution

### Geographic Analysis

- Listing Density Maps
- Neighbourhood Price Analysis

### Temporal Analysis

- Seasonality
- Review Trends
- Host Tenure Trends

### Host Analysis

- Portfolio Segmentation
- Superhost Analysis

### Demand Analysis

- Review Frequency
- Review Score Drivers

---

# Statistical Analysis

Hypothesis Testing:

### H1

Entire homes are priced higher than private rooms.

### H2

Superhosts receive higher ratings.

### H3

Listings with >10 reviews differ in pricing.

### H4

Neighbourhood prices differ significantly.

### H5

Weekend and weekday pricing differ significantly.

Additional Analysis:

- Confidence Intervals
- Effect Sizes
- Correlation Analysis
- OLS Regression
- VIF Analysis

---

# Machine Learning

## Price Prediction

Target Variable:

Price

Models:

- Linear Regression
- Random Forest
- Gradient Boosting

Evaluation Metrics:

- MAE
- RMSE
- MAPE

Explainability:

- SHAP Feature Importance

---

## Listing Segmentation

Clustering:

- K-Means

Evaluation:

- Silhouette Score

Outputs:

- Listing Segments
- Business Profiles

---

# Interactive Dashboard

Technology:

Streamlit

Features:

- KPI Metrics
- Price Analysis
- Host Analysis
- Geographic Insights
- Statistical Findings
- Machine Learning Results

Run:

```bash
streamlit run app.py
```

# Reproducibility Instructions

## 1. Clone Repository

```bash
git clone https://github.com/FathimaNafra/airbnb-data-engineering-project
cd airbnb-data-engineering-project
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Execute Data Pipeline

Run the automated data pipeline to perform ingestion, cleaning, enrichment, and metadata tracking.

```bash
python src/pipeline.py
```

## 5. Build Data Warehouse

Create the analytical warehouse and star schema in DuckDB.

```bash
python src/modeling.py
```

## 6. Run Interactive Dashboard

Launch the Streamlit dashboard.

```bash
streamlit run app.py
```

---

# Key Technologies

- Python
- Pandas
- NumPy
- DuckDB
- Scikit-Learn
- Statsmodels
- Matplotlib
- Seaborn
- Streamlit

---

# Assumptions

The following assumptions were made during implementation:

- Missing review score values were imputed using median values.
- Review frequency was used as a proxy indicator for booking demand.
- Occupancy was estimated using calendar availability information.
- Analysis was conducted using the London Airbnb dataset only.
- Historical booking information was inferred from available review and calendar data.

---


# Author

**Fathima Nafra**

BSc (Hons) Computer Science (Data Science)

Faculty of Computing and Technology

University of Kelaniya
