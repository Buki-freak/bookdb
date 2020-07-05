# 图书管理数据库应用程序

## 程序介绍

此应用程序使用 python 下的 tkinter 模块进行编写，数据库基于 mysql ，各文件如下：



> admin.py 管理员界面
>
> bookdb.sql 数据库文件
>
> login.py 登陆界面
>
> main.py 初始化文件（入口文件）
>
> query.py 查询界面
>
> reader.py 读者界面
>
> register.py 注册界面



## 使用方法

1. 向 mysql 数据库中导入 bookdb.sql 中的数据和设置 
2. 在 bookdb 目录下运行 main.py 文件（必须先安装 tkinter 模块）
3. 点击 query 进入图书查询界面；点击 login 可以进行登录
4. login 界面可以点击 register  进行注册；login 的方式有两种：admin 或者 reader
5. admin 身份登录后可以对读者的图书借阅和归还进行操作；reader 身份登录后可以查看自己的借阅情况
