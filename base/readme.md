# Python基础内置函数

## 杂项

### 环境问题

- PyCharm Run模式运行正常，Debug模式报各种错误，***这个时候请检查自己命名的.py文件是否和Python自己定义的文件同名***

## zip

    - 参数
    -- 多个可迭代对象
    - 返回值，
    -- zip对象，其__next__() 方法可以返回一个元组
    - 打印zip
    ```
        print(list(zip(iterator1, iterator2)))
    ```
## map
    - 参数
    参数1：待执行函数，通常为lambda表达式
    参数2：可迭代对象
    
    返回值，由传入的lamda表达式决定，将迭代器中的对象作为参数共lambda使用
    - 打印map


​    

