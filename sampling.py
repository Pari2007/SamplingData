import pandas as pd
import statistics
import  csv
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go
# reading the file
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
# finding mean
population_mean = statistics.mean(data)
std_dev = statistics.stdev(data)

def randomSetOfMean(counter):
    dataset = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data))
        dataset.append(randomIndex)

    dataset_mean = statistics.mean(dataset)

    return dataset_mean

def showFigure(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["reading_time"],show_hist=False)
    # fig = fig.add_trace(go.scatter(x=[mean_list,mean_list], y =[0,1], mode ="lines"))
    fig.show()
   

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = randomSetOfMean(100)
        mean_list.append(set_of_mean)
    showFigure(mean_list)
    population_mean = statistics.mean(data)
    sampling_mean = statistics.mean(mean_list)
    print(population_mean,sampling_mean)
setup()









