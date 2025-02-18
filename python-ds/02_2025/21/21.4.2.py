
server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for data, info in server_data.items():
    print(data, end='\n')
    for key, value in info.items():
        print('   {}: {}'.format(key, value))