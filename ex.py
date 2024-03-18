import win32net

def get_windows_users():
    users_info = win32net.NetUserEnum(None, 0)
    users_list = [user_info['name'] for user_info in users_info[0]]
    return users_list

if __name__ == "__main__":
    windows_users = get_windows_users()
    print("Usuários do Sistema Operacional Windows:")
    for user in windows_users:
        print(user)
