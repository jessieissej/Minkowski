import pandas as pd

class Cleaner:
    def __init__(self, data):
        self.dataframe = data['dataframe']
        self.column_names = data['column_names']

    #Method for removing first element which containes data type of cloumn data
    def remove_first_index(self):
        #destructure the dataframe to individual column
        x = self.dataframe[self.column_names['first_column']].to_numpy();
        y = self.dataframe[self.column_names['second_column']].to_numpy();
        z = self.dataframe[self.column_names['third_column']].to_numpy();

        #Remove first element in each column Ex."DOUBLE", "INT"
        x = x[1:]
        y = y[1:]
        z = z[1:]
        #Recombine column into a dataframe
        self.dataframe = pd.DataFrame({self.column_names['first_column']: x, self.column_names['second_column']: y, self.column_names['third_column']: z})
        print(self.dataframe);

    #Method for converting data on each column to numeric value
    def convert_dataframe_to_numeric(self):
        #Destructure dataframe into individual columns
        x = self.dataframe[self.column_names['first_column']].to_numpy();
        y = self.dataframe[self.column_names['second_column']].to_numpy();
        z = self.dataframe[self.column_names['third_column']].to_numpy();

        #Convert each data to numeric, non-numeric data will be "Nan" value
        x = pd.to_numeric(x, errors='coerce')
        y = pd.to_numeric(y, errors='coerce')
        z = pd.to_numeric(z, errors='coerce')

        #Recombine cloumns into a dataframe
        self.dataframe = pd.DataFrame({self.column_names['first_column']: x, self.column_names['second_column']: y, self.column_names['third_column']: z})

    #Method for removing null and Nan values
    def remove_null(self):
        self.dataframe.dropna(inplace=True)
        print("____________Remove Null Values_____________")
        print(self.dataframe)

    #Method for returning the cleaned dataframe along with column names that will be user for entire process
    def getCleanedDataFrame(self):
        result = {
            'dataframe' : self.dataframe,
            'column_names': self.column_names,
        }
        return result
        