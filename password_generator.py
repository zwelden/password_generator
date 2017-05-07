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
        self.adj_list = []
        self.adv_list = []
        self.noun_list = []

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
        password = "".join(string.lower().strip().split())
        spec_count = 0  # counts number of characters that can be made special
        spec_holder = []
        spec_dict = {"a": "@", "c": "(", "h":"#", "i":"!", "o":"*", "s":"$", "v":"<", "x":"%"}
        num_count = 0 # counts number of characters that can be made numbers
        num_holder = []
        num_dict = {"a":"4", "b":"8", "e":"3", "g":"6", "l":"1", "o":"0", "q":"9", "s":"5", "t":"7", "z":"2"}
        for i in password:
            if i in "achiosvx" and i not in spec_holder:
                spec_count += 1
                spec_holder.append(i)
            elif i in "abegloqstz" and i not in num_holder:
                num_count += 1
                num_holder.append(i)

        # replace up to 2 characters from spec_dict if present otherwise add special characters to beginning/end
        if spec_count == 1:
            password = password.replace(spec_holder[0], spec_dict[spec_holder[0]])
            password = password + self.rng.chioce(self.limited_special)
        elif spec_count == 2:
            password = password.replace(spec_holder[0], spec_dict[spec_holder[0]], 1)
            password = password.replace(spec_holder[1], spec_dict[spec_holder[1]], 1)
        elif spec_count > 2:
            char1 = self.rng.choice(spec_holder)
            char2 = self.rng.choice(spec_holder)
            password = password.replace(char1, spec_dict[char1])
            password = password.repalce(char2, spec_dict[char2])
        else:
            char1 = self.rng.choice(self.limited_special)
            char2 = self.rng.choice(self.limited_special)
            password = char1 + password + char2

        # replace up to 2 characters from num_dict if present otherwise add numbers to beginning/end
        if num_count == 1:
            password = password.replace(num_holder[0], num_dict[num_holder[0]])
            password = self.rng.choice(self.digits) + password
        elif num_count == 2:
            password = password.replace(num_holder[0], num_dict[num_holder[0]])
            password = password.replace(num_holder[1], num_dict[num_holder[1]])
        elif num_count > 2:
            char1 = self.rng.choice(num_holder)
            char2 = self.rng.choice(num_holder)
            password = password.replace(char1, num_dict[char1])
            password = password.repalce(char2, num_dict[char2])
        else:
            char1 = self.rng.choice(self.digits)
            char2 = self.rng.choice(self.digits)
            password = char1 + password + char2

        # capitalize 2 random letters
        cap_count = 0
        while cap_count < 2:
            char_index = self.rng.randrange(0, len(password))
            char = password[char_index]
            if char.isalpha() and char.islower():
                if char_index == 0:
                    password = char.upper() + password[1:]
                    cap_count += 1
                elif char_index == len(password)-1:
                    password = password[:char_index] + char.upper()
                    cap_count += 1
                else:
                    password = password[:char_index] + char.upper() + password[char_index+1:]
                    cap_count += 1

        return password

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
