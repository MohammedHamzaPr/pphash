"""
pphash
------
Python Password Hashing Library

A simple library for creating and checking password hashes,
detecting hash algorithms, and generating strong passwords.
"""

from hashlib import new
from secrets import choice


__version__ = "0.0.1"

__all__ = [
    "help_",
    "ghash",
    "chash",
    "getmode",
    "gpass",
]


# Supported hash algorithms and their hexadecimal digest lengths
_HASH_MODES = {
    32: "md5",
    40: "sha1",
    56: "sha224",
    64: "sha256",
    96: "sha384",
    128: "sha512",
}


def help_(function=None):
    """
    Display help information about pphash functions.

    Usage:
        help_()
        help_('ghash')
    """

    if function is None:

        print("""
==================================================
                    pphash
        Python Password Hashing Library
==================================================

Version:
    0.0.1

Functions:
--------------------------------------------------

ghash(plaintext, mode='sha256')
    Create a hash value from plaintext.

    Example:
        ghash('hello')
        ghash('hello', 'sha512')


chash(plaintext, hashvalue, mode='sha256')
    Check whether plaintext matches a hash value.

    Example:
        chash('hello', hashvalue)
        chash('hello', hashvalue, 'sha256')


getmode(hashvalue)
    Detect the hash algorithm based on hash length.

    Example:
        getmode(hashvalue)


gpass(length=10)
    Generate a cryptographically secure random password.

    Example:
        gpass()
        gpass(16)
        gpass(32)


Supported Hash Modes:
--------------------------------------------------
    md5
    sha1
    sha224
    sha256
    sha384
    sha512


Example:
--------------------------------------------------

    from pphash import *

    password = 'MyPassword123'

    hashvalue = ghash(password)

    print(hashvalue)

    if chash(password, hashvalue):
        print('Password is correct')

    print(getmode(hashvalue))

    password = gpass(16)

    print(password)

==================================================
""")

        return

    functions = {
        "ghash": """
ghash(plaintext, mode='sha256')

Create a hash value from plaintext.

Parameters:
    plaintext -> Text that will be hashed.
    mode      -> Hash algorithm. Default: sha256

Example:
    ghash('hello')
    ghash('hello', 'sha512')

Returns:
    str -> Hexadecimal hash value.
""",

        "chash": """
chash(plaintext, hashvalue, mode='sha256')

Check whether plaintext matches a hash value.

Parameters:
    plaintext -> Original text.
    hashvalue -> Hash value to compare.
    mode      -> Hash algorithm. Default: sha256

Example:
    chash('hello', hashvalue)
    chash('hello', hashvalue, 'sha256')

Returns:
    bool -> True if the hash matches.
            False if the hash does not match.
""",

        "getmode": """
getmode(hashvalue)

Detect the hash algorithm based on hash length.

Parameters:
    hashvalue -> Hash value.

Example:
    getmode(hashvalue)

Returns:
    str  -> Detected hash algorithm.
    None -> If the hash length is not recognized.
""",

        "gpass": """
gpass(length=10)

Generate a cryptographically secure random password.

Parameters:
    length -> Password length. Default: 10

Example:
    gpass()
    gpass(16)
    gpass(32)

Returns:
    str -> Randomly generated password.
""",
    }

    if function in functions:
        print(functions[function])
    else:
        print(f"pphash: no help available for '{function}'")


def ghash(plaintext, mode="sha256"):
    """
    Create a hash value from plaintext.

    Returns:
        str: Hexadecimal hash value.
    """

    return new(
        mode,
        plaintext.encode("utf-8")
    ).hexdigest()


def chash(plaintext, hashvalue, mode="sha256"):
    """
    Check whether plaintext matches a hash value.

    Returns:
        bool: True if the hash matches, otherwise False.
    """

    return (
        new(
            mode,
            plaintext.encode("utf-8")
        ).hexdigest()
        == hashvalue
    )


def getmode(hashvalue):
    """
    Detect the hash algorithm based on hash length.

    Returns:
        str: Hash algorithm name.
        None: If the length is not recognized.
    """

    return _HASH_MODES.get(len(hashvalue))


def gpass(length=10):
    """
    Generate a cryptographically secure random password.

    Returns:
        str: Randomly generated password.
    """

    chars = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        """'"-=+_~!@#$%^&*;:(){}\\/?<>,."""
    )

    return "".join(choice(chars) for _ in range(length))