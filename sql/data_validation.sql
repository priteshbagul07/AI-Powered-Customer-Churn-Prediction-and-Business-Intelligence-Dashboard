USE telecom_churn;

-- Preview Data
SELECT *
FROM telecom_customers
LIMIT 5;

-- Total records
SELECT COUNT(*) AS total_customers
FROM telecom_customers;

-- Checking table structure
DESCRIBE telecom_customers;

-- Checking duplicate customer id
SELECT Customer_ID,
COUNT(*) AS duplicate_count
FROM telecom_customers
GROUP BY Customer_ID
HAVING COUNT(*) > 1;

-- Churn class distribution
SELECT Churn_Label,
COUNT(*) AS customers
FROM telecom_customers
GROUP BY Churn_Label;

-- Checking null values
SELECT
SUM(customer_id IS NULL) AS customer_id_nulls,
SUM(age IS NULL) AS age_nulls,
SUM(contract IS NULL) AS contract_nulls,
SUM(monthly_charge IS NULL) AS monthly_charge_nulls,
SUM(total_charges IS NULL) AS total_charges_nulls,
SUM(churn_label IS NULL) AS churn_label_nulls
FROM telecom_customers;

-- Checking Blank Strings
SELECT
SUM(contract = '') AS contract_blank,
SUM(payment_method = '') AS payment_blank,
SUM(internet_type = '') AS internet_blank,
SUM(churn_reason = '') AS churn_reason_blank
FROM telecom_customers;

-- Age
SELECT
MIN(age) AS min_age,
MAX(age) AS max_age
FROM telecom_customers;

-- Monthly Charge
SELECT
MIN(monthly_charge),
MAX(monthly_charge)
FROM telecom_customers;

-- Total Charges
SELECT
MIN(total_charges),
MAX(total_charges)
FROM telecom_customers;

-- Total Revenue
SELECT
MIN(total_revenue),
MAX(total_revenue)
FROM telecom_customers;

-- Tenure
SELECT
MIN(tenure_in_months),
MAX(tenure_in_months)
FROM telecom_customers;

-- Checking Invalid Values
SELECT *
FROM telecom_customers
WHERE age < 0;

SELECT *
FROM telecom_customers
WHERE monthly_charge < 0;

SELECT *
FROM telecom_customers
WHERE total_revenue < 0;

SELECT *
FROM telecom_customers
WHERE tenure_in_months < 0;

-- Checking Distinct Categories
SELECT DISTINCT gender
FROM telecom_customers;

SELECT DISTINCT contract
FROM telecom_customers;

SELECT DISTINCT internet_type
FROM telecom_customers;

SELECT DISTINCT offer
FROM telecom_customers;

SELECT DISTINCT payment_method
FROM telecom_customers;

SELECT DISTINCT customer_status
FROM telecom_customers;

