from configparser import ConfigParser
from os.path import abspath

from cripto import Cripto


class Config:
    def __init__(self, chave: str = None, arquivo: str = '../proj.cfg'):
        """
        abre um objeto gerenciador de arquivos de configuração com criptogradia
        :param chave: chave do arquivo a ser aberto
        :param arquivo: diretorio do arquivo
        """
        self.cfg = ConfigParser()
        if chave is not None:
            self.cripto = Cripto(bytes(chave.encode('utf-8')))
            self.dir_arquivo = arquivo
            try:
                self.cfg.read(self.dir_arquivo)
            except Exception as e:
                raise Exception('Não foi possivel carregar o arquivo ', abspath(arquivo), 'Causa:', e)

    def open(self, diretorio: str):
        self.cfg.read(diretorio)

    def save(self, diretorio: str = '../proj.cfg'):
        try:
            file = open(diretorio, 'x')
        except FileExistsError:
            file = open(diretorio, 'w')
        finally:
            self.cfg.write(file)
            file.close()

    def set_db_user(self, value: str):
        user = self.cripto.criptografar(value)
        try:
            self.cfg['DATABASE']['User'] = user
        except KeyError:
            self.cfg.add_section('DATABASE')
            self.cfg.set('DATABASE', 'User', user)

    def get_db_user(self):
        user = self.cfg['DATABASE']['User']
        return self.cripto.descriptografar(user)

    def set_db_passwd(self, value: str):
        passwd = self.cripto.criptografar(value)
        try:
            self.cfg['DATABASE']['Password'] = passwd
        except KeyError:
            self.cfg.add_section('DATABASE')
            self.cfg.set('DATABASE', 'Password', passwd)

    def get_db_passwd(self):
        passwd = self.cfg['DATABASE']['Password']
        return self.cripto.descriptografar(passwd)

    def set_db_url(self, value: str):
        url = self.cripto.criptografar(value)
        try:
            self.cfg['DATABASE']['Url'] = url
        except KeyError:
            self.cfg.add_section('DATABASE')
            self.cfg.set('DATABASE', 'Url', url)

    def get_db_url(self):
        url = self.cfg['DATABASE']['url']
        return self.cripto.descriptografar(url)

    def set_db_name(self, value: str):
        name = self.cripto.criptografar(value)
        try:
            self.cfg['DATABASE']['Name'] = name
        except KeyError:
            self.cfg.add_section('DATABASE')
            self.cfg.set('DATABASE', 'Name', name)

    def get_db_name(self):
        name = self.cfg['DATABASE']['Name']
        return self.cripto.descriptografar(name)

    def set_db_port(self, value: int):
        port = self.cripto.criptografar(str(value))
        try:
            self.cfg['DATABASE']['Port'] = port
        except KeyError:
            self.cfg.add_section('DATABASE')
            self.cfg.set('DATABASE', 'PORT', port)

    def get_db_port(self):
        port = self.cfg['DATABASE']['Port']
        return int(self.cripto.descriptografar(port))

    def set_db_driver(self, value: 'str'):
        driver = self.cripto.criptografar(value)
        try:
            self.cfg['DATABASE']['Driver'] = driver
        except KeyError:
            self.cfg.add_section('DATABASE')
            self.cfg.set('DATABASE', 'Driver', driver)

    def get_db_driver(self):
        driver = self.cfg['DATABASE']['Driver']
        return self.cripto.descriptografar(driver)
