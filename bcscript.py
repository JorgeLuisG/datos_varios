import bcrypt

for password in ["pass0", "pass1", "pass2", "pass3"]:
    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

    print(password)
    print(hashed)
    print()