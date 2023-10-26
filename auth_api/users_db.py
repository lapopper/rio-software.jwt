users = {
    "mike": {
        "username": "mike",
        "hashed_password": "$2y$10$jTHVmm2YbEhc1JBlJmTgYuWoY6yFGm4DW6NpA9MAczdNC/SV/TtGe",
    }
}


def get_user(username: str):
    if username in users:
        user = users[username]
        return user