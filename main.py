from scripts.requirement_handler import *

install_requirements(check_requirements())
from scripts.generate import *
from scripts.input import *
from scripts.misc import *


def main():
    clearscreen()

    code_amount = get_code_amount(clearscreen)

    clearscreen()

    format = get_format()

    clearscreen()

    length = get_length()

    clearscreen()

    codes = pool_handler(
        length,
        code_amount,
        format,
        {
            "generate_code_no_url": generate_code_no_url,
            "generate_code_with_url": generate_code_with_url,
        },
    )

    clearscreen()

    write_codes(codes, code_amount)


if __name__ == "__main__":
    main()


