# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 13:28:10 2020

@author: Christian
"""

import pandas as pd
import seaborn as sb

# READ DATA
movie_data = pd.read_table('http://bit.ly/movieusers', sep ='|', header = None)
movie_data.isnull().sum()
movie_data.head(20)



movie_data.shape

# ADD COLUMN NAMES
movie_data = movie_data.rename(columns = {0:'Index', 1:'Age', 2:'Sex', 3:'Job', 4:'Zip_Code'})
movie_data.head()

# REMOVE UNECESSARY COLUMNS
movie_data.drop('Index', axis = 1, inplace = True)


# RENAME VALUES FOR SEX VARIABLE
movie_data.loc[movie_data.Sex == 'M' , 'Sex'] = 'Male'
movie_data.loc[movie_data.Sex == 'F' , 'Sex'] = 'Female'


movie_data.Job.unique()

sb.violinplot(x = movie_data.Job, y = movie_data.Age, hue = movie_data.Sex)
sb.
sb.boxplot(x = movie_data.Sex, y = movie_data.Age)



movie_data.Age.hist()


movie_data[movie_data.Job.isin(['educator', 'student', 'engineer', 'writer'])]
plt_data = movie_data[movie_data.Job.isin(['educator', 'student', 'engineer', 'writer'])]
sb.violinplot(x = plt_data.Job, y = plt_data.Age, hue = jobs.Sex)



#######
ufo_data = pd.read_csv('http://bit.ly/uforeports')
ufo_data.head()
















df = pd.DataFrame({"X": [1,1,2,1,1], "Y": ["A","D","B","C", "D"]})
df[(df.X == 1) & df.Y.isin(["A","B","C"])]





