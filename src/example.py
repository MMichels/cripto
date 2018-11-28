from cfgManager import Config

cfg = Config('ESghnvslK75_QDZgO3X7aqNM2Tej7JtzgsN2ogAOZzA=')
cfg.set_db_user('root')
cfg.set_db_passwd('psKkZMVn2ojTFuEBvNg=')
cfg.set_db_port(3306)
cfg.save()
print(cfg.get_db_user())
print(cfg.get_db_passwd())
print(cfg.get_db_url() +
      '\n' + cfg.get_db_name())
print(cfg.get_db_port())
