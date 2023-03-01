import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import parse

path = r'./data'
def getAppNames(path):
    list_of_files = os.listdir(path)
    app_names = []
    for file in list_of_files:
        name = parse.parse('submission_{}.csv',file)
        app_names.append(str(name)[10:-7])
    
    return app_names
appNames = getAppNames(path)

def creating_df(path, appNames):
    dfs = []
    for file in os.listdir(path):
        print("Reading "+file)
        data = pd.read_csv(path+'/'+ file)
        df = pd.DataFrame(data)
        print("Current Data Frame shape ")
        print(df.shape)
        df['appName'] = appNames[os.listdir(path).index(file)]
        dfs.append(df)
    print("Total Files found: ", len(dfs))
    final_df = pd.DataFrame()
    for i in range(len(dfs)):
        final_df = pd.concat([final_df, dfs[i]], axis=0)
        
    return final_df
    
final_df = creating_df(path, appNames)
final_df.to_csv(path+'/'+'final_submission.csv', index=False) 
print("Final Submission File SAVED!")
print("Final File Shape: ", final_df.shape)
final_df.head()
final_df['sentiment'] = np.where(final_df['score'] == 3, 'nutral')
final_df['sentiment'] = np.where(final_df['score'] <3, 'negative')
final_df['sentiment'] = np.where(final_df['score'] >3, 'positive')
final_df.head()