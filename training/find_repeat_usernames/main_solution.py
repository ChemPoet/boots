def find_repeated_usernames(usernames):
    seen = set()
    added_duplicates = set()
    repeated = []

    for username in usernames:
        if username in seen:
            if username not in added_duplicates:
                repeated = repeated + [username]
                added_duplicates.add(username)
        else:
            seen.add(username)

    return repeated
