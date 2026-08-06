CREATE DATABASE telecom_churn;
USE telecom_churn;

-- Renaming columns
ALTER TABLE telecom_customers RENAME COLUMN `Customer ID` TO customer_id;
ALTER TABLE telecom_customers RENAME COLUMN `Under 30` TO under_30;
ALTER TABLE telecom_customers RENAME COLUMN `Senior Citizen` TO senior_citizen;
ALTER TABLE telecom_customers RENAME COLUMN `Number of Dependents` TO number_of_dependents;
ALTER TABLE telecom_customers RENAME COLUMN `Zip Code` TO zip_code;
ALTER TABLE telecom_customers RENAME COLUMN `Referred a Friend` TO referred_a_friend;
ALTER TABLE telecom_customers RENAME COLUMN `Number of Referrals` TO number_of_referrals;
ALTER TABLE telecom_customers RENAME COLUMN `Tenure in Months` TO tenure_in_months;
ALTER TABLE telecom_customers RENAME COLUMN `Phone Service` TO phone_service;
ALTER TABLE telecom_customers RENAME COLUMN `Avg Monthly Long Distance Charges` TO avg_monthly_long_distance_charges;
ALTER TABLE telecom_customers RENAME COLUMN `Multiple Lines` TO multiple_lines;
ALTER TABLE telecom_customers RENAME COLUMN `Internet Service` TO internet_service;
ALTER TABLE telecom_customers RENAME COLUMN `Internet Type` TO internet_type;
ALTER TABLE telecom_customers RENAME COLUMN `Avg Monthly GB Download` TO avg_monthly_gb_download;
ALTER TABLE telecom_customers RENAME COLUMN `Online Security` TO online_security;
ALTER TABLE telecom_customers RENAME COLUMN `Online Backup` TO online_backup;
ALTER TABLE telecom_customers RENAME COLUMN `Device Protection Plan` TO device_protection_plan;
ALTER TABLE telecom_customers RENAME COLUMN `Premium Tech Support` TO premium_tech_support;
ALTER TABLE telecom_customers RENAME COLUMN `Streaming TV` TO streaming_tv;
ALTER TABLE telecom_customers RENAME COLUMN `Streaming Movies` TO streaming_movies;
ALTER TABLE telecom_customers RENAME COLUMN `Streaming Music` TO streaming_music;
ALTER TABLE telecom_customers RENAME COLUMN `Unlimited Data` TO unlimited_data;
ALTER TABLE telecom_customers RENAME COLUMN `Paperless Billing` TO paperless_billing;
ALTER TABLE telecom_customers RENAME COLUMN `Payment Method` TO payment_method;
ALTER TABLE telecom_customers RENAME COLUMN `Monthly Charge` TO monthly_charge;
ALTER TABLE telecom_customers RENAME COLUMN `Total Charges` TO total_charges;
ALTER TABLE telecom_customers RENAME COLUMN `Total Refunds` TO total_refunds;
ALTER TABLE telecom_customers RENAME COLUMN `Total Extra Data Charges` TO total_extra_data_charges;
ALTER TABLE telecom_customers RENAME COLUMN `Total Long Distance Charges` TO total_long_distance_charges;
ALTER TABLE telecom_customers RENAME COLUMN `Total Revenue` TO total_revenue;
ALTER TABLE telecom_customers RENAME COLUMN `Satisfaction Score` TO satisfaction_score;
ALTER TABLE telecom_customers RENAME COLUMN `Customer Status` TO customer_status;
ALTER TABLE telecom_customers RENAME COLUMN `Churn Label` TO churn_label;
ALTER TABLE telecom_customers RENAME COLUMN `Churn Score` TO churn_score;
ALTER TABLE telecom_customers RENAME COLUMN `Churn Category` TO churn_category;
ALTER TABLE telecom_customers RENAME COLUMN `Churn Reason` TO churn_reason;


