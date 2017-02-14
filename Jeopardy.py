
# coding: utf-8

# In[39]:

import pandas as pd 
import random
q_df = pd.read_json('JEOPARDY_QUESTIONS1.json')
q_df['value'] = q_df['value'].str.replace('$', '')
q_df['value'] = q_df['value'].str.replace(',', '')
q_df.dropna(inplace=True)
q_df['value'] = q_df['value'].astype(int)
#print(q_df.head())
#print(q_df.shape)
#print(q_df[q_df.isnull().any(axis=1)])


# In[43]:

rounds = input("How many rounds do you want to play? ")
score = 0
for x in range(0, int(rounds)):
    num = random.randrange(1,216929) 
    print(q_df.iloc[num][['category','value']].values)
    answer = input(q_df.iloc[num]['question'] + " ")
    if (answer == q_df.iloc[num]['answer']):
        print("you got it! "+ q_df.iloc[num]['answer'])
        score = score + q_df.iloc[num]['value']
    else:
        print("no the correct answer is "+ q_df.iloc[num]['answer'])
        score = score - q_df.iloc[num]['value']
    print("Your score is "+ str(score))




