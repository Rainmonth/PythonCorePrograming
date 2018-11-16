# -*- coding: UTF-8 -*-
import re


def is_valid_mobile(mobile_num):
    """
    是否是有效的手机号
    先要知道三大运营商手机号的规则：
    中国电信：133、149、153、173、177、180、181、189、199
    中国联通：130、131、132、145、155、156、166、175、176、185、186
    中国移动：134(0-8)、135、136、137、138、139、147、150、151、152、157、158、159、172、178、182、183、184、187、188、198

    其他号段
    14号段以前为上网卡专属号段，如中国联通的是145，中国移动的是147等等。

    虚拟运营商
    电信：1700、1701、1702
    移动：1703、1705、1706
    联通：1704、1707、1708、1709、171
    卫星通信：1349
    :param mobile_num
    :return:
    """
    mobile = '^134[0-8]\d{7}|(13[5-9]|147|15[0-2,7-9]|178|18[2-4,7-8]|198)\d{8}|170[3,5,6]\d{7}$'
    mobile_re = '^134[0-8]\d{7}|(13[5-9]|147|15[0-2,7-9]|178|18[2-4,7-8]|198)\d{8}$'
    mobile_virtual_re = '^170[3,5,6]\d{7}$'

    tele = '^(133|149|153|173|177|180|181|189|199)\d{8}|170[0,1,2]\d{7}$'
    telecome_re = '^(133|149|153|173|177|180|181|189|199)\d{8}$'
    telecome_virtual_re = '^170[0,1,2]\d{7}$'

    unicom = '^(13[0-2]|145|155|156|166|17[5-6]|18[5-6])\d{8}|171\d{8}|170[4,7-9]\d{7}$'
    unicom_re = '^(13[0-2]|145|155|156|166|17[5-6]|18[5-6])\d{8}$'
    unicom_virtaul_re = '^171\d{8}|170[4,7-9]\d{7}$'

    satellite = "^1349\d{7}$"

    if re.match(mobile, mobile_num):
        if re.match(mobile_re, mobile_num):
            print('中国移动号码')
        elif re.match(mobile_virtual_re, mobile_num):
            print('中国移动虚拟运营商号码')
        return True
    elif re.match(tele, mobile_num):
        if re.match(telecome_re, mobile_num):
            print('中国电信号码')
        elif re.match(telecome_virtual_re, mobile_num):
            print('中国电信虚拟运营商号码')
        return True
    elif re.match(unicom, mobile_num):
        if re.match(unicom_re, mobile_num):
            print('中国联通号码')
        elif re.match(unicom_virtaul_re, mobile_num):
            print('中国联通虚拟运营商号码')
        return True
    elif re.match(satellite, mobile_num):
        print('卫星电话')
        return True
    else:
        print('不是有效手机号码')
        return False


def is_valid_email(email_str):
    """
    邮箱地址规则：
    1、前半部分由字母、数字、下划线和点组成且不能以点开头
    2、中间为@
    3、后半部分
    @ 后半部分由字母、数据和点组成
    :param email_str
    :return:
    """
    email_pattern = '^[0-9a-zA-Z_-]+(\.[a-zA-Z0-9_-]+)*@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'
    if re.match(email_pattern, email_str):
        print("正确的邮箱地址")
        return True
    else:
        print("错误的邮箱地址")
        return False


errors = ['验证通过！', '身份证号码位数不对', '身份证出身日期不对', '含有非法字符', '身份证校验错误', '身份证地区错误']


def is_valid_id_num(id_num):
    """
    身份证介绍 https://baike.baidu.com/item/%E5%B1%85%E6%B0%91%E8%BA%AB%E4%BB%BD%E8%AF%81%E5%8F%B7%E7%A0%81/3400358?fr=aladdin
    是否是有效的身份证号码
    1. 位数是否正确
    2. 第一代身份证校验（15位）15位身份证号码各位的含义:
        1-2：    位省、自治区、直辖市代码；
        3-4：    位地级市、盟、自治州代码；
        5-6：    位县、县级市、区代码；
        7-12：   位出生年月日,比如670401代表1967年4月1日；
        13-15：  位为顺序号，其中15位男为单数，女为双数；
    与18位区别：
        1. 日期的表示采用6位而不是8位
        2. 没有最后一位的验证码。
    3. 第二代身份证校验
        号码的结构
            公民身份号码是特征组合码，由十七位数字本体码和一位校验码组成。排列顺序从左至右依次为：六位数字地址码，八位数字出生日期码，
            三位数字顺序码和一位数字校验码。
        地址码
            表示编码对象常住户口所在县（市、旗、区）的行政区划代码，按GB/T2260的规定执行。
        出生日期码
            表示编码对象出生的年、月、日，按GB/T7408的规定执行，年、月、日代码之间不用分隔符。
        顺序码
            表示在同一地址码所标识的区域范围内，对同年、同月、同日出生的人编定的顺序号，顺序码的奇数分配给男性，偶数分配给女性。
        校验码
            根据前面十七位数字码，按照ISO 7064:1983.MOD 11-2校验码计算出来的检验码。

    具体编码规则如下：
        地址码
            中国大陆居民身份证号码中的地址码的数字编码规则为：
            第一、二位表示省（自治区、直辖市、特别行政区）。
            第三、四位表示市（地级市、自治州、盟及国家直辖市所属市辖区和县的汇总码）。其中：
                01-20，51-70表示省直辖市；
                21-50表示地区（自治州、盟）。
            第五、六位表示县（市辖区、县级市、旗）。其中：
                01-18表示市辖区或地区（自治州、盟）辖县级市；
                21-80表示县（旗）；
                81-99表示省直辖县级市。
        生日期码
            身份证号码第七位到第十四位，表示编码对象出生的年、月、日，其中年份用四位数字表示，年、月、日之间不用分隔符。例如：
                1981年05月11日就用19810511表示。
        顺序码
            身份证号码第十五位到十七位，地址码所标识的区域范围内，对同年、月、日出生的人员编定的顺序号。其中：
                第十七位奇数分给男性，偶数分给女性。
        校验码
            作为尾号的校验码，是由号码编制单位按统一的公式计算出来的，如果某人的尾号是0-9，都不会出现X，但如果尾号是10，那么就得用X来代
            替，因为如果用10做尾号，那么此人的身份证就变成了19位，而19位的号码违反了国家标准，并且中国的计算机应用系统也不承认19位的身份
            证号码。Ⅹ是罗马数字的10，用X来代替10，可以保证公民的身份证符合国家标准。
    :param id_num:
    :return:
    """

    id_num = str(id_num)
    id_num = id_num.strip()
    print('待校验的身份证号为：' + id_num)
    # 非法字符校验
    id_re = '^\d{15}|\d{17}[0-9X]$'
    if re.match(id_re, id_num):
        pass
    else:
        print(errors[3])
        return False
    if len(id_num) == 18:
        # 处理18位身份证号码
        if check_address_num(id_num) \
                and check_birthday_num(id_num) \
                and check_verify_num(id_num):
            print(id_num + '为第二代身份证')
            return True
        else:
            return False
    elif len(id_num) == 15:
        # 处理15位身份证号码
        if check_address_num(id_num) \
                and check_birthday_num(id_num):
            print('第一代身份证')
            return True
        else:
            return False
    else:
        print(errors[1])
        return False


def check_address_num(id_num):
    provinces = {
        # 华北地区（5个）：北京市|110000，天津市|120000，河北省|130000，山西省|140000，内蒙古自治区|150000
        '11': '北京市', '12': '天津市', '13': '河北省', '14': '山西省', '15': '内蒙古自治区',
        # 东北地区（3个）：辽宁省|210000，吉林省|220000，黑龙江省|230000
        '21': '辽宁省', '22': '吉林省', '23': '黑龙江省',
        # 华东地区（7个）：上海市|310000，江苏省|320000，浙江省|330000，安徽省|340000，福建省|350000，江西省|360000，山东省|370000
        '31': '上海市', '32': '江苏省', '33': '浙江省', '34': '安徽省', '35': '福建省', '36': '江西省', '37': '山东省',
        # 华中地区（3个）：河南省|410000，湖北省|420000，湖南省|430000
        '41': '河南省', '42': '湖北省', '43': '湖南省',
        # 华南地区（3个）：广东省|440000，广西壮族自治区|450000，海南省|460000，
        '44': '广东省', '45': '广西壮族自治区', '46': '海南省',
        # 西南地区（5个）：四川省|510000，贵州省|520000，云南省|530000，西藏自治区|540000，重庆市|500000，
        '51': '四川省', '52': '贵州省', '53': '云南省', '54': '西藏自治区', '50': '重庆市',
        # 西北地区（5个）：陕西省|610000，甘肃省|620000，青海省|630000，宁夏回族自治区|640000，新疆维吾尔自治区|650000，
        '61': '陕西省', '62': '甘肃省', '63': '青海省', '64': '宁夏回族自治区', '65': '新疆维吾尔自治区',
        # 特别地区（3个）：台湾地区(886)|710000，香港特别行政区（852)|810000，澳门特别行政区（853)|820000
        '71': '台湾省', '81': '香港特别行政区', '82': '澳门特别行政区'

    }
    id_num = str(id_num).strip()
    address_num = id_num[0:2]
    print('待校验的地址代码为：' + address_num)
    if address_num in provinces.keys():
        print('地址代码：' + str(address_num) + '对应省(直辖市、特别行政区）：' + provinces.get(address_num))
        return True
    else:
        print(errors[5] + '->地址代码：' + str(address_num))
        return False


def check_birthday_num(id_num):
    """
    如果是大月1、3、5、7、8、10、12，1<=day<=31
    如果是小月4、6、9、11，1<=day<=30
    如果是2月，闰年01<=day<=29,否则01<=day<=28
    :param id_num:
    :return:
    """
    id_num = str(id_num).strip()
    if len(id_num) != 16 and len(id_num) != 18:
        print(errors[1])
        return False
    else:
        if len(id_num) == 16:
            year = id_num[6:8]
            month = id_num[8:10]
            day = id_num[10:12]
        else:
            year = id_num[6:10]
            month = id_num[10:12]
            day = id_num[12:14]

        if 1 <= int(month) <= 12:
            if int(month) in [1, 3, 5, 7, 8, 10, 12]:
                if 1 <= int(day) <= 31:
                    print("出生日期为：" + year + '年' + month + '月' + day + '日')
                    return True
                else:
                    print("输入生日为：" + year + '年' + month + '月' + day + '日')
                    print(errors[2] + '->出生天数不对，' + month + '月天数应该在1到29之间，当前为' + day)
                    return False
            elif int(month) in [4, 6, 9, 11]:
                if 1 <= int(day) <= 31:
                    print("出生日期为：" + year + '年' + month + '月' + day + '日')
                    return True
                else:
                    print("输入生日为：" + year + '年' + month + '月' + day + '日')
                    print(errors[2] + '->出生天数不对，' + month + '月天数应该在1到29之间，当前为' + day)
                    return False
            else:
                if is_yield_year(year):
                    if 1 <= int(day) <= 29:
                        print("出生日期为：" + year + '年' + month + '月' + day + '日')
                        return True
                    else:
                        print("输入生日为：" + year + '年' + month + '月' + day + '日')
                        print(errors[2] + '->出生天数不对，闰年' + month + '月天数应该在1到29之间，当前为' + day)
                        return False
                else:
                    if 1 <= int(day) <= 28:
                        print("出生日期为：" + year + '年' + month + '月' + day + '日')
                        return True
                    else:
                        print("输入生日为：" + year + '年' + month + '月' + day + '日')
                        print(errors[2] + '->出生天数不对，平年' + month + '月天数应该在1到28之间，当前为' + day)
                        return False
        else:
            print(errors[2] + '->出生月份不对')
            return False


def is_yield_year(year):
    try:
        year = int(year)
        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
            print(str(year) + "是闰年")
            return True
        else:
            print(str(year) + "不是闰年")
            return False
    except Exception as e:
        print(e)
        return


def check_verify_num(id_num):
    id_num = str(id_num).strip()
    if id_num[-1] == get_verify_num_v1(id_num):
        print('校验成功')
        return True
    else:
        print('校验错误')
        return False


def get_verify_num_v1(id_num):
    """
    校验码计算方法：
    1、将前面的身份证号码17位数分别乘以不同的系数。从第一位到第十七位的系数分别为：
        7－9－10－5－8－4－2－1－6－3－7－9－10－5－8－4－2。
    2、将这17位数字和系数相乘的结果相加。
    3、用加出来和除以11，看余数是多少？
    4、余数只可能有0－1－2－3－4－5－6－7－8－9－10这11个数字。对应关系如下：
        0－1－2－3－4－5－6－7－8－9－10
        1－0－X－9－8－7－6－5－4－3－2
    :param id_num:
    :return:
    """
    try:
        s = id_num[0:17]
        sum_num = int(s[0]) * 7 + int(s[1]) * 9 + int(s[2]) * 10 + int(s[3]) * 5 + int(s[4]) * 8 + int(s[5]) * 4 + \
                  int(s[6]) * 2 + int(s[7]) * 1 + int(s[8]) * 6 + int(s[9]) * 3 + int(s[10]) * 7 + int(s[11]) * 9 + \
                  int(s[12]) * 10 + int(s[13]) * 5 + int(s[14]) * 8 + int(s[15]) * 4 + int(s[16]) * 2
        sum_num = sum_num % 11
        verify_pairs = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
        return verify_pairs.get(sum_num)
    except Exception as e:
        print(e)
        return


def get_verify_num_v2(id_num):
    pass


def get_all_mobiles(text):
    """
    获取text中所有的手机号
    :param text:
    :return:
    """


def get_all_emails(text):
    """
    获取text中所有的邮箱
    :param text:
    :return:
    """


def get_total_words(text):
    """
    获取text所有的单词
    :param text:
    :return:
    """


if __name__ == '__main__':
    """
    # 打开一个文本文件
    # 读入其中的内容
    # 分析文本的内容
    """

    # is_yield_year(input("请输入年份："))
    # check_birthday_num(input('请输入身份证号：'))
    # check_address_num(input('请输入身份证号：'))
    # check_verify_num(input('请输入身份证号：'))
    is_valid_id_num(input('请输入身份证号：'))
