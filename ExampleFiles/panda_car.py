# we can import pandas just like numpy
import pandas as pd
# Series - we can pass through values like so
type_car = pd.Series(['BMW', 'Porsche'])
print(type_car)
# DataFrame - passing a dictionary of objects
df = pd.DataFrame({'Price': [39600, 62900], 'model_year': [2020, 2024]})
print(df.head())

# 0        BMW
# 1    Porsche
# dtype: object
#    Price  model_year
# 0  39600        2020
# 1  62900        2024