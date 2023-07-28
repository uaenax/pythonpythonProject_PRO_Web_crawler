'''
需求:用户输入当前目录下任意文件名，完成对该文件的备份功能(备份文件名为XX[备份]后缀，例如:(test[备份].txt)
1.命名变化: test.txt => 备份 => test[备份].txt
2.内容变化: 需要把旧文件中的内容完全拷贝到新文件中
分析:命名变化如何实现
test.txt => test[备份].txt ?
 提示用户输入要备份的文件名称
 分别获取文件的名称以及文件的后缀 =>(文件名 => test 后缀 => .txt)
 重新拼接新文件 test + [备份] + .txt
新方法:rfind()方法，从左向右查找，返回这个关键词在最后一次出现的位置
test.abc.txt
'''
oldname = input("请输入你要备份的文件名:")
index = oldname.rfind('.')
filename = oldname[:index]
postfix = oldname[index:]
newname = filename + '[备份]' + postfix
print(newname)

old_f = open(oldname, 'rb')
new_f = open(newname, 'wb')
while True:
    content = old_f.read(1024)
    if not content:
        break
    new_f.write(content)

old_f.close()
new_f.close()