USE telecom_churn;

-- Gender Analysis

-- Counting total male and female customers
SELECT
    gender,
    COUNT(*) AS total_customers
FROM telecom_customers
GROUP BY gender;

-- churn rate by gender
SELECT
    gender,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        100 * SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS churn_rate
FROM telecom_customers
GROUP BY gender;