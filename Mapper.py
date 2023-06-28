import plotly.graph_objs as go
import matplotlib.pyplot as plt

class Mapper:
    def __init__(self, output):
        self.dataframe = output["dataframe"]
        self.column_names = output["column_names"]
        self.x = None
        self.y = None
        self.a = None
    
    def map(self):
        self.x = self.dataframe[self.column_names['first_column']].to_numpy();
        self.y = self.dataframe[self.column_names['second_column']].to_numpy();
        self.a = self.dataframe["Assignment"].to_numpy();
        self.a = self.a.astype(int)
                            #1      #2      #3         #4       #5          #6
        colors = ['white', 'red', 'green', 'blue', 'orange', 'yellow', 'violet']
        cluster_colors = [colors[Assignment] for Assignment in self.a]

        # Plot the scatter plot with colored clusters
        plt.scatter(self.x, self.y, c=cluster_colors)

        # Set labels and title
        plt.xlabel(self.column_names['first_column'])
        plt.ylabel(self.column_names['second_column'])
        plt.title('Scatter Plot ( '+ self.column_names['first_column'] +" vs " + self.column_names['second_column']+" )")

        # Show the plot
        plt.show()
   