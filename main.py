import win32net

users = win32net.NetUserEnum(None, 0)

for user in users[0]:
    print(user['name'])

print("Aluna: Larissa Felipe Reis")
print("RA: 32419802")