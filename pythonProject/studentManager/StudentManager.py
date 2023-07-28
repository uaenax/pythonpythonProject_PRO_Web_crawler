from studentManager.Student import Student


class StudentManager(object):
    # 初始化将学员信息储存在列表中
    def __init__(self):
        self.student_list = []

    # 定义静态方法打印系统功能选项
    @staticmethod
    def menu():
        print('-' * 40)
        print('欢迎进入学员管理系统!')
        print('[1]添加学员')
        print('[2]删除学员')
        print('[3]修改学员')
        print('[4]查询学员')
        print('[5]显示所有学员')
        print('[6]保存学员信息')
        print('[7]退出系统')
        print('-' * 40)

    #  从文件中加载学员信息
    def load_student(self):
        f = open('student.data', 'r', encoding='utf-8')
        student = f.read()
        if not student:
            student = '[]'
        # 将文件中字典形式的数据转换成原格式(列表)
        data = eval(student)
        self.student_list = [Student(i['name'], i['age'], i['mobile']) for i in data]

    #  添加学员信息 add_student()
    def add_student(self):
        name = input('请输入学员姓名:')
        age = int(input('请输入学员年纪:'))
        mobile = input('请输入学员手机号:')
        student = Student(name, age, mobile)
        self.student_list.append(student)
        print('学员信息已经添加成功')

    #  删除学员信息
    def del_student(self):
        name = input('请输入需要删除的学员姓名:')
        for i in self.student_list:
            if i.name == name:
                self.student_list.remove(i)
                print(f'学员{name}已经删除成功')
                break
        else:
            print('您要删除的学员不存在!')

    #  修改学员信息
    def mod_student(self):
        name = input('请输入需要修改的学员姓名:')
        for i in self.student_list:
            if i.name == name:
                new_name = input('请输入需要修改的学员新姓名:')
                new_age = int(input('请输入需要修改的学员新年纪:'))
                new_mobile = input('请输入需要修改的学员新手机号:')
                i.name = new_name
                i.age = new_age
                i.mobile = new_mobile
                print(f'学员{name}已经修改成功')
                break
        else:
            print('您要修改的学员不存在!')

    #  查询学员信息
    def show_student(self):
        name = input('请输入需要查询的学员姓名:')
        for i in self.student_list:
            if i.name == name:
                print(i)
                break
        else:
            print('您要查询的学员不存在!')

    #  显示所有学员信息
    def show_all(self):
        for i in self.student_list:
            print(i)

    #  保存学员信息
    def save_student(self):
        #  打开文件
        f = open('student.data', 'w', encoding='utf-8')
        #  把学员实例对象组成一个新列表
        # 使用__dict__魔术方法将列表数据转换成字典形式
        new_list = [i.__dict__ for i in self.student_list]
        #  读写文件
        f.write(str(new_list))
        #  关闭文件
        f.close()
        

    # 定义一个启动程序
    def run(self):
        #  加载本地文件
        self.load_student()
        #  循环程序
        while True:
            # 展示系统提示
            self.menu()
            # 用户进行系统选择
            user = int(input('请输入您要选择的功能:'))
            if user == 1:
                # 添加学员信息
                self.add_student()
            elif user == 2:
                # 删除学员信息
                self.del_student()
            elif user == 3:
                # 修改学员信息
                self.mod_student()
            elif user == 4:
                # 查询学员信息
                self.show_student()
            elif user == 5:
                # 显示所有学员信息
                self.show_all()
            elif user == 6:
                # 保存学员信息
                self.save_student()
            elif user == 7:
                print('退出系统成功!')
                break
            else:
                print('您选择的功能尚未开发,请重新选择!')
