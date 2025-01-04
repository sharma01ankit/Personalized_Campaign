##Merchant Campaign Personalization Tool

This project involves building a feature for a merchant application where merchants can design their own marketing campaigns targeting specific customer segments based on radius, age, gender, and customer tags. The system leverages customer transaction data, demographic attributes, and purchase patterns to create meaningful customer segments and identify analogous customer behaviors for more effective targeting.

Objective

Customer Segmentation:

Identify and create relevant customer segments for merchants based on past campaign scenarios and common requests.

Develop 23 customer tags by analyzing transaction, demographic, and behavioral data.

Use RFM (Recency, Frequency, Monetary) analysis to filter and segment customers.

Look-alike Customer Identification:

Predict customers likely to belong to specific segments using their purchase patterns.

Leverage machine learning models to find customers with analogous behavior who do not meet the strict RFM criteria.

Implementation

1. Customer Segmentation

Steps:

Dataset Creation:

Prepare a member-level dataset with relevant features for segmentation.

Ensure inclusion of transaction data, demographic attributes, and behavioral metrics.

Outlier Capping:

Identify and cap outliers using percentile cutoffs for key variables.

Feature Standardization:

Standardize metrics for Recency (R), Frequency (F), and Monetary (M) values.

Score Buckets:

Categorize RFM metrics into score buckets for easier segmentation analysis.

Cutoff Selection:

Define thresholds for R, F, and M metrics based on business rules to segment customers.

2. Look-alike Customer Identification

Steps:

Feature Engineering:

Generate 723 variables using transaction history, demographics, category-specific behavior, seasonality, redemption history, and online/offline activity.

Machine Learning Model:

Use the XGBoost algorithm for predicting customer tags.

Train the model with labeled data and evaluate performance using validation metrics.

Customer Classification:

Identify customers likely to belong to specific segments based on patterns learned by the model.

Key Components

Customer Tags

Examples of predefined customer tags include:

Prefers Local Stores: Shoppers at local boutiques, parlors, and suiting/shirting stores.

Discount Sensitive: Customers preferring value-for-money deals.

Luxury Buyers: Frequent shoppers at high-end stores and restaurants.

Health Conscious: Customers prioritizing health-related purchases.

Adrenaline Junkies: Customers engaging in adventure activities.

Variables

Transaction Features: Total spends, transaction count, category-wise metrics, and seasonality.

Demographics: City, age, gender, and household attributes.

Behavioral Patterns: Online/offline activity, redemption data, and purchasing during specific occasions (e.g., birthdays).

Model Selection

XGBoost:

Handles large feature sets efficiently (700+ variables).

Robust to multicollinearity and variable standardization.

Provides high accuracy with low bias and variance.
