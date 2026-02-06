import pandas as pd


class DataInspector:
    """
    Responsible for inspecting dataset quality and structure
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def basic_info(self):
        print("\n" + "=" * 50)
        print("DATASET BASIC INFO")
        print("=" * 50)

        print(f"Rows    : {self.df.shape[0]}")
        print(f"Columns : {self.df.shape[1]}")

    def column_types(self):
        print("\n" + "=" * 50)
        print("COLUMN DATA TYPES")
        print("=" * 50)

        print(self.df.dtypes)

    def missing_values(self):
        print("\n" + "=" * 50)
        print("MISSING VALUES REPORT")
        print("=" * 50)

        missing = self.df.isnull().sum()
        missing = missing[missing > 0]

        if len(missing) == 0:
            print("No missing values found ✅")
        else:
            print(missing)

    def target_distribution(self, target_column: str):
        print("\n" + "=" * 50)
        print(f"TARGET DISTRIBUTION → {target_column}")
        print("=" * 50)

        if target_column not in self.df.columns:
            print(f"[WARNING] Column {target_column} not found")
            return

        dist = self.df[target_column].value_counts(normalize=True) * 100
        print(dist)

    def statistical_summary(self):
        print("\n" + "=" * 50)
        print("STATISTICAL SUMMARY (NUMERIC)")
        print("=" * 50)

        print(self.df.describe())
