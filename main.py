from src.data.data_loader import DataLoader
from src.data.data_inspector import DataInspector
from src.data.data_cleaner import DataCleaner
from src.config.data_cleaning_config import CLEANING_CONFIG




def main():
    # Dataset path
    data_path = "data/raw/churn.csv"

    print("[INFO] Starting Customer Churn Pipeline...")

    # Ingestion
    loader = DataLoader(data_path)
    df = loader.load_data()

    #Inspection
    inspector = DataInspector(df)
    inspector.basic_info()
    inspector.column_types()
    inspector.missing_values()
    inspector.target_distribution("Churn")
    inspector.statistical_summary()

    # Cleaning
    print("\n[INFO] Cleaning Data...")

    cleaner = DataCleaner(CLEANING_CONFIG)
    df_clean = cleaner.clean(df)

    print("\n[INFO] Cleaned Data Preview:")
    print(df_clean.head())



    # Show first few rows
    print("\n[INFO] Dataset Preview:")
    print(df.head())


if __name__ == "__main__":
    main()
