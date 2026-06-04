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
