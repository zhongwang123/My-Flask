from app import create_app, db
from flask_script import Manager

app = create_app()
manager = Manager(app)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db)

if __name__ == '__main__':
    manager.run()
