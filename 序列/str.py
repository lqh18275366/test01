#str的定义
a = "idjekmvlsjwma"
#字符串格式化%s
print("我的名字叫：%s"%"李桥红")
print("他的年龄是%d" % 25)
print("他今天花了%.2f钱" % 238.9)

#使用format进行格式：format（）
print("我的名字叫：{}".format("李桥红"))
print("他的年龄是：{}".format(25))
print("他今天花了{}钱".format(300))

print("我的名字：{}，年龄{}，现居城市：{}".format('李桥红',25,"北京"))
print("***"+"==="*20+"format()")
#位置参数：format（0,1,2，……）
print("我的名字：{0}，年龄{1}，现居城市：{2}".format('李桥红',25,"北京"))
print("我的名字：{1}，年龄{0}，现居城市：{2}".format('李桥红',25,"北京"))
print("***"+"==="*20+"位置参数")
#关键字参数：可更换位置
print("我的名字：{x}，年龄{y}，现居城市：{z}".format(x='李桥红',y=25,z="北京"))
print("我的名字：{x}，年龄{y}，现居城市：{z}".format(y=25,z="北京",x='李桥红'))
print("***"+"==="*20+"关键字参数")

#关键字参数和位置参数组合使用：位置参数必须放在关键字前面
print("我的名字：{0}，年龄{y}，现居城市：{1}".format('李桥红',"北京",y=25))
print("***"+"==="*20+"关键字参数+位置参数")