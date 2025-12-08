import random
import string

while True:
    try:
        leng_pas = int(input("\033[36mLength Password (Max : 50) >> \033[0m"))
        if leng_pas > 50:
            continue
        number = "1234567890"
        random_char = "@#$_&-+()/*:;?!~`|•√π÷×=°^¥€¢[]"
        lowercase_alp = random.choices(string.ascii_lowercase, k = leng_pas)
        uppercase_alp = random.choices(string.ascii_uppercase, k = leng_pas)
        char = random.choices(random_char , k = leng_pas)
        num = random.choices(number, k = leng_pas)
        post = ""
        for i,b,c,d in zip(lowercase_alp,num,char,uppercase_alp):
            post += i
            post += b
            post += c
            post += d
        result = random.choices(post, k = leng_pas)
        print("\033[35mYour password : \033[0m")
        for i in result:
            print(f"\033[32m{i}\033[0m",end="")
        while True:
            regenerate = input("\n\033[34mRegenerate (y/n) : \033[0m").lower()
            if regenerate == "y":
                result = random.choices(post, k = leng_pas)
                print("\033[35mYour new password : \033[0m")
                for i in result:
                    print(f"\033[32m{i}\033[0m",end="")
                continue
            else:
                break
        break
    except ValueError:
        print("\033[31m [INPUT LENGTH PASSWORD]\033[0m")
