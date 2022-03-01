import sklearn 
from sklearn import datasets
from sklearn.datasets import fetch_openml
mice = fetch_openml(name='miceprotein',version=4)
print(mice.details)