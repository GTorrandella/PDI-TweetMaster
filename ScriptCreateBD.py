#Script para crear la BD:
from DataBaseConnector import configTables
configTables.BD.metadata.create_all(configTables.engine)