import random
import string


class PasswordGenerator:

    def __init__(self):
        self.rng = random.SystemRandom()
        self.letters = string.ascii_letters
        self.digits = string.digits
        self.limited_special = "!@#$%^&*()_-+="
        self.all_special = string.punctuation
        self.new_password = ""
        self.length = 16
        self.xkcd_word_list = []

    def create_xkcd_word_list(self):
        word_dictionary = []
        with open('words.txt') as words:
            for line in words:
                if line[0].isalpha() and len(line) >= 5 and "'" not in line:
                    word_dictionary.append(line[:-1])
            self.xkcd_word_list = word_dictionary

    def set_length(self, length):
        try:
            length = int(length)
            if 8 <= length <= 128:
                self.length = length
            else:
                raise ValueError("Length must be an integer between 8 and 128.")
        except:
            raise TypeError("Length must be and integer")

    def make_random_password(self, pwd_chars):
        password = ""
        for i in range(self.length):
            next_char = self.rng.choice(pwd_chars)
            password += next_char
        return password

    def make_simple_password(self):
        poss_pw_chars = self.letters + self.digits
        return self.make_random_password(poss_pw_chars)

    def make_basic_complex_password(self):
        poss_pw_chars = self.letters + self.digits + self.limited_special
        return self.make_random_password(poss_pw_chars)

    def make_full_complex_password(self):
        poss_pw_chars = self.letters + self.digits + self.all_special
        return self.make_random_password(poss_pw_chars)

    def make_xkcd_password(self):
        if self.xkcd_word_list == []:
            self.create_xkcd_word_list()
        word_dictionary = list(self.xkcd_word_list)
        """ rng.choice() is used as it is much faster than rng.shuffle()
            given size of words.txt (300,000+ words)
            it is unlikely to generate duplicates """
        word_1 = self.rng.choice(word_dictionary)
        word_2 = self.rng.choice(word_dictionary)
        word_3 = self.rng.choice(word_dictionary)
        word_4 = self.rng.choice(word_dictionary)

        password = word_1 + word_2 + word_3 + word_4
        return password

    def make_complex_xkcd_password(self):
        password = self.make_xkcd_password()
        spec_char = "!@#*"
        for _ in range(4):
            index_num = self.rng.randrange(0, len(password))
            char = password[index_num].upper()
            if index_num == 0:
                password = char + password[1:]
            elif index_num == len(password)-1:
                password = password[:index_num] + char
            else:
                password = password[0:index_num] + char + password[index_num+1:]
        for i in range(4):
            index_num = self.rng.randrange(0, len(password))
            char = spec_char[i]
            if index_num == 0:
                password = spec_char + password
            elif index_num == len(password)-1:
                password = password + char
            else:
                password = password[:index_num] + char + password[index_num:]
        return password

    def complexify_password(self, string):

        return None

    def choose_password_type(self):

        return None

    def get_options_menu(self):
        menu = ["Option 1: Simple Random Password (only letters and digits)",
                "Option 2: Complex Random Password (letters, digits, and !@#$%()^&* )",
                "Option 3: Full Complex Random Passowrd (letters, digits, and all posible special characters)",
                "Option 4: XKCD Password (four random words)",
                "Option 5: XKCD Password with added complexity (four random words with special characters)",
                "Option 6: Complixify password (takes a given string and adds complexity to it, ex: password --> p4$sW*rd)"]

        menu_str = ""
        for menu_item in menu:
            menu_str += menu_item + "\n"

        return menu_str
