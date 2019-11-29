class Config(object):
    """

    Common configurations

    """

    # Put any condigurations here that are commo across all env's

class DevelopmentConfig(Config):

    """

    Development configurations

    """

    DEBUG = True
    # Enable Flask's debugging features. Should be False in production
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):

    """

    Production configurations

    """

    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
