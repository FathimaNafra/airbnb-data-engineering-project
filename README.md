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
airbnb-market-analysis/

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