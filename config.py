class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'some secret key'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:Labandroid99@127.0.0.1:5432/payroll_system'
    environment = 'Development'
    DEBUG = True


class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:Labandroid99@127.0.0.1:5432/payroll_system'
    environment = 'Development'
    DEBUG = True


class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://frklucjwocdhyd:4b15858605b077f5375f423c16d80878d5ac8a48ba8c36483e9c046b8234d043@ec2-23-21-177-102.compute-1.amazonaws.com:5432/dpkf92obtrrfu'
    environment = 'Production'
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

