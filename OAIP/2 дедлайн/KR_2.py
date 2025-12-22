admins = {"admin_bob", "admin_alice", "admin_john"}
editors = {"editor_nick", "editor_emma", "admin_bob"}
banned = {"user5", "spammer", "admin_bob", "editor_nick"}

access_attempts = ["user1", "user5", "admin_bob", "editor_nick", "unknown_user", "admin_alice"]

def find_super_users(admins_set, editors_set):
    return admins_set.intersection(editors_set)

def find_wrongly_banned(banned_set, admins_set, access_list):
    wrongly_banned = []
    for user in access_list:
        if user in banned_set and user not in admins_set:
            wrongly_banned.append(user)
    return wrongly_banned

def find_no_role_users(access_list, admins_set, editors_set):
    no_role = []
    for user in access_list:
        if user not in admins_set and user not in editors_set:
            no_role.append(user)
    return no_role

super_users = find_super_users(admins, editors)
print("Супер-пользователи (админы и редакторы одновременно):", super_users)

wrongly_banned_users = find_wrongly_banned(banned, admins, access_attempts)
print("Некорректно заблокированные пользователи:", wrongly_banned_users)

no_role_users = find_no_role_users(access_attempts, admins, editors)
print("Пользователи без ролей:", no_role_users)