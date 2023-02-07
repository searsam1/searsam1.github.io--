
import secrets
import os
import string
import unittest # TestCase

class Test(unittest.TestCase):
    def test_password_length(self, pw):
        assert len(pw) > 10

class Password:    
    letters = string.ascii_letters
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    punc  = string.punctuation
    nums = "".join(str(i) for i in range(10)) * 3
    all_ = letters + lowers + uppers + punc + nums

    @classmethod
    def gen_new_pw(cls):
        block = lambda : b"".join(secrets.choice(cls.all_).encode() for _ in range(10))
        blocks = b"".join(block() for _ in range(10))
        print(blocks)

        
        

p = Password()

p.gen_new_pw()