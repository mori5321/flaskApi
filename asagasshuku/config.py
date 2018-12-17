import os

class DevelopmentConfig:
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = "postgresql://localhost/asagasshuku"

Config = DevelopmentConfig
