CLEANING_CONFIG = {

    # ---------------------------
    # GENERAL CLEANING RULES
    # ---------------------------
    "strip_whitespace": True,
    "replace_blank_with_nan": True,


    # ---------------------------
    # SCHEMA ENFORCEMENT
    # ---------------------------
    "numeric_columns": [
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ],

    "categorical_columns": [
        "gender",
        "Partner",
        "Dependents",
        "PhoneService",
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "Contract",
        "PaperlessBilling",
        "PaymentMethod"
    ],


    # ---------------------------
    # MISSING VALUE STRATEGY
    # ---------------------------
    "missing_value_strategy": {
        "TotalCharges": "median"
    },


    # ---------------------------
    # TARGET PROCESSING
    # ---------------------------
    "target_column": "Churn",

    "target_mapping": {
        "Yes": 1,
        "No": 0
    }

}
