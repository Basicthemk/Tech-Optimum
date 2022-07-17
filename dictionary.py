import enchant

def checker(word):
    test = enchant.Dict("en_US")
    if test.check(word) == True:
        return True
    else:
        return False
