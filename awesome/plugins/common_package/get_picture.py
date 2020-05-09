import os
import re
import random
def get_pic_of_iamge(keyword=r'^\d+.jpg'):
    """ 获得特定的图片，返回一个列表，列表为图片的名字 """
    filepath = '/my_coolq/data/image/'
    filename = os.listdir(filepath)
    keywordRegex = re.compile(r'%s' %keyword)
    key_pics = []
    for i in range(len(filename)):
        key_pic = keywordRegex.search(filename[i])
        if key_pic:
            key_pics.append(filename[i])

    num = random.randint(0, len(key_pics)-1)
    pic_name = key_pics[num]
    return pic_name