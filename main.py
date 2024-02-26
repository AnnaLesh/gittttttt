import datetime

from flask import Flask, render_template, redirect

from data.jobs import Jobs
from data.user import User
from log_in_form import LoginForm
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def i():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    return render_template("base2.html", news=news)




# 
# user3 = User()
# user3.surname = 'Andrew'
# user3.name = "Lesh"
# user3.position = 'programmer'
# user3.speciality = 'programmer'
# user3.address = 'module_3'
# user3.email = "andrew@yandex.ru"
# db_sess = db_session.create_session()
# db_sess.add(user3)
# db_sess.commit()
#
# 
#
# job = Jobs()
# job.team_leader = 1
# job.job = 'deployment of residential modules 1 and 2'
# job.work_size = 15
# job.collaborators = '2, 3'
# job.is_finished = False



# db_sess.add(job)
# db_sess.commit()

if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    # db_sess = db_session.create_session()
    # colonist = db_sess.query(User).filter(User.age < 18)
    # colonist1 = db_sess.query(User).filter((User.position.like('%chief%')) | (User.position.like('%middle%')))
    # for user in colonist:
    #     print(user + f"{user.age} years")

    # db_sess = db_session.create_session()
    # news = db_sess.query(Jobs).all()
    app.run(port=8080, host='127.0.0.1')
