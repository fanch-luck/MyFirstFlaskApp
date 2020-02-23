#!/usr/bin/python
# -*- coding:utf-8 -*-
# -----------------------------------------------------------
# @File Name: myapp
# @Author:    Fan
# @Date:      2020/1/18 19:29
# @Content:   一个最简单的Flask实现
# -----------------------------------------------------------
from flask import Flask, redirect, url_for, request

app = Flask(__name__)  # Flask类的一个对象是我们的WSGI应用程序 Flask构造函数使用当前模块（__name __）的名称作为参数。


@app.route('/')
# Flask类的route(rule, options)函数是一个装饰器，它告诉应用程序哪个URL应该调用相关的函数。
# rule 参数表示与该函数的URL绑定。 options 是要转发给基础Rule对象的参数列表。
#  在上面的示例中，'/ ' URL与my_first_flask_app()函数绑定。因此，当在浏览器中打开web服务器的主页时，将呈现该函数的输出。
def my_first_flask_app():
    return 'This is my first flask app!'


# @app.route('/hello')  # 指定路由/hello与程序返回间的对应关系
# def hello_world():
#     return 'Hello world!'


@app.route('/hello/')  # 确保在输入URL时，/hello 与/hello/是等价的
def hello_world_correct():
    return 'Hello world! You are using the correct URL rule "/hello/"!'


@app.route('/commit/<param>')  # 指定路由和提交参数，且参数作为对应函数的参数
def commit_param(param):
    return 'You committed a string param: %s' % param


@app.route('/commit/param_int/<int:record_id>')
def commit_param_int(record_id):
    return 'You committed an int param(record id): %d' % record_id


@app.route('/commit/param_float/<float:temperature>')
def commit_param_float(temperature):
    return 'You commit a float param(temperature): %f' % temperature


# 创建以下内容为login.html表单，演示表单中利用POST方法将数据发送到URL<login>,
# 该URL接收数据并处理后显示成功信息<success>
"""
<html>
   <body>
      
      <form action = "http://localhost:5000/login" method = "post">
         <p>Enter Name:</p>
         <p><input type = "text" name = "nm" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>
      
   </body>
</html>
"""
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))  # 再重定向（？）到/success
    else:
        user = request.args.get('nm')  # 如果指定了method='GET'，则通过args字典获取nm的值
        return redirect(url_for('success', name=user))



if __name__ == '__main__':
    app.run(debug=True)  # Flask类的run()方法在本地开发服务器上运行应用程序。
