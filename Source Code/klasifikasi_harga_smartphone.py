# -*- coding: utf-8 -*-
"""Klasifikasi Harga Smartphone.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DIYR2w1gx8EY4SJ1mudmusOZwVARfOFw

**KLASIFIKASI HARGA SMARTPHONE DENGAN KNN**

**Import Library**
"""

# Commented out IPython magic to ensure Python compatibility.
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt #visualisasi data
import pandas as pd #proses data
# %matplotlib inline

import warnings

warnings.filterwarnings('ignore')

"""**Read Dataset**"""

df = pd.read_csv('dataset_mobile.csv', header=None)

"""**Eksplorasi Data**"""

df.shape

# Menampilkan 5 data teratas
df.head()

# Melakukan rename pada kolom dataset sesuai dengan nama atribut
rename_col = ['battery_power','blue','clock_speed', 'dual_sim', 'fc', 'four_g', 'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height', 'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g', 'touch_screen', 'wifi', 'price_range']
df.columns = rename_col
df.columns

# Menghapus baris pertama (nama atribut) karena tidak diperlukan
df.drop(labels=0, axis=0, inplace=True)
df.head()

# Melihat informasi dari dataset
df.info()

# Mengubah tipe data ke numerik, karena "Data Type" masih berupa objek
df = df.apply(pd.to_numeric, errors='coerce')
df.dtypes

# Melihat value dari target class
df['price_range'].unique()

# Melakukan pengecekan nilai yang null
df.isnull().sum()

"""**Membuat Variabel Khusus Untuk Dataframe Yang Memiliki Fitur dan Target Class**"""

X = df.drop(['price_range'], axis=1)

y = df['price_range']

"""**Membuat Data Training dan Data Testing**"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

X_train.shape, X_test.shape

"""**Menggunakan KNN Untuk Melatih Data Training**"""

# Mendeklarasikan nilai k
k = 5

# Membuat KNN model
model = KNeighborsClassifier(n_neighbors=k)

# Melatih model dengan data training
model.fit(X_train, y_train)

"""**Prediksi Target Class Dari Data Testing**"""

# Prediksi class dilakukan menggunakan atribut pada data testing
y_pred = model.predict(X_test)
y_pred

"""**Melihat Skor Akurasi**"""

# Mengecek prediksi akurasi
akurasi = accuracy_score(y_pred, y_test)*100

print('Akurasi Model : ' + str(round(akurasi, 2)) + ' %.')

"""**Mengubah Nilai K**
(pada tahap ini akan dicoba beberapa nilai k yang berbeda)
"""

# Mendeklarasikan nilai k
k = 6

# Membuat KNN model
model = KNeighborsClassifier(n_neighbors=k)

# Melatih model dengan data training
model.fit(X_train, y_train)

# Melakukan prediksi class menggunakan atribut di data testing
y_pred_6 = model.predict(X_test)

# membandingkan hasil prediksi dengan class data testing
akurasi = accuracy_score(y_pred_6, y_test)*100

print('Akurasi Model: ' + str(round(akurasi, 2)) + ' %.')

# Mendeklarasikan nilai k
k = 7

# Membuat KNN model
model = KNeighborsClassifier(n_neighbors=k)

# Melatih model dengan data training
model.fit(X_train, y_train)

# Melakukan prediksi class menggunakan atribut di data testing
y_pred_7 = model.predict(X_test)

# membandingkan hasil prediksi dengan class data testing
akurasi = accuracy_score(y_pred_7, y_test)*100

print('Akurasi Model: ' + str(round(akurasi, 2)) + ' %.')

# Mendeklarasikan nilai k
k = 8

# Membuat KNN model
model = KNeighborsClassifier(n_neighbors=k)

# Melatih model dengan data training
model.fit(X_train, y_train)

# Melakukan prediksi class menggunakan atribut di data testing
y_pred_8 = model.predict(X_test)

# membandingkan hasil prediksi dengan class data testing
akurasi = accuracy_score(y_pred_8, y_test)*100

print('Akurasi Model: ' + str(round(akurasi, 2)) + ' %.')

"""**Confussion Matriks**"""

#Menggunakan nilai k = 7 dikarenakan akurasi model yang dihasilkan tertinggi dengan nilai 95.25%
cm = confusion_matrix(y_test, y_pred_7)
print('Confusion matrix\n\n', cm)

"""**Visualisasi Data Confussion Matriks**"""

# Membuat plot confussion matrix
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)

# Menambahkan label pada garis horizontal (x) dan vertikal (y)
plt.title('Confussion Matrix')
plt.colorbar()
tick_marks = np.arange(4)
plt.xticks(tick_marks, ['Class 0', 'Class 1', 'Class 2', 'Class 3'])
plt.yticks(tick_marks, ['Class 0', 'Class 1', 'Class 2', 'Class 3'])

# Menambahkan nilai di dalam kotak matriks
thresh = cm.max() / 2.
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, format(cm[i, j], 'd'),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

# Menampilkan plot
plt.tight_layout()
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.show()

"""**Menghitung TP, FP, dan FN Tiap Class**"""

#Note
#a: class 0
#b: class 1
#c: class 2
#d: class 3

#TP = True Positive
#FP = False Positive
#FN = False Negative


# Menghitung TP tiap class
TP_a = cm[0,0]
TP_b = cm[1,1]
TP_c = cm[2,2]
TP_d = cm[3,3]

print("TP a =", TP_a)
print("TP b =", TP_b)
print("TP c =", TP_c)
print("TP d =", TP_d)
print("\n")

# Menghitung FP tiap class
FP_a = sum(cm[1:3, 0])
FP_b = sum(cm[:4, 1]) - cm[1,1]
FP_c = sum(cm[:4, 2]) - cm[2,2]
FP_d = sum(cm[:4, 3]) - cm[3,3]

print("FP a =", FP_a)
print("FP b =", FP_b)
print("FP c =", FP_c)
print("FP d =", FP_d)
print("\n")

# Menghitung FN tiap class
FN_a = sum(cm[0, :4]) - cm[0,0]
FN_b = sum(cm[1, :4]) - cm[1,1]
FN_c = sum(cm[2, :4]) - cm[2,2]
FN_d = sum(cm[3, :4]) - cm[3,3]

print("FN a =", FN_a)
print("FN b =", FN_b)
print("FN c =", FN_c)
print("FN d =", FN_d)

"""**Menghitung Precision**"""

P_a = TP_a/(TP_a+FP_a)
P_b = TP_b/(TP_b+FP_b)
P_c = TP_c/(TP_c+FP_c)
P_d = TP_d/(TP_d+FP_d)
P = (P_a+P_b+P_c+P_d)/4
print('Precision : {0:0.4f}'.format(P))

"""**Menghitung Recall**"""

R_a = TP_a/(TP_a+FN_a)
R_b = TP_b/(TP_b+FN_b)
R_c = TP_c/(TP_c+FN_c)
R_d = TP_d/(TP_d+FN_d)
R = (R_a+R_b+R_c+R_d)/4
print('Recall : {0:0.4f}'.format(R))

