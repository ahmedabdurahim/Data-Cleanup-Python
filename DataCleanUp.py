import pandas as pd

class DataCleanUp:
  df = pd.read_csv("/content/agro_clean_data.csv")

  #Count how much a string in a cell appears in the whole file

  def CountAppearances():
    counter = 0
    for i in range(Rows):
      
      ######################################################################
      # Modify these parameters running code or it will generate an error! #
      ######################################################################
      
      if (df.at[i,'ColumnName'] == "string to look for"):
        counter = counter + 1

    if(counter > 1):
      print("The string has appeared " + str(counter) + " times in this spreadsheet")
    elif(counter == 1):
      print("The string has appeared only once")
    else:
      ("Could not find the string")


 #Change the character from a cell to a different char

  def FixCells(ColumnName, OldCharacter, NewCharacter):
    df[ColumnName] = df[ColumnName].str.replace(OldCharacter,NewCharacter)

#Change a cell that contains dual data to a data that comes after a delimeter

  def CleanDualData(ColumnName, Delimiter):
    df[ColumnName] = df[ColumnName].str.split(Delimiter).str[0]
  
  #Add Data After delimiter to a second column
    
  def AddDualDataToColumn(ColumnName, Delimiter):
    df[ColumnName + "_Second"] = df[ColumnName].str.split(Delimiter).str[1]
    
  def EliminateBadData(ColumnName, CharNo):
    for i in range(497):
      if(len(df.at[i,ColumnName]) != CharNo):
        df.at[i,ColumnName] = ""
        
  def EliminateStringFromInt(ColumnName):
    df['columnName'] = df['columnName'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)


FixCells('Phone_Number','09', '9')
FixCells('Phone_Number', '011', '11')
CleanDualData('Phone_Number', '/')

print(df)





