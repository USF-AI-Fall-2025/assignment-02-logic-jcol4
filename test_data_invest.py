#copied from lab spec along with printing demonstrating corr and zeroR
import pandas as pd
from DataInvestigator import DataInvestigator

df = pd.read_csv("gallstone.csv")
di = DataInvestigator(df)

print(di.baseline(1))
print(di.corr(0, 1))
print(di.zeroR(1))
