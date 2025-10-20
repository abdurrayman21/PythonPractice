import random
import string

def Generate_password():
    length = int(input("include desired lenght").strip())
    include_uppercase = input("include uppercase").strip()
    include_digits = input("include digits").strip()
    include_special = input("include special").strip()

    if length < 4:
       print("too short")
       return

    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits  == "yes" else ""
    all_characters = lower + uppercase + special + digits

    required_characters = []
    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase))
    if include_digits == "yes":
        required_characters.append(random.choice(digits))
    if include_special == "yes":
        required_characters.append(random.choice(special))

    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)

    str_password = "".join(password)
    return str_password

password = Generate_password()
print(password)

