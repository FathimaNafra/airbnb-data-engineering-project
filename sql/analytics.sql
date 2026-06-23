-- Query 1: Top Revenue Listings

SELECT
    id,
    estimated_revenue
FROM fact_listings
ORDER BY estimated_revenue DESC
LIMIT 10;

-- Query 2: Average Revenue by Neighbourhood

SELECT
    neighbourhood_cleansed,
    AVG(estimated_revenue) AS avg_revenue
FROM fact_listings
GROUP BY neighbourhood_cleansed
ORDER BY avg_revenue DESC;

-- Query 3: Best Occupancy Areas

SELECT
    neighbourhood_cleansed,
    AVG(occupancy_rate) AS avg_occupancy
FROM fact_listings
GROUP BY neighbourhood_cleansed
ORDER BY avg_occupancy DESC;


-- Query 4: Revenue by Room Type

SELECT
    d.room_type,
    AVG(f.estimated_revenue) AS avg_revenue
FROM fact_listings f
JOIN dim_listing d
ON f.id = d.id
GROUP BY d.room_type;

