import random
import string


def create_password(pw_length, pw_type):
    """ creates a strong password pw_length characters long
        and of a given pw_type
        type 1: letters and digits
        type 2: letters, digits, and limited special characters '!@#$%^&*()'
        type 3: letters, digits, and all special characters
    """

    rng = random.SystemRandom()
    letters = string.ascii_letters
    digits = string.digits
    limited_special = "!@#$%^&*()_-+="
    all_special = string.punctuation
    new_password = ""

    if pw_type == "1":
        possible_characters = letters + digits
    elif pw_type == "2":
        possible_characters = letters + digits + limited_special
    else:
        possible_characters = letters + digits + all_special

    for i in range(pw_length):
        new_password += rng.choice(possible_characters)

    return new_password

""" turn each choice section into a function
    mainloop the while portion
    impliment better clear screen
"""

make_new_pw = "Yes"
while make_new_pw not in "Nn":
    print("\n\n\n\n\n\n\n\n\n\n")
    print("What type of password would you like?")
    print("Type 1: Only letters and digits")
    print("Type 2: Letters, digits and a limited number of special characters")
    print("\t\t--> !@#$%^&*()")
    print("Type 3: Letters, digits, and all the special characters")
    print("""\t\t--> ~`!@#$%^&*()_-+={[\}]|\\:;"'<,>.?/""")
    pw_type = input("Enter Type Number:")
    if pw_type not in ["1", "2", "3"]:
        print("Password type must be between 1 and 3")
        continue
    pw_length = input("Enter desired password length (between 8 and 128):")
    try:
        pw_length = int(pw_length)
    except:
        print("Password must be an interget between 8 and 128")
        continue
    if pw_length > 128 or pw_length < 8:
        print("Password must be between 8 and 100")
        continue
    new_password = create_password(pw_length, pw_type)
    print("Your new password is: {}".format(new_password))

    make_new_pw = input("Create new password? (Y/n):")
