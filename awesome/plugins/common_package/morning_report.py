import numpy as np
import matplotlib.pyplot as plt
import datetime


def plot_morning_get_up():

    filepath = "python_files/coolq_of_xiaozhang/database/get_up_time.txt"
    filepath_of_xiaozhang = "python_files/coolq_of_xiaozhang/database/get_up_time_of_xiaozhang.txt"
    with open(filepath) as obj_file:
        contents = obj_file.readlines()
        y_axis_wang = []
        x_axis = ['0']
        y_axis_label = []
        for i in range(len(contents)):
            content = contents[i].split()
            y_axis_wang.append(int(content[2] + content[3]))
            y_axis_label.append(str(content[2] + ':' + content[3]))
            x_axis.append(str(content[0] + '-' + content[1]))
    with open(filepath_of_xiaozhang) as obj_file:
        contents = obj_file.readlines()
        y_axis_zhang = []
        y_axis_label_zhang = []
        for i in range(len(contents)):
            content = contents[i].split()
            y_axis_zhang.append(int(content[2] + content[3]))
            y_axis_label_zhang.append(str(content[2] + ':' + content[3]))
    # 画图
    x = np.arange(len(x_axis)-1)  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, y_axis_wang, width, label='小王')
    rects2 = ax.bar(x + width/2, y_axis_zhang, width, label='小张')
    ax.set_ylim([600, 1200])
    ax.set_yticks([600, 700, 800, 900, 1000, 1100, 1200])
    ax.set_yticklabels(['6:00','7:00', '8:00', '9:00', '9:00', '10:00', '11:00', '12:00'])
    ax.set_xticklabels(x_axis)
    ax.set_ylabel('起床时间')
    ax.set_xlabel('日期')
    ax.set_title("小王和小张的起床时间统计图 \n来自饺子的搜集以及小张的编程")
    ax.legend()

    def autolabel(rects, label):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for i, rect in enumerate(rects):
            height = label[i]
            print(height)
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, rect.get_height()),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1, y_axis_label)
    autolabel(rects2, y_axis_label_zhang)
    fig.tight_layout()
    day = datetime.datetime.now()
    plt.savefig('../my_coolq/data/image/%s.png' % str(day.date()))

