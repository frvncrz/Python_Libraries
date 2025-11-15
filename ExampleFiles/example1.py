import pandas as pd

myDataSet = {
    'cars': ['BMW', 'Porche', 'Ferrari'],
    'passing': [3, 7, 2]
}

myVar = pd.DataFrame(myDataSet)
print(myVar)