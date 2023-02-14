from inquirer import prompt, List


def get_code_amount(clearscreen_func):
    while True:
        try:
            code_amount = int(input("How many codes should be generated?\n"))
        except ValueError:
            clearscreen_func()
        else:
            return code_amount


def get_format():
    return {"{nitro_code}": 0, "https://discord.gift/{nitro_code}": 1}[
        prompt(
            [
                List(
                    "format",
                    message="Format",
                    choices=["https://discord.gift/{nitro_code}", "{nitro_code}"],
                )
            ]
        )["format"]
    ]


def get_length():
    return {
        "Nitro classic/basic = 16 characters": 16,
        "Nitro boost = 24 characters": 24,
    }[
        prompt(
            [
                List(
                    "length/type",
                    message="Nitro type",
                    choices=[
                        "Nitro classic/basic = 16 characters",
                        "Nitro boost = 24 characters",
                    ],
                )
            ]
        )["length/type"]
    ]
