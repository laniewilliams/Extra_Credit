# The Iris dataset is referred to as a “toy dataset” because it has only 150 samples and four features. 
# The dataset describes 50 samples for each of three Iris flower species—Iris setosa, Iris versicolor and Iris 
# virginica. Each sample’s features are the sepal length, sepal width, petal 
# length and petal width, all measured in centimeters. The sepals are the larger outer parts of each flower 
# that protect the smaller inside petals before the flower buds bloom.

#EXERCISE
# load the iris dataset and use classification
# to see if the expected and predicted species
# match up

# display the shape of the data, target and target_names

# display the first 10 predicted and expected results using
# the species names not the number (using target_names)

# display the values that the model got wrong

# visualize the data using the confusion matrix
import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df["target"] = iris.target
print(df.head())











# display the shape of the data, target and target_names
print(iris.data.shape)
print(iris.target)
print(iris.target_names)

from sklearn.model_selection import train_test_split

data_train, data_test, target_train, target_test = train_test_split(iris.data, iris.target,random_state=11)

print(data_train.shape) #training the data --> 2-D
print(data_test.shape)
print(target_train.shape) # just going to 1-D
print(target_test.shape)

# display the first 10 predicted and expected results using
# the species names not the number (using target_names)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()

knn.fit(X=data_train , y=target_train)  #it all comes down to this one method. this will do all of the machine learning. 
                                        #It needs the data (what it should look at) and the target (what it should be)

predicted = knn.predict(X=data_test) #only have X because you don't need the target because it will tell you the target

#how do we know if it's correct?
expected = target_test

print(predicted[:10])
print(expected[:10])
# display the values that the model got wrong
wrong = [(p,e)for (p,e) in zip(predicted,expected) if p != e] #put in the wrongs as a tuple in a list called wrong
print(wrong)

# visualize the data using the confusion matrix

from sklearn.metrics import confusion_matrix

confusion = confusion_matrix(y_true=expected, y_pred=predicted)
print(confusion) #allows you the see where it kind of messed up. 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt2

confusion_df = pd.DataFrame(confusion, index=range(3), columns=range(3))

figure = plt2.figure(figsize=(7,6))
axes = sns.heatmap(confusion_df, annot=True, cmap=plt2.cm.nipy_spectral_r)
plt2.show()

print("done")
# each row represents one of the classes
# each column represents what the program guesses the class as
# numbers outside of the diagnal represent wrong guesses