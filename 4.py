import pandas as pd
import numpy as np

df = pd.read_csv('titanic.csv')
relatives_array = df[['SibSp', 'Parch']].values
total_relatives = np.sum(relatives_array)
passenger_with_most_relatives_index = np.argmax(np.sum(relatives_array, axis=1))
passenger_with_most_relatives_info = df.iloc[passenger_with_most_relatives_index]
print("Общее количество родственников на борту:", total_relatives)
print("Пассажир с наибольшим количеством родственников:", passenger_with_most_relatives_info['Name'])