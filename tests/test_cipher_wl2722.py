from cipher_wl2722 import __version__
from cipher_wl2722 import cipher_wl2722

def test_version():
    assert __version__ == '0.1.0'


def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

def test_cipher_word():
    example = 'homeland'
    expected = 'jqogncpf'
    actual = cipher(example,2)
    assert actual == expected
test_cipher_word()
