import os 
class config(object):
    DEBUG = False
    CSRF_ENABLED= True
    SECRET = os.getenv('SECRET')

class DevelopmentConfig(config):
    DEBUG = True
class TestingConfig(config):
    TESTING = True
    DEBUG = True

class StagingConfig(Config):
    
    DEBUG = True


class ProductionConfig(Config):
   
    DEBUG = False
    TESTING = False
    
app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}


  