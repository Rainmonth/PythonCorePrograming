# -*- coding: UTF-8 -*-
def get_triangle_area(var_a, var_b, var_c):
    if is_legal_abc(var_a, var_b, var_c):
        s = (var_a + var_b + var_c) / 2
        area = (s * (s - var_a) * (s - var_b) * (s - var_c)) ** 0.5
        print('三角形的面积为:%0.2f' % area)


def is_legal_abc(var_a, var_b, var_c):
    """
    判断是否可构成三角形（两边之和大于第三边）
    :param var_a:
    :param var_b:
    :param var_c:
    :return:
    """
    if (var_a + var_b) > var_c and (var_b + var_c) > var_a and (var_c + var_a) > var_b:
        print('可构成三角形')
        return True
    else:
        print("参数异常，不符合三边定理，不能构成三角形")
        return False


if __name__ == '__main__':
    a = input('请输入第一条边长a：')
    if a.isdecimal():
        pass
    else:
        print(a + '不是有效的边长')
        a = input('请重新输入如第一条边长a：')
    b = input('请输入第二条边长b：')
    if b.isdecimal():
        pass
    else:
        b = input(b + '不是有效的边长请重新数据如第一条边长b：')
    c = input('请输入第三条边长c：')
    if c.isdecimal():
        pass
    else:
        print(c + '不是有效的边长')
        c = input('请重新数据如第一条边长c：')

    # unsupported operand type(s) for /: 'str' and 'int'
    try:
        get_triangle_area(int(a), int(b), int(c))
    except Exception as e:
        print(e)
        print('参数异常')
