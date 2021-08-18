import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')
    # fig, ax = plt.subplots(figsize=(8, 5), dpi=128)
    fig, ax = plt.subplots()

    points = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=points, cmap=plt.cm.Blues,
               edgecolors='none', s=10)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='r',
               edgecolors='none', s=25)
    ax.scatter(0, 0, c='green', edgecolors='none', s=25)
    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
