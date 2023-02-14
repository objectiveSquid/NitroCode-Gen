from random import choice


def generate_code_with_url(length: int, _):
    return f"https://discord.gift/{''.join(choice('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(length))}"


def generate_code_no_url(length: int, _):
    return "".join(
        choice("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        for i in range(length)
    )
