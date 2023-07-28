class Tool(object):
    @staticmethod
    def menu():
        print('静态方法效果展示')


Tool.menu()
p1 = Tool()
p1.menu()
