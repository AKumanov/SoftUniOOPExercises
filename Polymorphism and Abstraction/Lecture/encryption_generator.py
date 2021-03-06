class EncryptionGenerator:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        result = ""
        if not type(other) == int:
            raise ValueError("You must add a number.")
        for letter in self.text:
            encoded_char = ord(letter) + other
            while encoded_char < 32:
                encoded_char += 95
            while encoded_char > 126:
                encoded_char -= 95
            result += chr(encoded_char)
        return result


some_text = EncryptionGenerator('I Love Python!')
print(some_text + 1)
print(some_text + (-1))

# example = EncryptionGenerator('Super-Secret Message')
# print(example + 20)
# print(example + (-52))
