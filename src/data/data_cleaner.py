import pandas as pd
import numpy as np


class DataCleaner:
    """
    Production-grade data cleaner:
    - Config driven
    - Schema aware
    - Numeric enforcement
    - Missing value handling
    - Target processing
    """

    def __init__(self, config: dict):
        self.config = config

    # ------------------------------------------------
    # MAIN PIPELINE ENTRY
    # ------------------------------------------------
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:

        df = df.copy()

        # Step 1 — Strip whitespace
        if self.config.get("strip_whitespace", False):
            df = self._strip_whitespace(df)

        # Step 2 — Replace blank with NaN
        if self.config.get("replace_blank_with_nan", False):
            df = self._replace_blank_with_nan(df)

        # Step 3 — Schema-driven numeric conversion
        df = self._convert_numeric_columns(df)

        # Step 4 — Missing value handling
        df = self._handle_missing_values(df)

        # Step 5 — Target processing
        df = self._process_target(df)

        return df

    # ------------------------------------------------
    # CLEANING HELPERS
    # ------------------------------------------------

    def _strip_whitespace(self, df: pd.DataFrame):

        for col in df.select_dtypes(include="object"):
            df[col] = df[col].astype(str).str.strip()

        return df

    def _replace_blank_with_nan(self, df: pd.DataFrame):
        return df.replace(r'^\s*$', np.nan, regex=True)

    # ------------------------------------------------
    # NUMERIC SCHEMA ENFORCEMENT (PRODUCTION GRADE)
    # ------------------------------------------------
    def _convert_numeric_columns(self, df: pd.DataFrame):

        numeric_cols = self.config.get("numeric_columns", [])

        for col in numeric_cols:

            if col not in df.columns:
                continue

            before_null = df[col].isnull().sum()

            df[col] = pd.to_numeric(df[col], errors="coerce")

            after_null = df[col].isnull().sum()

            new_nulls = after_null - before_null

            print(f"[NUMERIC CLEAN] {col} → converted. New nulls introduced: {new_nulls}")

            if new_nulls > 0:
                print(f"[WARNING] {col}: {new_nulls} values could not be converted to numeric")

        return df

    # ------------------------------------------------
    # MISSING VALUE HANDLING
    # ------------------------------------------------
    def _handle_missing_values(self, df: pd.DataFrame):

        strategy_map = self.config.get("missing_value_strategy", {})

        for col, strategy in strategy_map.items():

            if col not in df.columns:
                continue

            if strategy == "mean":
                df[col] = df[col].fillna(df[col].mean())

            elif strategy == "median":
                df[col] = df[col].fillna(df[col].median())

            elif strategy == "mode":
                df[col] = df[col].fillna(df[col].mode()[0])

        return df

    # ------------------------------------------------
    # TARGET PROCESSING
    # ------------------------------------------------
    def _process_target(self, df: pd.DataFrame):

        target_col = self.config.get("target_column")
        mapping = self.config.get("target_mapping")

        if target_col and mapping and target_col in df.columns:
            df[target_col] = df[target_col].map(mapping)

        return df
