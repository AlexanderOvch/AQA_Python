from db import init_db, insert_user, get_users

def main():
    init_db()
    insert_user("Test user")
    print(get_users())

if __name__ == "__main__":
    main()
