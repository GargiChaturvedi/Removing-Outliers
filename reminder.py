import csv
import plotly.graph_objects as go
import statistics
import numpy
import seaborn as sb
import pandas

with open('savings_data_final.csv', 'r') as f:
    df = csv.reader(f)
    savings_data = list(df)

savings_data.pop(0)

totalEntries = len(savings_data)
reminded = 0

for data in savings_data:
    if int(data[3]) == 1:
        reminded += 1

fig = go.Figure(go.Bar(x=['Reminded', 'Not Reminded'], y=[reminded, (totalEntries-reminded)], marker=dict(color=['tomato', 'hotpink'])))
fig.show()

allSavings = []

for entry in savings_data:
    allSavings.append(float(entry[0]))

allSavings.pop(0)

mean = statistics.mean(allSavings)
median = statistics.median(allSavings)
mode = statistics.mode(allSavings)

print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)

remindedSavings = []
notRemindedSavings = []

for i in savings_data:
    if i[3] == '1':
        remindedSavings.append(float(i[0]))
    else :
        notRemindedSavings.append(float(i[0]))

remindedMean = statistics.mean(remindedSavings)
remindedMedian = statistics.median(remindedSavings)
remindedMode = statistics.mode(remindedSavings)

notRemindedMean = statistics.mean(notRemindedSavings)
notRemindedMedian = statistics.median(notRemindedSavings)
notRemindedMode = statistics.mode(notRemindedSavings)

print("\nReminded: ")
print("Mean: ", remindedMean)
print("Median: ", remindedMedian)
print("Mode: ", remindedMode)

print("\nNot Reminded: ")
print("Mean: ", notRemindedMean)
print("Median: ", notRemindedMedian)
print("Mode: ", notRemindedMode)

remindedStDev = statistics.stdev(remindedSavings)
notRemindedStDev = statistics.stdev(notRemindedSavings)
allStDev = statistics.stdev(allSavings)

age = []
savings = []

for point in savings_data:
    if float(point[5]) != 0:
        age.append(float(point[5]))
        savings.append(float(point[0]))

correlation = numpy.corrcoef(age, savings)
print("Correlation b/w age and savings: ", correlation[0, 1])

df = pandas.read_csv('savings_data_final.csv')

#sb.boxplot(data=df, x=df['quant_saved'])

q1 = df['quant_saved'].quantile(0.25)
q3 = df['quant_saved'].quantile(0.75)

iqr = q3 - q1
lower_whisker = q1 - (1.5 * iqr)
upper_whisker = q3 + (1.5 * iqr)

print("Q1: ", q1)
print("Q2: ", q3)
print("LW: ", lower_whisker)
print("UW: ", upper_whisker)

new_df = df[df['quant_saved'] < upper_whisker]

