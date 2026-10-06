# pphash

### Python Password Hashing Library

`pphash` is a lightweight and beginner-friendly Python library for working with password hashes and generating secure random passwords.

It provides a simple API for:

- 🔐 Creating hash values
- ✅ Verifying passwords against hash values
- 🔎 Detecting hash algorithms
- 🔑 Generating secure random passwords
- 📚 Built-in help for library functions

---

## Features

- Simple and easy-to-use API
- Supports multiple hashing algorithms
- Password hash verification
- Hash algorithm detection
- Cryptographically secure password generation using Python's `secrets` module
- Built-in documentation through `help_()`
- No external dependencies

---

## Installation

Install `pphash` from PyPI:

```bash
pip install pphash
```

---

## Quick Start

Import the library:

```python
import pphash
```

Create a hash:

```python
password = "MyPassword123"

hash_value = pphash.ghash(password)

print(hash_value)
```

Verify the password:

```python
result = pphash.chash(
    password,
    hash_value
)

print(result)
```

Output:

```text
True
```

Detect the hashing algorithm:

```python
mode = pphash.getmode(hash_value)

print(mode)
```

Output:

```text
sha256
```

Generate a secure random password:

```python
password = pphash.gpass(16)

print(password)
```

Example output:

```text
G7@kP!2x#Lm9$qW4
```

---

# Functions

## `ghash()`

Creates a hexadecimal hash value from plaintext.

### Syntax

```python
ghash(plaintext, mode="sha256")
```

### Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `plaintext` | `str` | Required | Text to hash |
| `mode` | `str` | `"sha256"` | Hashing algorithm |

### Example

```python
import pphash

hash_value = pphash.ghash("hello")

print(hash_value)
```

Using another algorithm:

```python
hash_value = pphash.ghash(
    "hello",
    "sha512"
)

print(hash_value)
```

### Return

```text
str
```

Returns the hash as a hexadecimal string.

---

# `chash()`

Checks whether a plaintext value matches a previously generated hash.

### Syntax

```python
chash(plaintext, hashvalue, mode="sha256")
```

### Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `plaintext` | `str` | Required | Original plaintext |
| `hashvalue` | `str` | Required | Hash to compare |
| `mode` | `str` | `"sha256"` | Hashing algorithm |

### Example

```python
import pphash

password = "MyPassword123"

hash_value = pphash.ghash(password)

if pphash.chash(password, hash_value):
    print("Password is correct")
else:
    print("Password is incorrect")
```

### Return

```text
bool
```

Returns:

- `True` if the hash matches
- `False` if the hash does not match

---

# `getmode()`

Attempts to identify the hashing algorithm based on the hexadecimal hash length.

### Syntax

```python
getmode(hashvalue)
```

### Example

```python
import pphash

hash_value = pphash.ghash("hello")

print(pphash.getmode(hash_value))
```

Output:

```text
sha256
```

### Supported Hash Lengths

| Length | Algorithm |
|---:|---|
| 32 | MD5 |
| 40 | SHA-1 |
| 56 | SHA-224 |
| 64 | SHA-256 |
| 96 | SHA-384 |
| 128 | SHA-512 |

### Return

```text
str
```

Returns the detected algorithm name.

If the hash length is not recognized:

```python
None
```

### Important

`getmode()` detects the algorithm based **only on digest length**.

This means it cannot mathematically guarantee which algorithm produced a hash when multiple algorithms could produce the same-length output.

---

# `gpass()`

Generates a cryptographically secure random password.

### Syntax

```python
gpass(length=10)
```

### Parameters

| Parameter | Type | Default | Description |
|---|---|---:|---|
| `length` | `int` | `10` | Password length |

### Example

```python
import pphash

password = pphash.gpass()

print(password)
```

Generate a 20-character password:

```python
password = pphash.gpass(20)

print(password)
```

Example output:

```text
aF7@x!Q2#pL9$wZ4&mK8
```

The generated password can contain:

- Lowercase letters
- Uppercase letters
- Numbers
- Special characters

---

# Built-in Help

`pphash` includes a built-in help function.

Display information about all functions:

```python
import pphash

pphash.help_()
```

You can also request help for a specific function:

```python
pphash.help_("ghash")
```

```python
pphash.help_("chash")
```

```python
pphash.help_("getmode")
```

```python
pphash.help_("gpass")
```

---

# Complete Example

The following example demonstrates the main functionality of `pphash`:

```python
import pphash


# Password
password = "MyPassword123"


# Create hash
hash_value = pphash.ghash(password)

print("Hash:")
print(hash_value)


# Detect hash algorithm
mode = pphash.getmode(hash_value)

print("\nHash mode:")
print(mode)


# Verify password
result = pphash.chash(
    password,
    hash_value
)

print("\nPassword verification:")
print(result)


# Generate a new password
new_password = pphash.gpass(16)

print("\nGenerated password:")
print(new_password)
```

Example output:

```text
Hash:
2cf24dba5fb0a30e...

Hash mode:
sha256

Password verification:
True

Generated password:
G7@kP!2x#Lm9$qW4
```

---

# Supported Algorithms

Currently, `pphash` supports the following algorithms through Python's `hashlib`:

```text
MD5
SHA-1
SHA-224
SHA-256
SHA-384
SHA-512
```

Example:

```python
pphash.ghash("hello", "sha256")
```

or:

```python
pphash.ghash("hello", "sha512")
```

---

# Security Notes

`pphash` is designed to provide a simple interface for hashing and password-related operations.

However, **general-purpose hash functions such as SHA-256 are not recommended for storing user passwords in production applications**.

For password storage, use a password-specific key derivation function (KDF) such as:

- `scrypt`
- `PBKDF2`
- Argon2
- bcrypt

A password should normally be stored together with a unique salt and an appropriate password-based KDF.

`ghash()` is useful for general hashing and learning purposes, but should not be treated as a complete password-storage solution.

---

# Requirements

`pphash` does not require external Python packages.

It uses Python's standard library:

```python
hashlib
secrets
```

---

# Version

Current version:

```text
0.0.1
```

---

# Project Structure

A simple project structure can look like this:

```text
pphash/
│
├── pphash/
│   └── __init__.py
│
├── LICENSE
├── README.md
├── pyproject.toml
└── ...
```

---

# License

This project is licensed under the **MIT License**.

Copyright © 2026 **Mohammed Hamza**

See the [`LICENSE`](LICENSE) file for more information.

---

# Author

**Mohammed Hamza**

Python Developer & Cybersecurity Enthusiast

---

## Contributing

Contributions, suggestions, and improvements are welcome.

If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request.

---

## Disclaimer

This project is provided for educational and development purposes.

The author is not responsible for any damage, data loss, security issues, or misuse resulting from the use of this library.
