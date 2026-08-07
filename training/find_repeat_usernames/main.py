def find_repeated_usernames(usernames: str | None):
    unique: set[str] = set()
    repeat: set[str] = list()

    for name in usernames:
        if name == None:
            pass
        elif name not in unique:
            unique.add(name)
        elif name in unique:
            if name not in repeat:
                repeat.append(name)
    return repeat
    pass


usernames = []
find_repeated_usernames(usernames)
