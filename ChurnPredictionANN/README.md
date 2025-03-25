# Churn Prediction Using ANN

## Project Overview
This project aims to predict customer churn using an Artificial Neural Network (ANN). The dataset contains customer information, including demographics, account details, and past behaviors. The goal is to classify whether a customer will churn (leave) or stay active.

## Technologies Used
- Python
- TensorFlow/Keras
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn

## Dataset Details

https://www.kaggle.com/code/devahuja2808/churn-modelling-using-ann/input?select=Churn_Modelling.csv

The dataset includes the following key features:
- **Customer Demographics**: Gender, Geography
- **Account Details**: Balance, Credit Score, Tenure
- **Behavioral Factors**: Number of products, estimated salary, active status
- **Target Variable**: `Exited` (1 for churned customers, 0 for active customers)

## Steps Involved
1. **Data Preprocessing**
   - Removal of unnecessary columns (RowNumber, CustomerId, Surname)
   - Encoding categorical variables
   - Standardizing numerical features
   
2. **Exploratory Data Analysis**
   - Visualization of churn distribution using Seaborn
   - Correlation analysis and feature impact assessment

3. **Building the ANN Model**
   - Input layer with 32 neurons (ReLU activation)
   - Hidden layer with 16 neurons (ReLU activation)
   - Output layer with 1 neuron (Sigmoid activation)
   - Dropout layers for regularization

4. **Model Training & Evaluation**
   - Train-test split (80%-20%)
   - Optimization using Adam
   - Evaluation using accuracy, confusion matrix, and classification report
   
5. **Visualization of Results**
   - Training and validation accuracy plots
   - Confusion matrix
   - Final summary of customer statistics

## Final Summary
- **Total Customers**: `10000`
- **Active Customers**: `7963`
- **Churned Customers**: `2037`

Out of `10000` customers, `7963` are still active, while `2037` have left.

## How to Run the Code
1. Install dependencies using:
   ```bash
   pip install tensorflow pandas numpy matplotlib seaborn scikit-learn
   ```
2. Run the Python script.
   ```bash
   python churn_prediction_ann.py
   ```
3. Analyze the output, visualizations, and performance metrics.

This README provides a high-level overview of the project. Update values in the **Final Summary** section after executing the script. 🚀

