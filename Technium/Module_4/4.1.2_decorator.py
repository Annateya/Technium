def requires_admin(func):
    def wrapper(user, *args, **kwargs):
        if user['role'] != 'admin':
            raise PermissionError('Ошибка: только администратор может выполнять это действие')
        return func(user, *args, **kwargs)
    return wrapper

@requires_admin
def delete_user(user, username_to_delete):
    return f"User {username_to_delete} has been deleted by {user['username']}."


# Пример юзеров
admin_user = {'username': 'Alice', 'role': 'admin'}
regular_user = {'username': 'Bob', 'role': 'user'}

# Вызовы функции
print(delete_user(admin_user, 'Charlie')) # Должно отработать
print(delete_user(regular_user, 'Charlie')) # Должно рейзить PermissionError

