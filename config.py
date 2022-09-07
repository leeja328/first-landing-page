import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Give access to the project in any OS we find ourselves in
# Allow outside files or folders to be added to the project from
# the base directory

class Config():
    """
    Set config variables for the flask app
    Using enviroment variables where available, otherwise
    create the config variable if not done already
    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #turn off update messages from sqlalchemy
    # Todo: Add .env