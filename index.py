#-*-coding:utf-8 -*_
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import  make_response
from flask import  session,escape,url_for
from wtforms import Form,TextField,PasswordField,validators

app=Flask(__name__)



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
app.secret_key = 'fadkjakfjiuijfdsafjajfaj090!'

@app.route("/")

def index():
    if 'hugo' in session:
        return  'Logged in as %s' % escape(session['hugo'])
    else:
        return  'you are not logged in'

@app.route("/login",methods=['GET','POST'])

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
                                #设置session会话保持
                                session['hugo'] = myForm.username.data
                                return  resp
                                # return  redirect('http://www.baidu.com')
                        else:
                                message="Login Failed"
                                return render_template('index.html', message=message, form=myForm)
                return render_template('index.html', form=myForm)

#退出
@app.route('/logout')
def logout():
    session.pop('hugo',None)
    return  redirect(url_for('login'))


if __name__=="__main__":
        app.run(port=10000)