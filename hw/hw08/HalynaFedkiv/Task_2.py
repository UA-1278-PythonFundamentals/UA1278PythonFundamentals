import re


def password_validation(password):
    if re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])[A-Za-z0-9$#@]{6,16}$', password):
        return True
    else:
        return False


print(password_validation('jkhvj9fkd9'))
print(password_validation('kRjigf@kd80'))
print(password_validation('1Rjf@!!'))
print(password_validation('1Rj@'))
