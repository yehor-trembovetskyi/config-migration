import json

result = "#, uniqueId, name\n"
i = 0
for line in open('not-found.txt').readlines():
    i += 1
    info = json.loads(line)
    result += f'{i}, {info["unique_id"]}, {info["leo_admin_game"]["name"]}\n'


f = open("not-found.csv", "w")
f.write(result)
