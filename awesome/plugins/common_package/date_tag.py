"""
有关于时间的函数
"""
import datetime


def get_time_tag(filepath: str) -> str:
    " 获取当日的时间 "
    # filepath = "python_files/coolq_of_xiaozhang/database/date.txt"
    with open(filepath) as obj_file:
        content = obj_file.read()
    return content.strip()

def write_time_tag(filepath: str) -> str:
    " 写入当日的时间 "
    # filepath = "python_files/coolq_of_xiaozhang/database/date.txt"
    with open(filepath,'w') as obj_file:
        day = datetime.datetime.now()
        obj_file.write(str(day.date()))

def write_get_up_time(filepath: str) -> str:
    " 把起床时间写入到文件中 "
    # filepath = "python_files/coolq_of_xiaozhang/database/get_up_time.txt"
    with open(filepath,'a') as obj_file:
        day = datetime.datetime.now()
        obj_file.write('\n'+str(day.month)+' '+str(day.day)+' '+str(day.hour)+' '+str(day.minute))

