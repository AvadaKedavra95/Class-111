import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()

mean=statistics.mean(data)
std_deviation=statistics.stdev(data)

print("The Mean is : ",mean)
print("The Standard Deviation is : ",std_deviation)

def random_set_of_mean(counter):
    dataset=[]
    for x in range(counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    
    mean=statistics.mean(dataset)
    return(mean)

mean_list=[]
for i in range(1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)

std_deviation = statistics.stdev(mean_list)
mean=statistics.mean(mean_list)

fig=ff.create_distplot([mean_list],["Math Score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="MEAN"))
fig.show()

print("The Mean of sampling distribution is : ", mean)
print("The Standard Deviation of sampling distribution is : ", std_deviation)
