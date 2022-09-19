import pandas as pd

df = pd.read_csv("/content/agg_cleaned.csv")

def EliminateStringFromInt(ColumnName):
    count = 0
    df[ColumnName] = df[ColumnName].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)
    for i in range(497):
      if(len(str(df['year_of_licence'][i])) > 6):
        count =  count + 1
    print(count)
    for i in range(497):
      if(len(str(df['year_of_licence'][i])) > 6):
        #df.at[i,'year_of_licence'] = None
        df['Establishment_year'] = df['year_of_licence'].astype(str).str[:4]

      if(len(str(df['year_of_licence'][i])) < 4):
        df.at[i,'year_of_licence'] = None

EliminateStringFromInt('year_of_licence')


with pd.option_context('display.max_rows', None):
  print(df['year_of_licence'].value_counts().astype(int))
