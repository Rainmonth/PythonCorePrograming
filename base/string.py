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


def is_valid_email(email):
    """
    是否是有效的邮箱地址
    :param email
    :return:
    """


def is_valid_id_num(id_num):
    """
    是否是有效的身份证号码
    :param id_num:
    :return:
    """


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
        input_mobile = input('请输入第%d个手机号码:' % (count + 1))
        is_valid_mobile(input_mobile)
        count = count + 1
