USE telecom_churn;

-- Total Revenue
SELECT
ROUND(SUM(total_revenue),2) AS total_revenue
FROM telecom_customers;

-- Average Revenue per Customer
SELECT
ROUND(AVG(total_revenue),2) AS avg_revenue_per_customer
FROM telecom_customers;

-- Highest Revenue Customer
SELECT
customer_id,
total_revenue
FROM telecom_customers
ORDER BY total_revenue DESC
LIMIT 1;

-- Top 10 Highest Revenue Customers
SELECT
customer_id,
round(total_revenue,2)
FROM telecom_customers
ORDER BY total_revenue DESC
LIMIT 10;

-- Average Monthly Charge
SELECT
ROUND(AVG(monthly_charge),2) AS avg_monthly_charge
FROM telecom_customers;

-- Highest Monthly Charge
SELECT
MAX(monthly_charge) AS highest_monthly_charge
FROM telecom_customers;

-- Lowest Monthly Charge
SELECT
MIN(monthly_charge) AS lowest_monthly_charge
FROM telecom_customers;

-- Revenue by Contract Type
SELECT
contract,
ROUND(SUM(total_revenue),2) AS total_revenue
FROM telecom_customers
GROUP BY contract
ORDER BY total_revenue DESC;

-- Revenue by Internet Type
SELECT 
    internet_type, ROUND(SUM(total_revenue), 2) AS total_revenue
FROM
    telecom_customers
GROUP BY internet_type
ORDER BY total_revenue DESC;

-- Top 10 Revenue Cities
SELECT
city,
ROUND(SUM(total_revenue),2) AS total_revenue
FROM telecom_customers
GROUP BY city
ORDER BY total_revenue DESC
LIMIT 10;

-- Average CLTV
SELECT
ROUND(AVG(cltv),2) AS avg_cltv
FROM telecom_customers;

-- Top 10 Customers by CLTV
SELECT
customer_id,
cltv
FROM telecom_customers
ORDER BY cltv DESC
LIMIT 10;

-- Revenue Lost from Churned Customers
SELECT
ROUND(SUM(total_revenue),2) AS revenue_lost
FROM telecom_customers
WHERE churn_label = 'Yes';

