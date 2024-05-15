import pandas as pd
import matplotlib as pu
import seaborn as sb
file_t = 'test.csv'
test_data = pd.read_csv(file_t)
print(test_data.head(10))
print(test_data.shape)
print(test_data.isnull().sum())
print(test_data.dtypes)