#  This is a comment
#  print("Hello world!")

x = 5  # inline comment
y = 10  # one more inline comment

counter = 0  # intialize counter
counter = counter + 1  # add 1

counter = 0
counter += 1  # Count retry from zero

"""
Thi is a
multiline comment
sadsadsa
"""

print("real code")


def add(a, b):
    """
    Add two numbers
    and return result
    """
    return a + b


print(add.__doc__)
help(add)


def fetch_user(user_id: int) -> dict:
    """Return user data

    Args:
        user_id

    Returns:
       Dict with user data
    """
    return {}


help(fetch_user)


# total = 0
# for item in cart:
#     # The gifts are out of charge
#     if item.is_gift:
#         continue
#     total += item.price


# TODO: "Do something later"
# FIXME: "Fix it"
# HACK: "My own data"
# NOTE: "Endpoint is deprecated!"


""" Задачи за упражнение: само коментари """

# 1. Напиши едноредов коментар с текст: Това е първият ми коментар.
# 2. Напиши едноредов коментар с текст: Днес уча Python коментари.
# 3. Напиши два последователни едноредови коментара по твой избор.
# 4. Напиши inline коментар след произволен ред с код (без да променяш кода).
# 5. Напиши многостроков коментар (triple quotes) с 2-3 реда текст.
# 6. Напиши TODO коментар за бъдеща задача.
# 7. Напиши FIXME коментар за въображаем проблем.
# 8. Напиши NOTE коментар с важно напомняне.
