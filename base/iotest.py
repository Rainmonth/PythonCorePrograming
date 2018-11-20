import pathlib


def printViaExpress(s):
    print(str(s))  # 返回一个用户易读的表达式形式
    print(repr(s))  # 返回一个解释器易读的表达形式，可以转移字符串中的特殊字符


def printViaPrint(s):
    print(s)


def useZfill(s):
    print(str(s).zfill(5))


def useStrFormat(siteName, siteUrl):
    print('{}的网址：{}'.format(siteName, siteUrl))


def useStrFormatWithOrder(siteUrl, siteName):
    print('{1}的网址：{0}'.format(siteUrl, siteName))


def printPowerTable():
    print("平方、立方表的打印方式（一）：")
    for x in range(1, 11):
        print(repr(x).rjust(2), repr(x * x).rjust(3), end=" ")
        print(repr(x * x * x).rjust(4))


def printPowerTable2():
    print("平方、立方表的打印方式（二）：")
    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))


# ------文件操作------
def isFileExist(filePath, fileName):
    """
    判断文件是否存在
    :param filePath:
    :param fileName:
    :return:
    """
    path = pathlib.Path(filePath + fileName)
    return path.exists()


def openFile(filePath, fileName, openMode):
    print("")
    if isFileExist(filePath + fileName):
        f = open(str(filePath) + str(fileName), openMode)
        return f
    else:
        return '文件不存在'


printViaExpress("hello world\n")

printPowerTable()
printPowerTable2()

useZfill(12)
useStrFormat('荏苒追寻', 'http:/rainmonth.cn')
useStrFormat('荏苒追寻', 'http:/rainmonth.cn')

# str = input("请输入字符串：")  # 'str' object is not callable，因为Python中存在str这个函数
# printViaExpress(str)
inputStr = input("请输入字符串：")
printViaExpress(inputStr)
