import matplotlib.pyplot as plt
import datetime

def plot_morning_get_up():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # 有中文出现的情况，需要u'内容'

    filepath = "python_files/coolq_of_xiaozhang/database/get_up_time.txt"

    with open(filepath) as obj_file:
        contents = obj_file.readlines()
        y_axis = []
        x_axis = []
        y_axis_label = []
        for i in range(len(contents)):
            content = contents[i].split()
            y_axis.append(int(content[2] + content[3]))
            y_axis_label.append(str(content[2] + ':' + content[3]))
            x_axis.append(str(content[0] + '-' + content[1]))
            print(y_axis)
    width = 0.6
    fig, ax = plt.subplots()
    rects1 = ax.bar(x_axis, y_axis, width, label='小王')
    ax.set_ylim([700, 1200])
    ax.set_yticks([700, 800, 900, 1000, 1100, 1200])
    ax.set_yticklabels(['7:00', '8:00', '9:00', '10:00', '11:00', '12:00'])
    ax.set_ylabel('起床时间')
    ax.set_xlabel('日期')
    ax.set_title("小王的起床时间统计图 \n来自饺子的搜集以及小张的编程")
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
    fig.tight_layout()
    autolabel(rects1, y_axis_label)
    day = datetime.datetime.now()
    plt.savefig('../my_coolq/data/image/%s.png' % str(day.date()))
