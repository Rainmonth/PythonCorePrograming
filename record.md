# 网址记录

## 学习网址
- [音视频学习](https://blog.csdn.net/leixiaohua1020)
- [提高效率的AS插件](https://juejin.im/post/5bbda0df5188255c7b16a2a1)
- [快速学Python](https://github.com/xianhu/LearnPython)
- [RecyclerView加载图片闪烁的真凶及解法](https://www.jianshu.com/p/29352def27e6)

## 配置问题
1. charles 代理问题 [Charles抓包https](https://www.jianshu.com/p/ec0a38d9a8cf)

## 爬虫相关
###[高效微信公众号历史文章和阅读数据爬虫](https://github.com/wonderfulsuccess/weixin_crawler)
#### 项目运行前提条件
Mac 下安装MongoDB、Redis、elasticsearch
##### 安装MongoDB
1. [了解MongoDB]()
    - [MongoDB百度百科](https://baike.baidu.com/item/mongodb/60411?fr=aladdin)
    - [MongoDB官网](https://www.mongodb.com/)
    - [MongoDB文档](https://docs.mongodb.com/)
2. [Mac下安装与配置MongoDB](https://blog.csdn.net/thatway_wp/article/details/79362261)
具体步骤：
- 官网下载对应的版本，我下载的是`mongodb-osx-ssl-x86_64-4.0.4.tgz`
- 解压缩到指定目录（假设为dir）
- 设置环境变量
     ```
     export MONGODB_HOME="dir"
     export PATH=${PATH}:${MONGODB_HOME}/bin      
    ```
- 配置MongoDB运行环境(采用以下配置，其中{dir}换成自己定义的数据库存放目录)
    ```
    #数据库路径
    dbpath={dir}/db/
    
    #日志输出文件路径
    logpath={dir}/logs/mongodb.log
    
    #错误日志采用追加模式，配置这个选项后mongodb的日志会追加到现有的日志文件，而不是从新创建一个新文件
    logappend=true
    
    #启用日志文件，默认启用
    journal=true
    
    #这个选项可以过滤掉一些无用的日志信息，若需要调试使用请设置为false
    quiet=false

    #是否后台启动，有这个参数，就可以实现后台运行
    fork=true

    #端口号 默认为27017
    port=27017

    #指定存储引擎（默认不需要指定）
    #storageEngine=mmapv1

    #开启网页日志监控，有这个参数就可以在浏览器上用28017查看监控界面
    #这个配置在4.0.4上已经不用了，注释掉
    #httpinterface=true
    ```
- 应用上面的配置
    ```
    mongod -f conf_file_path_dir # 配置文件路径
    # 或者
    mongod --config conf_file_path_dir
    # 二者等效
    ```
##### 安装Redis 
1. [了解Redis](https://baike.baidu.com/item/Redis/6549233?fr=aladdin)
2. [Mac下安装Redis]()
3. [配置Redis]()
##### 安装elasticsearch
    1. [了解elasticsearch]()
    2. [Mac下安装elasticsearch]()
    3. [配置elasticsearch]()


## todo
- [用Python写一个翻译脚本（实现基本的GUI界面）](https://blog.csdn.net/MrLevo520/article/details/51674188)
    > 里面包含了如何创建GUI界面，如何发布成APP的详细步骤