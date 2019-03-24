from datetime import datetime
from mysayhello import db


class Message(db.Model):  # 信息的数据库模型
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
