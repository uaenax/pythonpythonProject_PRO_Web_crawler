'''
① 显示功能界面
② 提示用户输入要操作的功能编号
③ 根据用户输入的序号执行相关功能 => if...elif...else
④ 如何让程序一直执行下去，而不是选择某个功能后，程序就退出了 => while True
⑤ 根据用户输入的序号，完成系统中的每一个功能
⑥ 扩展功能：把学生信息保存在文件中
'''


# 1.显示功能界面
def show():
    print('-' * 40)
    print('学生管理系统 V1.0')
    print('[1] 添加学生信息')
    print('[2] 删除学生信息')
    print('[3] 修改学生信息')
    print('[4] 查询学生信息')
    print('[5] 遍历所有学生信息')
    print('[6] 保存数据到文件')
    print('[7] 退出系统')
    print('-' * 40)


lines = []


#  2.添加学生信息
def add_infor():
    dict = {'name': input('请输入学生姓名:'), 'age': int(input('请输入学生年纪:')), 'mobile': int(input('请输入学生手机号码:'))}
    global lines
    lines.append(dict)
    # print(lines)


#  3.删除学生信息
def del_infor():
    index = input('请输入需要删除的学生姓名:')
    for i in lines:
        if i['name'] == index:
            lines.remove(i)
            break
    else:
        print('查询学生不存在')
    # print(lines)


# 4.修改学生信息
def mode_info():
    info = input('请输入需要修改学生的姓名:')
    for i in lines:
        if i['name'] == info:
            i['name'] = info
            i['age'] = int(input('请输入学生新年纪:'))
            i['mobile'] = int(input('请输入学生新手机号码:'))
            break
    else:
        print('查询学生不存在')
    print(lines)


# 5.查询学生信息
def find_infor():
    info = input('请输入需要查询学生的姓名:')
    for i in lines:
        if i['name'] == info:
            print(i)
            break
    else:
        print('查询学生不存在')


# 6.遍历所有学生信息
def renge_infor():
    for i in lines:
        print(i)


# 7.保存数据到文件
def write_infor():
    file = open('student.txt', 'a', encoding='utf-8')
    file.write(str(lines))
    file.close()


# 8.读取文件数据
def load_data():
    flie = open('student.txt', 'r', encoding='utf-8')
    global lines
    lines = eval(flie.read())
    flie.close()


load_data()
#  2.让程序一直运行
while True:
    show()
    user_input = input("请输入功能序号:")
    if user_input == '1':  # 添加学生信息
        add_infor()
    elif user_input == '2':  # 删除学生信息
        del_infor()
    elif user_input == '3':  # 修改学生信息
        mode_info()
    elif user_input == '4':  # 查询学生信息
        find_infor()
    elif user_input == '5':  # 遍历所有学生信息
        renge_infor()
    elif user_input == '6':  # 保存数据到文件
        write_infor()
    elif user_input == '7':  # 退出程序
        print('程序安全退出')
        break
