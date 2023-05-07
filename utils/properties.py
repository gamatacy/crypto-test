from jproperties import Properties

configs = Properties()
with open('../currency.properties', 'rb') as config_file:
    configs.load(config_file)
print(configs.get("test").data)
