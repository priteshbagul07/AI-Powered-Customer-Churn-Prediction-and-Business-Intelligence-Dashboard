USE telecom_churn;

-- Overall Churn Rate
SELECT
COUNT(*) AS total_customers,

SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END) AS churned_customers,

ROUND(
100*SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END)
/COUNT(*),2
) AS churn_rate

FROM telecom_customers;

-- Churn by Contract
SELECT
contract,
COUNT(*) AS customers,
SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END) AS churned,
ROUND(
100*SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END)
/COUNT(*),2
) AS churn_rate
FROM telecom_customers
GROUP BY contract
ORDER BY churn_rate DESC;

-- Churn by Internet Type
SELECT

internet_type,

COUNT(*) AS customers,

SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END) AS churned,

ROUND(
100*SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END)
/COUNT(*),2
) AS churn_rate

FROM telecom_customers

GROUP BY internet_type

ORDER BY churn_rate DESC;

-- Churn by Payment Method
SELECT

payment_method,

COUNT(*) AS customers,

SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END) AS churned,

ROUND(
100*SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END)
/COUNT(*),2
) AS churn_rate

FROM telecom_customers

GROUP BY payment_method

ORDER BY churn_rate DESC;

-- Churn by Phone Service
SELECT

phone_service,

COUNT(*) AS customers,

SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END) AS churned,

ROUND(
100*SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END)
/COUNT(*),2
) AS churn_rate

FROM telecom_customers

GROUP BY phone_service;

-- Churn by Tech Support
SELECT

premium_tech_support,

COUNT(*) AS customers,

SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END) AS churned,

ROUND(
100*SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END)
/COUNT(*),2
) AS churn_rate

FROM telecom_customers

GROUP BY premium_tech_support;

-- Churn Category 
SELECT

churn_category,

COUNT(*) AS customers

FROM telecom_customers

WHERE churn_label='Yes'

GROUP BY churn_category

ORDER BY customers DESC;

-- Churn by Tenure
SELECT

CASE

WHEN tenure_in_months<=12 THEN '0-12 Months'

WHEN tenure_in_months<=24 THEN '13-24 Months'

WHEN tenure_in_months<=48 THEN '25-48 Months'

ELSE '48+ Months'

END AS tenure_group,

COUNT(*) AS customers,

SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END) AS churned,

ROUND(
100*SUM(CASE WHEN churn_label='Yes' THEN 1 ELSE 0 END)
/COUNT(*),2
) AS churn_rate

FROM telecom_customers

GROUP BY tenure_group;