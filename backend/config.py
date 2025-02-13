import configparser

config = configparser.ConfigParser()
config.read('backend/config.ini')

# Debugging: print the loaded sections and key-values
print(config.sections())  # Should show ['postgresql', 'redis']
print(config['postgresql'])  # Should print out user, password, etc.

# PostgreSQL configuration
DB_CONFIG = {
    'user': config["postgresql"]["user"],
    'password': config['postgresql']['password'],
    'host': config['postgresql']['host'],
    'port': config['postgresql']['port']
}

# Redis configuration
REDIS_CONFIG = {
    'host': config['redis']['host'],
    'port': config['redis']['port']
}
