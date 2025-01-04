# System Architecture

## Overview
The tool comprises two main components:
1. **Segmentation Engine**: Uses RFM analysis to group customers.
2. **Prediction Model**: XGBoost predicts look-alike customers.

## Workflow
1. Input raw data.
2. Preprocess and segment customers.
3. Train and evaluate the prediction model.
4. Serve results via REST API.
