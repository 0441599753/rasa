import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Iris.csv' , index_col = 'Id')

labels = {
    'Iris-setosa': 0,
    'Iris-virginica': 1,
    'Iris-versicolor': 2
}

df['label'] = df['Species'].map(labels)


pedal_w_setosa = df[df['Species'] == 'Iris-setosa']['PetalWidthCm']
pedal_l_setosa = df[df['Species'] == 'Iris-setosa']['PetalLengthCm']




pedal_w_virginica= df[df['Species'] == 'Iris-virginica']['PetalWidthCm']
pedal_l_virginica = df[df['Species'] == 'Iris-virginica']['PetalLengthCm']
pedal_w_versicolor = df[df['Species'] == 'Iris-versicolor']['PetalWidthCm']
pedal_l_versicolor = df[df['Species'] == 'Iris-versicolor']['PetalLengthCm']



plt.figure(figsize=(16 , 10))
plt.bar(pedal_l_setosa ,  pedal_w_setosa , label = 'Setosa' , color = 'green')
plt.bar(pedal_l_versicolor ,  pedal_w_versicolor , label = 'Versicolor' , color = 'red')
plt.bar(pedal_l_virginica ,  pedal_w_virginica , label = 'Virginica' , color = 'yellow')
plt.legend()
plt.plot((4.11, 4.11) , (3, 0))
plt.plot((2.45, 2.45) , (3, 0))
plt.show()
