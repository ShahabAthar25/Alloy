from lexar.lexar import Lexar


def shell():
    while True:
        text = input(">> ")
        tokens = Lexar(text).make_tokens()
        print(tokens)
