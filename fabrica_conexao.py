import mysql.connector, configparser


class FabricaConexao():

    @staticmethod
    def conectar():
        config = configparser.ConfigParser()
        config.read('config.ini')
        db = mysql.connector.connect(
            user=config['DATABASE']['user'],
            passwd=config['DATABASE']['passwd'],
            db=config['DATABASE']['db'],
            host=config['DATABASE']['host'],
            port=int(config['DATABASE']['port']),
            auth_plugin=config['DATABASE']['auth_plugin'],
            autocommit=config['DATABASE']['autocommit']
        )

        return db

