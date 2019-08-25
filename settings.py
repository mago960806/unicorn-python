class Config(object):
    # 是否启用DEBUG
    DEBUG = True

    # 数据库配置
    DB_HOST = '127.0.0.1'
    DB_PORT = '27017'


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
