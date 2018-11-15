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
    :param id_num:
    :return:
    """
    check_msgs = ['验证通过！', '身份证号码位数不对', '身份证出身日期不对', '含有非法字符', '身份证校验错误', '身份证地区错误']
    if len(id_num) == 18:
        # todo 处理18位身份证号码
        pass
    elif len(id_num) == 15:
        # todo 处理15位身份证号码
        pass
    else:
        # todo 错误提示
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
    count = 0
    while count < 10:
        input_mobile = input('请输入第%d个字符串:' % (count + 1))
        if is_valid_mobile(input_mobile):
            pass
        elif is_valid_email(input_mobile):
            pass
        count = count + 1
