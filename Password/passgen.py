# -*- coding: utf-8 -*-
#!/usr/bin/env python


# !pip install passlib
from passlib import pwd


def password_generator(length=64, entropy=192):
    options = {
        "entropy": entropy, "length": length, "charset": "ascii_72", "returns": None
    }
    return pwd.genword(**options)


if __name__ == "__main__":

    for i in range(5):
        print(f"Password {i + 1}: ", password_generator())
