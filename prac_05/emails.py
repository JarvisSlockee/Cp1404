def main():
    email_and_names = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirm = input("Is your name {}? (Y/N) ".format(name))
        if confirm.upper() != "Y" and confirm != "":
            name = input("Name: ")
        email_and_names[email] = name
        email = input("Email: ")

    for email, name in email_and_names.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name


main()
