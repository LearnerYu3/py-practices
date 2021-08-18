import matplotlib.pyplot as plt
import matplotlib


# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c='r', s=3)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=5)

# 保证中文标签正确显示，但要在创建图形对象后
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']

# 设置图表标题并给坐标轴加上标签
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)
ax.axis([0, 1100, 0, 1100000])

# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)

# 不能放在 plt.show() 之后，会得到空白图片
plt.savefig('scatter.png', bbox_inches='tight')
plt.show()
