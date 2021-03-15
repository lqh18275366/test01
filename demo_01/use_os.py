#系统包

'''
1. os模块
os.listdir(path)    返回指定的文件夹包含的文件或文件夹的名字的列表
os.path.isfile(path)	判断路径是否为文件
os.path.join(path1[, path2[, ...]])	把目录和文件名合成一个路径
os.path.split(path)	把路径分割成 dirname 和 basename，返回一个元组
'''
# 使用os模块中的一些常用方法
import os
# 查看当前路径下所有的文件和目录
print(os.listdir('.'))
# os.path.basename(path)	返回文件名
print(os.path.basename(r'e:\api_project\python_study02\demo_01\calc.py'))
# 分隔路径和文件名
print(os.path.split(r'e:\api_project\python_study02\demo_01\calc.py'))

'''
2.datetime模块
date 日期对象,常用的属性有year, month, day
time 时间对象
datetime 日期时间对象,常用的属性有hour, minute, second, microsecond
timedelta 时间间隔，即两个时间点之间的长度

'''

#导入datetime模块
from datetime import datetime
#strftime：对datetime对象进行格式化，生成需要时间格式的时间
now = datetime.now()
print(now)
df = now.strftime("%Y-%m-%d %H:%M:%S")
print(df)
dp1 = datetime.strptime(df, "%Y-%m-%d %H:%M:%S")
print(dp1)

print(datetime.strptime('2021-02-27 22:14:03',"%Y-%m-%d %H:%M:%S"))

'''
3. sys模块
sys模块提供了一系列有关Python运行环境的变量和函数。
sys.argv：可以用sys.argv获取当前正在执行的命令行参数的参数列表(list)。
sys.path:返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform:获取当前执行环境的平台，如win32表示是Windows系统，linux2表示是linux平台
'''

'''
4. 下载第三方包
#下载包 : pip install 包名 
#查看包 : pip show 包名 
#有的包有时候下载慢或无法下载，可以指定国内镜像 : pip install 包名 -i http://pypi.douban.com/simple/
'''

