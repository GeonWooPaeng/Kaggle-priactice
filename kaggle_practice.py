#%%
import pandas as pd 

train = pd.read_csv('titanic/train.csv')
test = pd.read_csv('titanic/test.csv')

#%%
train.head()

#%%
test.head()

#%%
train.shape

#%%
test.shape

#%%
train.info()

#%%
test.info()

#%%
train.isnull().sum()
#빠진부분 표시
#%%
test.isnull().sum()

#%%
import matplotlib.pyplot as plt
%matplotlib inline 
import seaborn as sns 
sns.set()

#%%
def bar_chart(feature):
    survived = train[train['Survived']==1][feature].value_counts()
    dead = train[train['Survived']==0][feature].value_counts()
    df = pd.DataFrame([survived,dead])
    df.index = ['Survived','Dead']
    df.plot(kind='bar',stacked=True, figsize=(10,5))

#%%
bar_chart('Sex')

#%%
bar_chart('Pclass')

#%%
bar_chart('SibSp')

#%%
bar_chart('Parch')

#%%
bar_chart('Embarked')

#%%
train_test_data = [train, test]

#%%
