from flask import flash, redirect, url_for, render_template
from mysayhello.forms import HelloForm
from mysayhello.models import Message
from mysayhello import app, db


@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()  # 按照时间降序
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)  # 实例化模型
        db.session.add(message)
        db.session.commit()  # 提交会话
        flash('Your message have been sent to the world')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)  # 如果没有提交表单就渲染index.html页面，并传入参数form和messages
