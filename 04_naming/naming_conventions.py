first_name = "Gosho"  # This is Python
is_admin = True

# def fetch_user_by_id(user_id):
firstName = "Gosho"  # This not Python
# print(first_name)
# print(firstName)

# Constants
MAX_RETRIES = 3
API_BASE_URL = "https://api.openai.com/v1"

# print(MAX_RETRIES)
# print("after")
MAX_RETRIES = 5
# print(MAX_RETRIES)


# PascalCase
class UserAccount:
    pass


class HTTPClient:
    pass


class Cache:
    def __init__(self):
        self.size = 100  # Public
        self._item = {}  # Privet


# def _cleanup(self): # internal method

my_cache = Cache()
my_cache.size = 200
# print(my_cache.size)

# False, True, break, and, or, as, async, await, finally, yield, with, while, for, class,  def, global, continue
# False = True
# print(False)
# print = "my name"
# print(print)
# my_list = list(range(5))
# print(list(range(5)))


# Bad naming!!!!
def calc(x, y):
    z = x * y * 0.2
    return z


# Good Naming
TAX_RATE = 0.2


def calculate_tax(price: float, quantity: int) -> float:
    return price * quantity * TAX_RATE


""" Задачи за упражнение: """

# 1. Създай променлива за имейл адрес с правилен snake_case.
# 2. Създай променлива за брой опити за вход — използвай snake_case.
# 3. Пренапиши тези camelCase имена на snake_case: `firstName`, `isAdmin`, `retryCount`.
# 4. Декларирай три constants: максимален брой потребители, базов URL и timeout в секунди.
# 5. Създай class `BankAccount` с PascalCase — само `pass` вътре.
# 6. Създай class `APIResponse` — провери дали акронимът е правилно изписан.
# 7. Добави към class `BankAccount` атрибути: един public `balance` и един „private" `_pin`.
# 8. Опитай да присвоиш стойност на `list` и после извикай `list(range(3))` — наблюдавай грешката.
# 9. Пренапиши тази функция с добри имена: `def f(a, b): r = a - b * 0.1; return r`
# 10. Вземи решението от задача 9 и добави type hints като в `calculate_tax`.
