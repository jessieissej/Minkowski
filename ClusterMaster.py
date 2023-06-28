import pandas as pd
import numpy as np
import time
from tqdm import tqdm

#Class for Clustering
class ClusterMaster:
    def __init__ (self, data):
        self.dataframe = data['dataframe']
        self.column_names = data['column_names']
        self.numberOfCluster = None
        self.kvalue = []
        self.x = None
        self.y = None
        self.p = None
        self.assignment = []
    
    #Method for setting number of clusters
    def set_number_of_cluster(self):
        self.numberOfCluster = input("Enter the number of cluster you want: ");
        self.numberOfCluster = pd.to_numeric(self.numberOfCluster)

    #Method for setting p value for Minkowski distance
    def set_p_value(self):
        self.p = input("Enter p value: ")
        self.p = pd.to_numeric(self.p)

    #Method for destructuring dataframe and passing its value to x,y,z properties
    def destructure_datafreame(self):
        self.x = self.dataframe[self.column_names['first_column']].to_numpy();
        self.y = self.dataframe[self.column_names['second_column']].to_numpy();

    #Method for initializing k value: Default is the first nth row in the dataset
    def initialize_kvalue(self):
        self.kvalue = [[] for _ in range(self.numberOfCluster)]

        for i in range (self.numberOfCluster):
            self.kvalue[i] = [self.x[i], self.y[i]]

        print("--------------Kvalues--------------------")
        print(self.kvalue)

    #Method for applying minowski distance equeation
    def apply_minkowski(self):

        row_length = len(self.x)
        distance = np.empty(self.numberOfCluster)
        nearest_distance = 0;

        #This first loop will loop each ROW in the dataset
        for i in tqdm(range (row_length)):
            print(f"\nInput x = {self.x[i]}\ty = {self.y[i]}")
            #In each row, loop number of clusters you set
            #This will check the distances from the given default centroid and choose which is the closest one
            for j in range (self.numberOfCluster):
                #On every loop call minkowski distance and pass the current row that is proccessing then the different centroids on each loop of "k"
                distance[j] = self.minowski_equation(self.x[i], self.y[i], self.kvalue[j], self.p);

                #This if else will chose the closest centroid to the given x,y,z of current row 
                if(j == 0):
                    nearest_distance = j
                else:
                    if(distance[j]< distance[nearest_distance]):
                        nearest_distance = j

                print(f"Distance from cluster{j+1}: {distance[j]}");
            print(f"Nearest Centroid: {nearest_distance + 1}")

            #On this part, depending on the chosen closest centroid, using the value of the given row, get their average and set it as new centroid
            self.kvalue[nearest_distance][0] = (self.kvalue[nearest_distance][0] + self.x[i]) / 2
            self.kvalue[nearest_distance][1] = (self.kvalue[nearest_distance][1] + self.y[i]) / 2

            #After assigning new centroid, assign the cluster where the row belongs
            self.assignment.append(nearest_distance + 1)

            for k in range (self.numberOfCluster):
                print(f"Centroid{k+1}: x = {self.kvalue[k][0]} \t y = {self.kvalue[k][1]}")
            #time.sleep(0.1)

    #This method will use minkowski distance using actual formula, not the library and will return the distance
    def minowski_equation(self, x1,y1, kvalue, p):
        distance = ((abs(kvalue[0] - x1) ** p) + (abs(kvalue[1] - y1) ** p)) ** (1 / p)
        return distance

    #This method will be use to retrieve the final output
    def get_result(self):
        self.dataframe = pd.DataFrame({self.column_names['first_column']: self.x, self.column_names['second_column']: self.y, "Assignment": self.assignment})
        print(self.dataframe)
        output = {
            "dataframe": self.dataframe,
            "column_names" : self.column_names
        }
        return output



    

    
    