# Day 02: Password Generator and Strength Checker (Command-Line Interface)

A command-line tool that generates secure passwords and checks how strong an existing password is, with tips on how to improve it.

## Features

- Generate passwords from 8 to 128 characters
- Choose which character types to include: lowercase, uppercase, numbers, symbols
- Guarantees at least one character from every chosen type
- Check any password and get a score out of 6 with a Weak / Fair / Good / Strong label
- Flags very common passwords straight away
- Hides typing when checking a password

## How to run

Requires Python 3.10 or newer. No extra packages needed.

```bash
cd day-02
python3 main.py
```

## Example

```text
=== Password Tool ===
1. Generate a password
2. Check a password
3. Quit
Choose an option: 1
Password length (8-128, press Enter for 16):
Include lowercase letters? (y/n, press Enter for yes):
Include uppercase letters? (y/n, press Enter for yes):
Include numbers? (y/n, press Enter for yes):
Include symbols? (y/n, press Enter for yes):
Your password is: 1;lW<ViM"QaoGV[t
Strength: Strong (6/6)
```

## What I learned

- Why `secrets` must be used instead of `random` for anything security related
- Using the `string` module for ready-made character sets
- Generator expressions with `join` and `any`
- Guaranteeing one character per type, then shuffling so the pattern isn't predictable
- Building a list first because strings can't be changed or shuffled
- Using a set for fast lookups of common passwords
- Returning two values from a function and unpacking them
- Hiding sensitive input with `getpass`

## Ideas for later

- Check passwords against a large leaked-password list
- Generate passphrases from random words
- Copy the password straight to the clipboard
