import affineCipher, transpositionEncrypt, vigenereCipher
import random

SYMBOLS = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-=!@#$%^&*()_+[];',./{}:\"|<>?")
LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def get_int_key():
    return random.randint(100, 1000000)

def get_str_key():
    return "".join([random.choice(SYMBOLS) for i in range(random.randint(5, 20))])

def get_word_key():
    return "".join([random.choice(LETTERS) for i in range(random.randint(2, 13))])

def get_relatively_prime_key():
    while True:
        key = get_int_key()
        keyA, keyB = affineCipher.getKeyParts(key)
        if affineCipher.checkKeys2(keyA, keyB, "encrypt"):
            break
    return key

def cipherFunction(text: str):
    t = text[:]
    t = vigenereCipher.encryptMessage(get_word_key(), t)
    t = transpositionEncrypt.encryptMessage(get_int_key(), t)
    t = affineCipher.encryptMessage(get_relatively_prime_key(), t)
    return t

def encrypt(text: str, strength: int):
    t = text[:]
    for i in range(strength):
        t = cipherFunction(t)
    return t

if __name__ == '__main__':
    strength = 6
    print(f"Strength: {strength}")
    text = input("Input your text to encrypt > ")
    print("\nEncrypted message:")
    print(encrypt(text, strength))
    print("!!!END!!!")