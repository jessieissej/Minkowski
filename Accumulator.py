import pandas as pd

class Accumulator:
    def __init__(self, filename):
        self.file = filename
        self.dataframe = None
        self.result = None

    #Method for extracting data from csv and store to a dataframe
    def extract(self):
        self.dataframe = pd.read_csv(self.file, sep=';')
        print(self.dataframe)

    #Mothod for getting name of columns that will be use and store on its own variable
    #return name and new dataframe
    def select(self):
        variable1 = input("Name of column in dataframe for x : ")
        variable2 = input("Name of column in dataframe for y : ")
        print("\n")

        x = self.dataframe[variable1].to_numpy();
        y = self.dataframe[variable2].to_numpy();

        #combine selected column as dataframe and column name as object then assign to property result
        column_names = {
            'first_column': variable1,
            'second_column': variable2,
          
        }
        new_dataframe = pd.DataFrame({variable1: x, variable2: y})
        self.result = {
            'column_names': column_names,
            'dataframe': new_dataframe,
        }
    
    #Method for getting the result property
    def getResult(self):
        return self.result
        


        