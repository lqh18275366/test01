#1. 文件读写步骤：使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。
# (1) 读取文件：a.txt 内容
    # ①. 需要打开文件:open()
    # 生成一个对象：r
r = open('read.txt','r')
    # ②. 使用对象f读取read.txt文件并打印文件内容: f.read()
print("读取文件read.txt的内容:\n",r.read())
    # ③. 关闭文件 :close()
r.close()

# (2) 编辑write.txt文件
    # ①. 需要打开文件:open()
w = open('write.txt','w')
    # ②. 使用对象w编辑write.txt文件并打印文件内容: f.write()
w.write('python java')

# (3) 关闭文件 :close()
w.close()

# 2.File(文件)方法使用
"""
readline() 方法语法格式：
    fileObject.readline([size]); 
        size -- 从文件中读取的字节数。
    返回值：从字符串中读取的字节。
"""
# 打开文件:
# (1) 使用open()方法
rl = open("readline.txt", "rb+")
print ("打开文件名为: ", rl.name)
i = 1
while i < 8:
    line = rl.readline()
    print("读取第{}行内容{}" .format(i,line))
    i = i + 1

# (2) 使用with进行读取文件
# 格式 ： with open(f,'r') as f
with open('a.txt','r') as f:
    all_lines = f.readlines()
    for x in all_lines:
        print(x)

"""
file.seek() 方法语法格式：
    fileObject.seek(offset,[ whence])
        offset -- 开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始。
        whence：可选，默认值为 0。给 offset 定义一个参数，表示要从哪个位置开始偏移；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。
    返回值: 如果操作成功，则返回新的文件位置，如果操作失败，则函数返回 -1。
"""
rl.seek(4, 0)  # 从头开始，偏移4个字节
position = rl.tell()
line = rl.readline(7)
print("当前位置{},读取内容{}".format(position,line))

rl.seek(4, 1)  # 从当前位置开始，偏移4个字节
line = rl.readline(5)
print("当前位置{},读取内容{}".format(position,line))

rl.seek(-4, 2)
line = rl.readline(3)
print("当前位置{},读取内容{}".format(position,line))
# 关闭文件
rl.close()

# 通过with进行读取文件后自动关闭该文件

# 格式 ： with open(f,'r') as f

with open('a.txt','r') as f:
    all_lines = f.readlines()
    for x in all_lines:
        print(x)