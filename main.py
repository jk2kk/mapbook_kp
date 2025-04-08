users = [
    {"name": "Krzysztof", "location": "Lublin", "posts": 500},
    {"name": "Bartosz", "location": "Ostrołeka", "posts": 69},
    {"name": "Ksawier", "location": "Warszawa", "posts": 32},
    {"name": "Mikołaj", "location": "Madryt", "posts": 56},

]


def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user['name']}, z miejscowości {user['location']} opublikował {user['posts']}")

        get_user_info(users)
