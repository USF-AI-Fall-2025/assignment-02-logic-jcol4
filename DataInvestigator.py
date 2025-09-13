import pandas as pd

class DataInvestigator:
    def __init__(self, df: pd.DataFrame):
        try:
            self.df = df
            self.error = False
        except Exception:
            self.error = True
            
    def baseline(self, col: int):
        if self.error or col < 0 or col >= self.df.shape[1]:
            return None
        try:
            return self.df.iloc[:, col].mode()[0]
        except Exception:
            return None
        
    def corr(self, col1: int, col2: int):
        if (
            self.error
            or col1 < 0 or col1 >= self.df.shape[1]
            or col2 < 0 or col2 >= self.df.shape[1]
        ):
            return None
        try:
            return self.df.iloc[:, col1].corr(self.df.iloc[:, col2])
        except Exception:
            return None

    def zeroR(self, col: int):
        if self.error or col < 0 or col >= self.df.shape[1]:
            return None
        try:
            target_col = self.df.iloc[:, col]
            majority_class = target_col.mode()[0]
            return majority_class
        except Exception:
            return None

