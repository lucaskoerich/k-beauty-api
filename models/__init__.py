from flask_sqlalchemy import SQLAlchemy

# Instância do SQLAlchemy
db = SQLAlchemy()

# Importando os modelos
from .accounts import Account
from .clients import Client
from .procedures import Procedure
