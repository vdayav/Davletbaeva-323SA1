def find_superusers(admins: set, editors: set) -> set:
    return admins & editors


def find_incorrectly_banned(access_attempts: list, banned: set, admins: set) -> set:
    banned_attempts = set(access_attempts) & banned
    
    return banned_attempts - admins


def find_users_without_roles(access_attempts: list, admins: set, editors: set) -> set:
    users_with_roles = admins | editors
    
    return set(access_attempts) - users_with_roles


def main():
    admins = {"admin_bob", "admin_alice", "user1", "user3"}
    editors = {"editor_john", "user1", "user2", "user4"}
    banned = {"user5", "spammer", "user1", "admin_bob"}
    access_attempts = ["user1", "user5", "admin_bob", "editor_john", 
                       "user10", "spammer", "user2", "guest", "user7"]
    
    superusers = find_superusers(admins, editors)
    print("Супер-пользователи (одновременно администраторы и редакторы):")
    print(f"   {sorted(superusers) if superusers else 'Нет таких пользователей'}")
    
    incorrectly_banned = find_incorrectly_banned(access_attempts, banned, admins)
    print("\nОшибочно заблокированные пользователи (в banned, но не админы):")
    print(f"   {sorted(incorrectly_banned) if incorrectly_banned else 'Нет таких пользователей'}")
    
    users_without_roles = find_users_without_roles(access_attempts, admins, editors)
    print("\nПользователи без ролей (пытались войти, но нет роли):")
    print(f"   {sorted(users_without_roles) if users_without_roles else 'Нет таких пользователей'}")

if __name__ == "__main__":
    main()