import plotly.graph_objs as go

class Mapper:
    def __init__(self, output):
        self.dataframe = output["dataframe"]
        self.column_names = output["column_names"]
        self.x = None
        self.y = None
        self.z = None
        self.a = None
        self.a = None
    
    def destructure_dataframe(self):
        self.x = self.dataframe[self.column_names['first_column']].to_numpy();
        self.y = self.dataframe[self.column_names['second_column']].to_numpy();
        self.z = self.dataframe[self.column_names['third_column']].to_numpy();
        self.a = self.dataframe["Assignment"].to_numpy();
        self.a = self.a.astype(int)

    def map_3d(self):
        
        #Color coding depending on the assignment
        color_mapping = {
            1: 'rgb(31, 119, 180)',  # Steel Blue
            2: 'rgb(255, 127, 14)',  # Orange
            3: 'rgb(44, 160, 44)',   # Lime Green
            4: 'rgb(214, 39, 40)',   # Crimson
            5: 'rgb(148, 103, 189)', # Medium Purple
            6: 'rgb(140, 86, 75)',   # Copper
            7: 'rgb(227, 119, 194)', # Pink
            8: 'rgb(127, 127, 127)', # Gray
            9: 'rgb(188, 189, 34)',  # Olive
            10: 'rgb(23, 190, 207)'  # Turquoise
        }


        color = [color_mapping[Assingment] for Assingment in self.a]
        trace = go.Scatter3d(
            x=self.x,
            y=self.y,
            z=self.z,
            mode='markers',
            marker=dict(
                size=8,
                color=color,
                colorscale='Viridis',
                opacity=0.8
            )
        )

        layout = go.Layout(
            title = '3D Scatter Plot (' + self.column_names['first_column'] + ' vs ' + self.column_names['second_column'] + ' vs ' + self.column_names['third_column'] + ')',
            scene=dict(
                xaxis=dict(title=self.column_names['first_column']),
                yaxis=dict(title=self.column_names['second_column']),
                zaxis=dict(title=self.column_names['third_column'])
            )
        )

        fig = go.Figure(data=[trace], layout=layout)
        fig.write_html('plot.html')


    



        