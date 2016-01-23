#-*-coding:utf-8 -*_
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import  make_response
from flask import  session,escape

app=Flask(__name__)

from wtforms import Form,TextField,PasswordField,validators

class LoginForm(Form):
        username = TextField("username",[validators.Required()])
        password = PasswordField("password",[validators.Required()])

#
# @app.route('/')
#
# def index():
#     if 'loginCookies' in request.cookies:
#                 #count = int(request.cookies['test'])+1
#                 return redirect("http://www.360.com");
#     else:

#设置密钥

@app.route("/login",methods=['GET','POST'])

# def saveCookies():
#       # redirect_to_index = redirect('/login')
#       # response = app.make_response(redirect_to_index )
#       response = app.make_response(render_template('index.html',form=LoginForm(request.form)))
#       response.set_cookie('loginCookies','fjdsafjafj9392jfn',max_age= 60 * 60)
#       return  response
#       # return redirect("htpp://www.baidu.com")



def login():
        #判断cookies中key是否存在
        if 'loginCookies' in request.cookies:
                #count = int(request.cookies['test'])+1
                return redirect("http://www.360.com");
        else:
                myForm = LoginForm(request.form)
                # resp = app.make_response(render_template('index.html',form=myForm))
                # #设置cookies有效期一个小时
                # resp.set_cookie('loginCookies','fjdsafjafj9392jfn',max_age= 1 * 60)
                # return  resp
                if request.method=='POST':
                        if myForm.username.data=="hugo" and myForm.password.data=="hugo9091" and myForm.validate():
                                # return redirect("http://www.baidu.com")
                                resp = make_response(redirect('http://www.baidu.com'))
                                #resp = app.make_response(render_template('index.html',form=myForm))
                                #设置cookies有效期一个小时
                                resp.set_cookie('loginCookies','fjdsafjafj9392jfn',max_age= 60 * 60)
                                return  resp
                                # return  redirect('http://www.baidu.com')
                        else:
                                message="Login Failed"
                                return render_template('index.html', message=message, form=myForm)
                return render_template('index.html', form=myForm)

if __name__=="__main__":
        app.run(port=10000)