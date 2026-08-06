USE telecom_churn;

-- Average customer age
SELECT
ROUND(AVG(age),2) AS average_age
FROM telecom_customers;

-- Youngest and oldest customer
SELECT
MIN(age) AS youngest_customer,
MAX(age) AS oldest_customer
FROM telecom_customers;

-- Creating Age Groups
SELECT
CASE
WHEN age < 30 THEN 'Under 30'
WHEN age BETWEEN 30 AND 45 THEN '30-45'
WHEN age BETWEEN 46 AND 60 THEN '46-60'
ELSE 'Above 60'
END AS age_group,
COUNT(*) AS total_customers
FROM telecom_customers
GROUP BY age_group
ORDER BY age_group;

-- Churn by Age Group
SELECT
CASE
WHEN age <30 THEN 'Under 30'
WHEN age BETWEEN 30 AND 45 THEN '30-45'
WHEN age BETWEEN 46 AND 60 THEN '46-60'
ELSE 'Above 60'
END AS age_group,
COUNT(*) AS customers,
SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END) AS churned,
ROUND(
100*SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END)
/COUNT(*),2
) AS churn_rate
FROM telecom_customers
GROUP BY age_group;