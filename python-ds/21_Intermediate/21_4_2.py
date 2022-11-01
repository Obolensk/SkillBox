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

# print(server_data)

for name, data in server_data.items():
  print('\n', name)
  for key, value in data.items():
    print('\t', key, ':', value)
