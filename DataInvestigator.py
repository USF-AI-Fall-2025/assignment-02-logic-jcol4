import pandas as pd

class DataInvestigator:
    #init datainvestigator
    def __init__(self, df: pd.DataFrame):
        #store as datafram, set error to false
        try:
            self.df = df
            self.error = False
        #if exception in assignment, set error to true
        except Exception:
            self.error = True

    #returns most frequent value in specified column
    def baseline(self, col: int):
        #check if error or if column is out of bounds from dataframe
        if self.error or col < 0 or col >= self.df.shape[1]:
            return None
        #select column based off entered int, and return most frequent value in that column
        try:
            return self.df.iloc[:, col].mode()[0]
            #if any errors return none
        except Exception:
            return None
        
    #returns linear correlation coef between two columns
    def corr(self, col1: int, col2: int):
        #if any errors or any out of bounds column indices, return none
        if (
            self.error
            or col1 < 0 or col1 >= self.df.shape[1]
            or col2 < 0 or col2 >= self.df.shape[1]
        ):
            return None
        #use pandas correlation method to find coefficient between two columns
        try:
            return self.df.iloc[:, col1].corr(self.df.iloc[:, col2])
        #return none if any errors are found
        except Exception:
            return None

    #returns zeroR classifier of column
    def zeroR(self, col: int):
        #if any errors or column is out of bounds
        if self.error or col < 0 or col >= self.df.shape[1]:
            return None
        #get column and find the majority class of it
        try:
            target_col = self.df.iloc[:, col]
            majority_class = target_col.mode()[0]
            return majority_class
        #return none if any exceptions
        except Exception:
            return None

