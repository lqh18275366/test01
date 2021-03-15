# # 将两次循环的值连接起来放在列表中
# print([y+str(x) for x in range(1,3) for y in 'abc'])
#
# # 等同于双循环
# a = [3,4,5]
# b = ['h','j','l']
# lst = []
# for x in a:
#     print(lst)
#     for y in b:
#         print(lst)
#         lst.append(y+str(x))
# print(lst)



a = [3,4,5]
b = ['h','j','l']
c = []
for x in a:
    print(x)
    for y in b:
        print(y)
        print(c)
        c.append(y + str(x))
print(c)

a = 'abc'
b = '123'
c = []
for x in a:
    #print(x)
    for y in b:
        #print(y)
        print(x+str(y))
        c.append(str(x)+y)
print(c)