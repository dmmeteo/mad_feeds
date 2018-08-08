# project/config.py
import os


class BaseConfig:
    """Base configuration"""
    SECRET_KEY = os.environ.get("SECRET_KEY")
    TESTING = False
    # MONGODB_HOST = 'mongo'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    MONGODB_DB = os.environ.get('DATABASE_NAME')
    DEBUG_TB_PANELS = ['flask_mongoengine.panels.MongoDebugPanel']


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    MONGODB_DB = os.environ.get('DATABASE_TEST_NAME')


class ProductionConfig(BaseConfig):
    """Production configuration"""
    MONGODB_DB = os.environ.get('DATABASE_NAME')
    MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME')
    MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD')

