from src.data.data_loader import DataLoader


def main():
    # Dataset path
    data_path = "data/raw/churn.csv"

    print("[INFO] Starting Customer Churn Pipeline...")

    # Load Data
    loader = DataLoader(data_path)
    df = loader.load_data()

    # Show first few rows
    print("\n[INFO] Dataset Preview:")
    print(df.head())


if __name__ == "__main__":
    main()
