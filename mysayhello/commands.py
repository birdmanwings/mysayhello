import click

from mysayhello import app, db
from mysayhello.models import Message


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):  # 初始化数据库
    if drop:
        click.confirm('这将会删除数据库，是否继续执行', abort=True)
        db.drop_all()
        click.echo('删除数据库')
    db.create_all()
    click.echo('初始化数据库')


@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages,default is 20')
def forge(count):
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker()
    click.echo('进行中...')

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)

    db.session.commit()
    click.echo('初始化 %d 条数据' % count)
