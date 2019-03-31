from flask import Flask, render_template, request, flash, redirect, url_for
# 导入wtf中的表单类
from flask_wtf import Form
# 导入自定义表单需要的字段
from wtforms import SubmitField,StringField,PasswordField

# 导入表单提供的表单验证器
from wtforms.validators import DataRequired, EqualTo, Required
import time
import json

app = Flask(__name__)
app.secret_key = 'lzd636'
#''' 留言板：discussion_board
with open('message.json', 'r') as f:
    data = json.load(f)
    users = data

@app.route('/say/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('discussion_board.html', says = users)
    else:
        title = request.form.get('say_title')
        text = request.form.get('say')
        user = request.form.get('say_user')
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        users.append({"title": title,
                      "text":text,
                      "user":user,
                      "date":date})
        with open('message.json', 'w') as f:
            json.dump(users, f)
    return redirect(url_for('index'))
# '''
if __name__ == '__main__':
    app.run(debug= True)

#
# class NameForm(Form):
#     name = StringField('What is your name',  validators = [Required])
#     submit = SubmitField('Submit')
#
#
# class LoginForm(Form):
#     username = StringField('用户名:', validators = [DataRequired()])
#     password = PasswordField('密码:', validators = [DataRequired()])
#     password2 = PasswordField('确认密码:', validators = [DataRequired(), EqualTo('password','密码不一致！')])
#     submit = SubmitField('提交')
#
#
#
# @app.route('/form', methods={'POST','GET'})
# def login():
#     login_form = LoginForm()
#     if request.form == 'POST':
#
#         username = request.form.get('username')
#         password = request.form.get('password')
#         password2 = request.form.get('password2')
#
#         # 参数校验
#         # if login_form.validate_on_submit():
#         #     print(username,password)
#         #     return 'success'
#         # #
#         # else:
#         #     print(9999999999)
#         #     flash('参数有误！！！')
#         if not all([username,password2,password]):
#             flash('yeys')
#         elif password != password2:
#             flash('no')
#         else:
#             return 'success'
#     return render_template('index.html', form=login_form)
#
# class RegisterForm(Form):
#     username = StringField('用户名:', validators = [DataRequired()])
#     password = PasswordField('密码:', validators = [DataRequired()])
#     password2 = PasswordField('确认密码:', validators = [DataRequired(), EqualTo('password','密码不一致！')])
#     submit = SubmitField('提交')
#
#
# @app.route('/', methods={'POST','GET'})
# def index():
#     # register_form = RegisterForm()
#     if request.method == 'POST':
#         # if register_form.validate_on_submit():
#         username = request.form.get('username')
#         password = request.form.get('password')
#         password2 = request.form.get('password2')
#         # print(username,password)
#
#         # return 'success'
#         if not all([username,password2,password]):
#             flash('yeys')
#         elif password != password2:
#             flash('no')
#         else:
#             return 'success'
#     return render_template('index.html')



#
# {{ form.username.label }}{{ form.username }} <br>
#     {{ form.password.label }}{{ form.password }} <br>
#     {{ form.password2.label }}{{ form.password2 }} <br>
#     {{ form.submit }} <br>