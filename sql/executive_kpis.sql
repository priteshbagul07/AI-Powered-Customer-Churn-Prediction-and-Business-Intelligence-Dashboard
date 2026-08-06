USE telecom_churn;

-- Total Customers
SELECT COUNT(*) AS total_customers
FROM telecom_customers;

-- Active Customers
SELECT COUNT(*) AS active_customers
FROM telecom_customers
WHERE customer_status = 'Stayed';

-- Churned Customers
SELECT COUNT(*) AS churned_customers
FROM telecom_customers
WHERE churn_label = 'Yes';

-- Top 10 Cities
SELECT
city,
COUNT(*) AS customers
FROM telecom_customers
GROUP BY city
ORDER BY customers DESC
LIMIT 10;

-- Churn Rate
SELECT
ROUND(
100.0 * SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END)
/ COUNT(*),
2
) AS churn_rate
FROM telecom_customers;

-- Total Revenue
SELECT
ROUND(SUM(total_revenue),2) AS total_revenue
FROM telecom_customers;

-- Average Revenue Per Customer
SELECT
ROUND(AVG(total_revenue),2) AS avg_revenue_per_customer
FROM telecom_customers;

-- Average Monthly Charge
SELECT
ROUND(AVG(monthly_charge),2) AS avg_monthly_charge
FROM telecom_customers;

-- Average Customer Tenure
SELECT
ROUND(AVG(tenure_in_months),2) AS avg_customer_tenure
FROM telecom_customers;

-- Average Satisfaction Score
SELECT
ROUND(AVG(satisfaction_score),2) AS avg_satisfaction_score
FROM telecom_customers;



