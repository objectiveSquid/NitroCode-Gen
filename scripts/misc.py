from multiprocessing import pool
from functools import partial
from os import system, name


def write_codes(codes: list, code_amount: int):
    print(f"Writing {code_amount} codes...")
    with open("codes.txt", "a") as codes_opened:
        for code in codes:
            codes_opened.write(f"{code}\n")
    input(f"Wrote all codes to file.\nPress enter to exit...")


def clearscreen():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def pool_handler(length: int, code_amount: int, format: int, code_generators: dict):
    codes = []
    print(f"Generating {code_amount} codes...")
    with pool.Pool() as Pool:
        if format == 0:
            results = Pool.map(
                partial(code_generators["generate_code_no_url"], length),
                range(code_amount),
            )
            for code in results:
                codes.append(code)
        else:
            results = Pool.map(
                partial(code_generators["generate_code_with_url"], length),
                range(code_amount),
            )
            for code in results:
                codes.append(code)
    return codes
