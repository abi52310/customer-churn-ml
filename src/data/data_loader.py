import pandas as pd


class DataLoader:
    """
    Responsible for loading dataset from given path
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        try:
            df = pd.read_csv(self.file_path)
            print(f"[INFO] Data loaded successfully. Shape: {df.shape}")
            return df
        except FileNotFoundError:
            raise Exception(f"[ERROR] File not found: {self.file_path}")
        except Exception as e:
            raise Exception(f"[ERROR] Failed loading data: {e}")
