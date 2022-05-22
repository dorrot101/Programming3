import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn import datasets
from sklearn.decomposition import PCA

csvdata = pd.read_csv("wine4.csv", sep=",")
#1 散布図行列から、４つの属性値のそれぞれがブドウの品種の違いをどの程度表せているか、概要を150字程度で述べよ。
sns.pairplot(csvdata, hue="class", palette='bright', vars=["Alcohol", "Flavanoids","Color Intensity", "Proline"])
plt.show()  
csvdata.iloc[:,[0,1,2,3]] = (csvdata.iloc[:,[0,1,2,3]] - np.mean(csvdata.iloc[:,[0,1,2,3]], axis=0))/csvdata.iloc[:,[0,1,2,3]].std()
pca = PCA(n_components = 4)
PCA_components = csvdata.values
PCA_components[:,[0,1,2,3]] = pca.fit_transform(csvdata.iloc[:,[0,1,2,3]])
PCA_components = pd.DataFrame(data = PCA_components, columns = ['PC1','PC2','PC3','PC4','class'])
#2 主成分分析で第１主成分と第２主成分を求めプロットせよ。
#3 各主成分（第1主成分～第4主成分）に対する散布図行列を出力せよ。
sns.pairplot(PCA_components.iloc[:,[0,1,4]], hue = "class", palette='muted', vars = ["PC1",'PC2'])
plt.show()
sns.pairplot(PCA_components, hue = "class", palette='muted', vars = ["PC1",'PC2','PC3','PC4'])
plt.show()
#4 3)の散布図行列のうち「第1主成分 - 第2主成分ペア」と「第3主成分 – 第4主成分ペア」の図を比較せよ。
print(pca.explained_variance_)
print(pca.components_)
#5 各主成分の寄与率を求めよ。
print(pca.explained_variance_ratio_)