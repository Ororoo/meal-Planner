from flask import Flask
import pymysql
import pymysql.cursors 




def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = ''
    
   
    # Register import
    from .home.home import home
    from .meal_plans.calendar import calendar
    from .account_settings.account_settings import account_settings

    # Register blueprints
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(calendar, url_prefix='/calendar')
    app.register_blueprint(account_settings, url_prefix='/account_settings')

    return app





    # from flask_mysqldb import MySQL
    # from .account_settings.user_info import user_info
    # from .account_settings.health_info import health_info
    # from .account_settings.diet_preference import diet_preference

    # app.register_blueprint(user_info, url_prefix='/')
    # app.register_blueprint(health_info, url_prefix='/')
    # app.register_blueprint(diet_preference, url_prefix='/')