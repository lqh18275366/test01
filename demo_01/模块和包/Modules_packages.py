#1.通过import 导入 ： import 文件名
from demo_01.模块和包 import Modules_packages_calcs

#使用导入文件（calc）：c1 = 文件名.类名
print(Modules_packages_calcs.add(4, 9))


#2. 通过from  ... import : from 包名 import 类名|函数|方法
from demo_01.模块和包.Modules_packages_calcs import add
#使用导入文件（calc）：c1 = 类名
print(add(3,4))