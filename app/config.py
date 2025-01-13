import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY', 'csrf-key')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
