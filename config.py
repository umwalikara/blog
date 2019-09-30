# import os

# class Config:

#     SECRET_KEY = 'a random string'
#     UPLOADED_PHOTOS_DEST ='app/static/photos'
#     QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
#     #  email configurations
#     MAIL_SERVER = 'smtp.googlemail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
#     MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
#     SUBJECT_PREFIX = 'blogging'

#     # simple mde  configurations
#     SIMPLEMDE_JS_IIFE = True
#     SIMPLEMDE_USE_CDN = True


#     @staticmethod
#     def init_app(app):
#         pass


# class ProdConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    

# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:kasa@10@localhost/blog_test'

# class DevConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:kasa@10@localhost/blog'
#     DEBUG = True

# config_options = {
# 'development':DevConfig,
# 'test':TestConfig,
# 'production':ProdConfig

# }
