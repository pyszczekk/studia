import random
def code_generate(poziom):
    if poziom == "easy":
        a = random.randrange(1, 7, 1)
        b = random.randrange(1, 7, 1)
        c = random.randrange(1, 7, 1)
        d = random.randrange(1, 7, 1)
        while b == a:
            b = random.randrange(1, 7, 1)

        while c == a or c == b:
            c = random.randrange(1, 7, 1)
        while d == a or d == b or d == c:
            d = random.randrange(1, 7, 1)
    elif poziom == "medium":
        a = random.randrange(1, 7, 1)
        b = random.randrange(1, 7, 1)
        c = random.randrange(1, 7, 1)
        d = random.randrange(1, 7, 1)
    elif poziom == "hard":
        a = random.randrange(1, 8, 1)
        b = random.randrange(1, 8, 1)
        c = random.randrange(1, 8, 1)
        d = random.randrange(1, 8, 1)
    code = [a, b, c, d]
    return code
