def EliminateStringFromInt(ColumnName):
    count = 0
    df[ColumnName] = df[ColumnName].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)
    for i in range(497):
      if(len(str(df['Establishment_year'][i])) > 6):
        count =  count + 1
    print(count)
    for i in range(497):
      if(len(str(df['Establishment_year'][i])) > 6):
        df.at[i,'Establishment_year'] = None

      if(len(str(df['Establishment_year'][i])) < 6):
        df.at[i,'Establishment_year'] = None
