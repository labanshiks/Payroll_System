class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:Labandroid99@127.0.0.1:5432/payroll_system'
    environment = 'Development'
    DEBUG = True


class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:Labandroid99@127.0.0.1:5432/payroll_system'
    environment = 'Development'
    DEBUG = True


class Testing(Config):
    DEBUG = False


class Production(Config):
    SQLALCHEMY_DATABASE_URI = ''
    environment = 'Production'
    DEBUG = False
