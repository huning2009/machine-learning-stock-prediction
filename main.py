from sklearn.datasets import load_iris 
from sklearn.neighbors import KNeighborsClassifier 
import numpy as np 
from sklearn.model_selection import train_test_split

singularData = open("data/AMR_quarterly_financial_data.csv").read().splitlines()
print(singularData)