# listing_master

Source:
- listings.csv
- calendar.csv
- reviews.csv

Transformations:
- Data Cleaning
- Missing Value Imputation
- Review Aggregation
- Revenue Estimation
- Occupancy Calculation
- Feature Engineering

Output:
- listing_master.csv


# fact_listings

Source:
- listing_master.csv

Transformation:
- Star Schema Modeling

Output:
- fact_listings