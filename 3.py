import pandas as pd
import matplotlib as pu
import seaborn as sb
file_t = 'train.csv'
train_data = pd.read_csv(file_t)
column_t = ['name', 'ticket', 'cabin']
train_data.drop(columns = column_t, inplace = True)
age_t = train_data['Age'].median()
train_data['Age'].fill(age_t,inplace=True)
train_data = pd.set_dumnies(train_data, colums = ['Sex'], drop_first=True)
