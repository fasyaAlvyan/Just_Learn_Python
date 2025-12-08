import random as rd
import string as sr
User_password = ""
final_pass_user = ""
while True:
    try:
        user_input = int(input("\033[36mMasukkan panjang pass(min8/max50) >> \033[0m"))
        if user_input < 8 or user_input > 50:
            print("\033[31m[Minimum panjang password 8 digit]\033[0m")
            continue
        else:
            user_lower = input("\033[36mSertakan huruf kecil? (y/n) >> \033[0m").lower()
            if user_lower == "y":
                User_password += sr.ascii_lowercase
            user_upper = input("\033[36mSertakan huruf besar? (y/n) >> \033[0m").lower()
            if user_upper == "y":
                User_password += sr.ascii_uppercase
            else:
                pass
            user_number = input("\033[36mSertakan angka? (y/n) >> \033[0m").lower()
            if user_number == "y":
                User_password += sr.digits
            else:
                pass
            user_sign = input("\033[36mSertakan tanda baca? (y/n) >> \033[0m").lower()
            if user_sign == "y":
                User_password += sr.punctuation
            else:
                pass
            if user_lower == "n" and user_number == "n" and user_upper == "n" and user_sign == "n" or len(User_password) == 0:
                print("\033[31m[Setujui salah satu jenis karakter]\033[0m")
                continue
            else:
                while True:
                    final_pass = rd.choices(User_password, k = user_input)
                    for password in final_pass:
                        final_pass_user += password
                    print(f"Password anda : \033[32m{final_pass_user}\033[0m")
                    User_recreate = input("\033[36mAnda ingin regenerate password ? (y/n) >> \033[0m").lower()
                    if User_recreate == "y":
                        final_pass_user = ""
                        continue
                    else:
                        print("\033[33m[Terima kasih]\033[0m")
                        break

                break
    except ValueError:
        print("\033[31m[Masukkan angka]\033[0m")
        