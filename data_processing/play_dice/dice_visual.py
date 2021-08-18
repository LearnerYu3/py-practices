from plotly.graph_objs import Bar, Layout
from plotly import offline
from dice import Dice


dice = Dice()

results = []
nums = 1000
for roll_num in range(nums):
    result = dice.roll()
    results.append(result)

frequencies = []
for value in range(1, dice.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_value = list(range(1, dice.num_sides+1))
data = [Bar(x=x_value, y=frequencies)]

x_axis_config = {'title': '结果'}
y_axis_config = {'title': "结果的频率"}
my_layout = Layout(title=f'掷{nums}的结果', xaxis=x_axis_config,
                   yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
