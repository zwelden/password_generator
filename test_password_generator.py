import unittest
import re
from .password_generator import PasswordGenerator



class TestPwGen(unittest.TestCase):

    def test_get_options_menu_returns_correct_menu(self):

        correct_menu_str = ("Option 1: Simple Random Password (only letters and digits)\n"
                            "Option 2: Complex Random Password (letters, digits, and !@#$%()^&* )\n"
                            "Option 3: Full Complex Random Passowrd (letters, digits, and all posible special characters)\n"
                            "Option 4: XKCD Password (four random words)\n"
                            "Option 5: XKCD Password with added complexity (four random words with special characters)\n"
                            "Option 6: Complixify password (takes a given string and adds complexity to it, ex: password --> p4$sW*rd)\n")

        password_gen = PasswordGenerator()
        returned_menu_str = password_gen.get_options_menu()
        self.assertEqual(correct_menu_str, returned_menu_str)

    def test_make_simple_password_default_length(self):
        password_gen = PasswordGenerator()
        password_regex = re.compile(r"^[a-zA-Z0-9]{16}$")
        test_password = password_gen.make_simple_password()
        pass_match = password_regex.fullmatch(test_password)
        self.assertTrue(pass_match)

    def test_make_simple_password_32_char_length(self):
        password_gen = PasswordGenerator()
        password_gen.set_length(32)
        password_regex = re.compile(r"^[a-zA-Z0-9]{32}$")
        for _ in range(25):
            test_password = password_gen.make_simple_password()
            pass_match = password_regex.fullmatch(test_password)
            self.assertTrue(pass_match)

    def test_make_basic_complex_password_default_length(self):
        password_gen = PasswordGenerator()
        password_regex = re.compile(r"^[a-zA-Z0-9!@#$%^&*()_\-+=]{16}$")
        test_password = password_gen.make_basic_complex_password()
        pass_match = password_regex.fullmatch(test_password)
        self.assertTrue(pass_match)

    def test_make_basic_complex_password_32_char_length(self):
        password_gen = PasswordGenerator()
        password_gen.set_length(32)
        password_regex = re.compile(r"^[a-zA-Z0-9!@#$%^&*()_\-+=]{32}$")
        for _ in range(25):
            test_password = password_gen.make_basic_complex_password()
            pass_match = password_regex.fullmatch(test_password)
            self.assertTrue(pass_match)

    def test_make_full_complex_password_default_length(self):
        password_gen = PasswordGenerator()
        password_regex = re.compile(r"^[a-zA-Z0-9!\"\#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~]{16}$")
        for _ in range(25):
            test_password = password_gen.make_full_complex_password()
            pass_match = password_regex.fullmatch(test_password)
            self.assertTrue(pass_match)

    def test_make_xkcd_password(self):
        password_gen = PasswordGenerator()
        password_regex = re.compile(r"^[a-z]{16,}$")
        for _ in range(25):
            test_password = password_gen.make_xkcd_password()
            pass_match = password_regex.fullmatch(test_password)
            self.assertTrue(pass_match)

    def test_make_complex_xkcd_password(self):
        password_gen = PasswordGenerator()
        password_regex = re.compile(r"^[a-zA-Z!@#*]{16,}")
        for _ in range(25):
            test_password = password_gen.make_complex_xkcd_password()
            pass_match = password_regex.fullmatch(test_password)
            self.assertTrue(pass_match)

    def test_complexify_password_8_char_2_spec_2_num(self):
        password_gen = PasswordGenerator()
        test_password = "awildend"
        password_regex = re.compile(r"^@[wW]!1[dD]3[nN][dD]$")
        for _ in range(10):
            test_complexified_pass = password_gen.complexify_password(test_password)
            pass_match = password_regex.fullmatch(test_complexified_pass)
            self.assertTrue(pass_match)

    def test_complexify_password_no_subs(self):
        password_gen = PasswordGenerator()
        test_password = "dfjkmnpruwy"
        password_regex = re.compile(r"""^[0-9][!\"\#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~]
                                         [a-zA-Z]{11}
                                         [!\"\#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~][0-9]$""", re.VERBOSE)
        for _ in range(25):
            test_complexified_pass = password_gen.complexify_password(test_password)
            pass_match = password_regex.fullmatch(test_complexified_pass)
            self.assertTrue(pass_match)
