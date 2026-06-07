# Python #6 — Naming conventions (snake_case и защо)

> **Дължина**: 3-4 мин | **Предишно**: #5 Variables | **Следващо**: #7 Numbers

---

## СЦЕНА 1 — Hook (0:00 – 0:12)

**На екрана**: split screen — ляво junior код, дясно senior код.

```python
# ❌ Junior
x = "ana@example.com"
y = 0
d = 86400

# ✅ Senior
user_email = "ana@example.com"
retry_count = 0
SECONDS_PER_DAY = 86400
```

**Казваш**:

> „Лоши имена са номер едно признак на junior код. Гледай това — може да пишеш на ниво senior още утре. Само 4 правила. 3 минути и са в главата."

---

## СЦЕНА 2 — Правило 1: snake_case (0:12 – 0:50)

**Пишеш**:

```python
# ──────────────────────────────────────────
# Правило 1: snake_case → variables и functions
# малки букви + долна черта между думите
# ──────────────────────────────────────────

# Variables — snake_case
user_email = "ana@example.com"   # не userEmail
retry_count = 0                  # не retryCount
is_admin = False                 # не isAdmin


# Functions — също snake_case
def calculate_total(items):
    ...

def fetch_user_by_id(user_id):
    ...
```

**Казваш докато пишеш** `user_email`:

> „Snake case — малки букви, думите свързани с долна черта. Защо snake? Защото underscore-ите изглеждат като змия извиваща се между думите."

**Казваш докато пишеш функциите**:

> „Същото важи за functions. `snake_case` за неща, които правят или съдържат данни."

**Пишеш camelCase примера**:

```python
# ❌ camelCase — работи технически, НЕ е Python
userEmail = "ana@example.com"
retryCount = 0
def calculateTotal(items): ...
```

**Казваш**:

> „Ако идваш от Java или JavaScript — там е camelCase, малка първа буква, главна за следваща дума. В Python технически работи, но всеки Python developer ще те погледне странно. Ruff linter ще warn-не."

> „Защо? Защото built-in functions са snake_case — `print`, `len`, `isinstance`. Твоят код трябва да изглежда като стандартната библиотека."

---

## СЦЕНА 3 — Правило 2: UPPER_CASE (0:50 – 1:25)

**Пишеш**:

```python
# ──────────────────────────────────────────
# Правило 2: UPPER_SNAKE_CASE → constants
# стойности, които НЕ променяме
# ──────────────────────────────────────────

MAX_RETRIES = 3
API_BASE_URL = "https://api.openai.com/v1"
DEFAULT_TIMEOUT = 30
PI = 3.14159
```

**Казваш докато пишеш**:

> „Constants — стойности, които не променяме след инициализация. Главни букви, underscore-и между думите."

> „Python няма истински constants — технически можеш да направиш `MAX_RETRIES = 5` по-късно. Главните букви са сигнал към другите developers: не пипай това."

> „Конвенция: constants отиват най-горе в файла, веднага след imports."

---

## СЦЕНА 4 — Правило 3: PascalCase (1:25 – 1:55)

**Пишеш**:

```python
# ──────────────────────────────────────────
# Правило 3: PascalCase → classes
# главна буква за всяка дума, без underscore
# ──────────────────────────────────────────

class UserAccount:
    pass

class HTTPClient:       # acronym-ите остават главни
    pass

class DatabaseConnection:
    pass
```

**Казваш докато пишеш**:

> „Classes — PascalCase. Главна първа буква за всяка дума. Без underscore."

> „Универсална конвенция — Java, C#, TypeScript — всички ползват PascalCase за classes."

**Казваш докато пишеш `HTTPClient`**:

> „Виж — `HTTPClient`. Акроними в Python остават главни в class names. Не `HttpClient`. Дискусионно — и двете виждаш в реални codebase-и."

> „Засега само naming — classes разглеждаме детайлно в видео 61."

---

## СЦЕНА 5 — Правило 4: leading underscore (1:55 – 2:25)

**Пишеш**:

```python
# ──────────────────────────────────────────
# Правило 4: _leading → "private" (само конвенция!)
# ──────────────────────────────────────────

class Cache:
    def __init__(self):
        self.size = 100       # public — ползвай свободно
        self._items = {}      # „private" — не пипай отвън

    def _cleanup(self):       # internal method
        ...
```

**Казваш докато пишеш `self._items`**:

> „Долна черта пред името — конвенция за private. Не пипай отвън."

> „Python няма истински private. Можеш да достъпиш `cache._items` от навсякъде. Но underscore-ът е сигнал: това е internal, може да се промени без warning."

**Казваш накрая**:

> „Двойна долна черта от двете страни — `__init__`, `__str__` — това са dunder methods, double underscore. Специални. Ще ги разгледаме в видео 67."

---

## СЦЕНА 6 — Reserved words + built-in капани (2:25 – 3:15)

**Пишеш и run-ваш**:

```python
# ──────────────────────────────────────────
# Reserved words — не можеш да ги ползваш като имена
# ──────────────────────────────────────────

class = "math"     # ❌ SyntaxError
def = "function"   # ❌ SyntaxError
return = 5         # ❌ SyntaxError
```

**Казваш**:

> „Тези думи са reserved — Python ги ползва за синтаксис. Не можеш да ги ползваш като имена."

**Пишеш решението**:

```python
# ✅ Ако трябва — trailing underscore по конвенция
class_ = "btn-primary"
type_ = "admin"
```

**Казваш**:

> „Ако наистина трябва — конвенцията е trailing underscore. Случва се когато правиш wrapper около external API, който има `class` параметър."

---

**Пишеш built-in капана**:

```python
# ──────────────────────────────────────────
# ⚠️ Капан: overriding built-ins
# ──────────────────────────────────────────

list = [1, 2, 3]
print(list)           # [1, 2, 3] — изглежда ОК

# По-късно в кода...
nums = list(range(5)) # ❌ TypeError: 'list' object is not callable
```

**Казваш докато пишеш**:

> „Гледай това. Сложих `list = [1, 2, 3]`. Override-нах built-in-а `list`. Сега когато опитам `list(range(5))` — грешка. Типът `list` вече не съществува."

> „Pylance подчертава ето тук — виж жълтата линия. Казва: shadows built-in name `list`."

> „Други built-ins, които начинаещи често override-ват: `dict`, `str`, `id`, `type`, `input`, `format`. Винаги ползвай по-специфично име — `my_list`, `user_dict`, `name_str`."

---

## СЦЕНА 7 — Защо имената матерят (3:15 – 3:45)

**Пишеш**:

```python
# ──────────────────────────────────────────
# Защо имената матерят
# ──────────────────────────────────────────

# ❌ Junior — какво е x, y, z?
def calc(x, y):
    z = x * y * 0.2
    return z


# ✅ Senior — четимо без коментар
TAX_RATE = 0.2

def calculate_tax(price: float, quantity: int) -> float:
    return price * quantity * TAX_RATE
```

**Казваш**:

> „Сравни. Двете правят абсолютно същото. Долният — четим. Преди type hints, преди docstring — просто имената казват всичко."

> „Запомни: кодът се чете 10 пъти повече, отколкото се пише. Компилаторът не го интересува дали си писал `x` или `customer_lifetime_value`. Хората — да."

---

## СЦЕНА 8 — CTA (3:45 – 4:00)

**Казваш**:

> „Следващото — numbers. Защо `0.1 + 0.2` не е `0.3` в Python. И как не правиш бъгове с пари. Натисни тук."

---

## Quick reference (финален overlay)

```
snake_case    → variables, functions
UPPER_CASE    → constants
PascalCase    → classes
_leading      → "private" (конвенция)
__dunder__    → special methods
```

| ❌ Лоши имена                            | ✅ Добри имена                   |
| ---------------------------------------- | -------------------------------- |
| `x, y, z, d, lst, fn1, temp`             | `user_email, retry_count, items` |
| `list, dict, str, type, id` (built-ins!) | `my_list, user_dict, name_str`   |
| `camelCase` за variables                 | `snake_case` за variables        |
| single letters (освен `i, j, k` в loops) | `calculate_total`, `MAX_SIZE`    |

---

## Възможни въпроси

**В: Single letter variables — никога?**
О: OK за loop counters (`for i in range(10)`) и math (`x, y` за координати). Иначе — не.

**В: Има ли auto-formatter?**
О: Да — `black` и `ruff format`. Но naming НЕ се поправя автоматично — само whitespace/quotes.
