from src.data.data_loader import DataLoader
from src.data.data_inspector import DataInspector



def main():
    # Dataset path
    data_path = "data/raw/churn.csv"

    print("[INFO] Starting Customer Churn Pipeline...")

    # Load Data
    loader = DataLoader(data_path)
    df = loader.load_data()

    inspector = DataInspector(df)
    inspector.basic_info()
    inspector.column_types()
    inspector.missing_values()
    inspector.target_distribution("Churn")
    inspector.statistical_summary()


    # Show first few rows
    print("\n[INFO] Dataset Preview:")
    print(df.head())


if __name__ == "__main__":
    main()
