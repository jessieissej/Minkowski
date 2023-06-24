import pandas as pd
import numpy as np
from Accumulator import Accumulator
from Cleaner import Cleaner
from ClusterMaster import ClusterMaster
from Mapper import Mapper

filename = input("Enter the file name: ")

#Create an instance of class - clasa for data aquisition
accumulator = Accumulator(filename)
accumulator.extract()
accumulator.select()
data = accumulator.getResult()

#Create an instance of cleaner object - class for cleaning and data preperation
cleaner = Cleaner(data)
cleaner.remove_first_index()
cleaner.convert_dataframe_to_numeric()
cleaner.remove_null()
data = cleaner.getCleanedDataFrame()

#Create a instance of clustermaster - class for clustering
clustermaster = ClusterMaster(data)
clustermaster.set_number_of_cluster()
clustermaster.set_p_value()
clustermaster.destructure_datafreame()
clustermaster.initialize_kvalue()
clustermaster.apply_minkowski()
output = clustermaster.get_result()

#Instance of class for Mapping of output
mapper = Mapper(output)
mapper.destructure_dataframe()
mapper.map_3d()



