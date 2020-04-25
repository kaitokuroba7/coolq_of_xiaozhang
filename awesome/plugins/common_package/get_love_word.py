"""
该函数用以获得情话，并将其在本文中删除
"""

def get_love_word() -> str:
    """ 获取情话 """
    filepath = "python_files/coolq_of_xiaozhang/lover's prattle.txt"
    with open(filepath) as obj_file:
        lines = obj_file.readlines()
        love_word = lines[0]
        lines.pop(0)
        content = ''.join(lines)
    with open(filepath, 'w') as obj_file:
        obj_file.write(content)
    return love_word