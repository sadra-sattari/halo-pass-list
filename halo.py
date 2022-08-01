import os
import string
import time
import threading

print("""
         _   _       _                                   _ _     _
        | | | | __ _| | ___    _ __   __ _ ___ ___      | (_)___| |_
        | |_| |/ _` | |/ _ \  | '_ \ / _` / __/ __|_____| | / __| __|
        |  _  | (_| | | (_) | | |_) | (_| \__ \__ \_____| | \__ \ |_
        |_| |_|\__,_|_|\___/  | .__/ \__,_|___/___/     |_|_|___/\__|
                              |_|

                 1 -  mobile
                 2  - windows and linux
                 

                 """)

def windows():
    os.system("cls")
    print("""
             _   _       _                                   _ _     _
            | | | | __ _| | ___    _ __   __ _ ___ ___      | (_)___| |_
            | |_| |/ _` | |/ _ \  | '_ \ / _` / __/ __|_____| | / __| __|
            |  _  | (_| | | (_) | | |_) | (_| \__ \__ \_____| | \__ \ |_
            |_| |_|\__,_|_|\___/  | .__/ \__,_|___/___/     |_|_|___/\__|
                                  |_|
                                  
                     1 - Install app
                     2  - Run app
                     3 - About me
                     
                     + Notice :  user who use Windows platform  , first should install app 
                     for download usage Libraries 
                     """)
    def install() :
        os.system("pip install tqdm")
        time.sleep(1)
        os.system("pip install colorama")
    def app():
        os.system("cls")
        from tqdm import tqdm
        from colorama import Fore , init
        time.sleep(1.5)
        os.system("cls")
        def logo():
            print(Fore.YELLOW + """
                     _   _       _                                   _ _     _
                    | | | | __ _| | ___    _ __   __ _ ___ ___      | (_)___| |_
                    | |_| |/ _` | |/ _ \  | '_ \ / _` / __/ __|_____| | / __| __|
                    |  _  | (_| | | (_) | | |_) | (_| \__ \__ \_____| | \__ \ |_
                    |_| |_|\__,_|_|\___/  | .__/ \__,_|___/___/     |_|_|___/\__|
                                          |_|
                                          
                                || WELCOME TO MY OWN PASSWORD list maker
            """ + Fore.RESET)
        logo()
        for load in tqdm(range(10) , colour="YELLOW") :
            time.sleep(0.5)
        os.system("cls")
        logo()
        first_name = input(Fore.YELLOW + " Please Enter your target first name :  ")
        last_name = input(Fore.YELLOW + " Please Enter your target last name  :  ")
        user_name = input(Fore.YELLOW + " Please Enter your target user name  :  ")
        nick_name = input(Fore.YELLOW + " Please Enter your target nick name  :  ")
        tel_phone = input(Fore.YELLOW + " Please Enter your target phone number :  ")
        job = input(Fore.YELLOW + " Please Enter your target job :  ")
        country = input(Fore.YELLOW + " Please Enter your target country :  ")
        province = input(Fore.YELLOW + " Please Enter your target province :  ")
        city = input(Fore.YELLOW + " Please Enter your target city :  ")
        pet_name = input(Fore.YELLOW + " Please Enter your target pet name :  ")
        print(Fore.BLUE + " all of your key word saved " + Fore.RESET)
        time.sleep(1)
        os.system("cls")
        print(Fore.YELLOW + """
                 _   _       _                                   _ _     _
                | | | | __ _| | ___    _ __   __ _ ___ ___      | (_)___| |_
                | |_| |/ _` | |/ _ \  | '_ \ / _` / __/ __|_____| | / __| __|
                |  _  | (_| | | (_) | | |_) | (_| \__ \__ \_____| | \__ \ |_
                |_| |_|\__,_|_|\___/  | .__/ \__,_|___/___/     |_|_|___/\__|
                                      |_|

                            || WELCOME TO MY OWN PASSWORD list maker
                            
                            please enter your password length 
                            1 - 6 
                            2 - 7
                            3 - 8
                            4 - 9
                            5 - 10
        """ + Fore.RESET)
        lenght = input(Fore.YELLOW  + "length: ")
        psw = first_name + last_name + user_name + nick_name + tel_phone + job + country + city + province + pet_name
        file = open("halo_passsword.txt", "a")
        def len6():
            for a in psw:
                for b in psw:
                    for c in psw:
                        for d in psw:
                            for e in psw:
                                for f in psw:
                                    time.sleep(0.5)
                                    print(a + b + c + d + e + f)
                                    file.write(a + b + c +e +f + "\n")
        def len7():
            for a in psw:
                for b in psw:
                    for c in psw:
                        for d in psw:
                            for e in psw:
                                for f in psw:
                                    for g in psw:

                                        time.sleep(0.5)
                                        print(a + b + c + d + e + f + g )
                                        file.write(a + b + c + e + f + g+ "\n")
        def len8():
            for a in psw:
                for b in psw:
                    for c in psw:
                        for d in psw:
                            for e in psw:
                                for f in psw:
                                    for g in psw:
                                        for h in psw:
                                                time.sleep(0.5)
                                                print(a + b + c + d + e + f + g +h)
                                                file.write(a + b + c + e + f + g + h + "\n")
        def len9():
            for a in psw:
                for b in psw:
                    for c in psw:
                        for d in psw:
                            for e in psw:
                                for f in psw:
                                    for g in psw:
                                        for h in psw:
                                            for i in psw:
                                                    time.sleep(0.5)
                                                    print(a + b + c + d + e + f + g + h + i )
                                                    file.write(a + b + c + e + f + g + h + i + "\n")
        def len10():
            for a in psw:
                for b in psw:
                    for c in psw:
                        for d in psw:
                            for e in psw:
                                for f in psw:
                                    for g in psw:
                                        for h in psw:
                                            for i in psw:
                                                for j in psw:
                                                    time.sleep(0.5)
                                                    print(a + b + c + d + e + f + g +h +i +j)
                                                    file.write(a + b + c + e + f + g + h + i + j + "\n")

        if lenght == "1" :
            len6()
        elif lenght == "2" :
            len7()
        elif lenght == "3" :
            len8()
        elif lenght == "4" :
            len9()
        elif lenght == "5" :
            len10()
        else:
            from colorama import Fore, init
            init()
            os.system("cls")
            print(Fore.RED + """
                        s____                    _               _____
                        |  _ \ _   _ _ __  _ __ (_)_ __   __ _  | ____|_ __ _ __ ___  _ __
                        | |_) | | | | '_ \| '_ \| | '_ \ / _` | |  _| | '__| '__/ _ \| '__|
                        |  _ <| |_| | | | | | | | | | | | (_| | | |___| |  | | | (_) | |
                        |_| \_\\__,_|_| |_|_| |_|_|_| |_|\__, | |_____|_|  |_|  \___/|_|
                                                         |___/
                """)
            os.system("pause")
    def about_me():
        print("hi")
    select = input("select: ")
    if select ==  "1" :
        install()
    elif select == "2" :
        app()
    elif select == "3" :
        about_me()
    else:
        from colorama import Fore , init
        init()
        os.system("cls")
        print(Fore.RED + """
                s____                    _               _____
                |  _ \ _   _ _ __  _ __ (_)_ __   __ _  | ____|_ __ _ __ ___  _ __
                | |_) | | | | '_ \| '_ \| | '_ \ / _` | |  _| | '__| '__/ _ \| '__|
                |  _ <| |_| | | | | | | | | | | | (_| | | |___| |  | | | (_) | |
                |_| \_\\__,_|_| |_|_| |_|_|_| |_|\__, | |_____|_|  |_|  \___/|_|
                                                 |___/
        """)
        os.system("pause")


def device():
    os.system("clear")
    from tqdm import tqdm
    from colorama import Fore, init
    time.sleep(1.5)
    os.system("clear")
    def logo():
        print(Fore.YELLOW + """
                     _   _       _                                   _ _     _
                    | | | | __ _| | ___    _ __   __ _ ___ ___      | (_)___| |_
                    | |_| |/ _` | |/ _ \  | '_ \ / _` / __/ __|_____| | / __| __|
                    |  _  | (_| | | (_) | | |_) | (_| \__ \__ \_____| | \__ \ |_
                    |_| |_|\__,_|_|\___/  | .__/ \__,_|___/___/     |_|_|___/\__|
                                          |_|

                                || WELCOME TO MY OWN PASSWORD list maker
                                
            """ + Fore.RESET)
    logo()
    for load in tqdm(range(10), colour="YELLOW"):
        time.sleep(0.5)
    os.system("clear")
    logo()
    first_name = input(Fore.YELLOW + " Please Enter your target first name :  ")
    last_name = input(Fore.YELLOW + " Please Enter your target last name  :  ")
    user_name = input(Fore.YELLOW + " Please Enter your target user name  :  ")
    nick_name = input(Fore.YELLOW + " Please Enter your target nick name  :  ")
    tel_phone = input(Fore.YELLOW + " Please Enter your target phone number :  ")
    job = input(Fore.YELLOW + " Please Enter your target job :  ")
    country = input(Fore.YELLOW + " Please Enter your target country :  ")
    province = input(Fore.YELLOW + " Please Enter your target province :  ")
    city = input(Fore.YELLOW + " Please Enter your target city :  ")
    pet_name = input(Fore.YELLOW + " Please Enter your target pet name :  ")
    print(Fore.BLUE + " all of your key word saved " + Fore.RESET)
    time.sleep(1)
    os.system("clear")
    print(Fore.YELLOW + """
                 _   _       _                                   _ _     _
                | | | | __ _| | ___    _ __   __ _ ___ ___      | (_)___| |_
                | |_| |/ _` | |/ _ \  | '_ \ / _` / __/ __|_____| | / __| __|
                |  _  | (_| | | (_) | | |_) | (_| \__ \__ \_____| | \__ \ |_
                |_| |_|\__,_|_|\___/  | .__/ \__,_|___/___/     |_|_|___/\__|
                                      |_|

                            || WELCOME TO MY OWN PASSWORD list maker

                            please enter your password length 
                            1 - 6 
                            2 - 7
                            3 - 8
                            4 - 9
                            5 - 10

        """ + Fore.RESET)
    psw = first_name + last_name + user_name + nick_name + tel_phone + job + country + city + province + pet_name
    file = open("halo_passsword.txt", "a")

    def len6():
        for a in psw:
            for b in psw:
                for c in psw:
                    for d in psw:
                        for e in psw:
                            for f in psw:
                                time.sleep(0.5)
                                print(a + b + c + d + e + f)
                                file.write(a + b + c + e + f + "\n")

    def len7():
        for a in psw:
            for b in psw:
                for c in psw:
                    for d in psw:
                        for e in psw:
                            for f in psw:
                                for g in psw:
                                    time.sleep(0.5)
                                    print(a + b + c + d + e + f + g)
                                    file.write(a + b + c + e + f + g + "\n")

    def len8():
        for a in psw:
            for b in psw:
                for c in psw:
                    for d in psw:
                        for e in psw:
                            for f in psw:
                                for g in psw:
                                    for h in psw:
                                        time.sleep(0.5)
                                        print(a + b + c + d + e + f + g + h)
                                        file.write(a + b + c + e + f + g + h + "\n")

    def len9():
        for a in psw:
            for b in psw:
                for c in psw:
                    for d in psw:
                        for e in psw:
                            for f in psw:
                                for g in psw:
                                    for h in psw:
                                        for i in psw:
                                            time.sleep(0.5)
                                            print(a + b + c + d + e + f + g + h + i)
                                            file.write(a + b + c + e + f + g + h + i + "\n")

    def len10():
        for a in psw:
            for b in psw:
                for c in psw:
                    for d in psw:
                        for e in psw:
                            for f in psw:
                                for g in psw:
                                    for h in psw:
                                        for i in psw:
                                            for j in psw:
                                                time.sleep(0.5)
                                                print(a + b + c + d + e + f + g + h + i + j)
                                                file.write(a + b + c + e + f + g + h + i + j + "\n")
    lenght = input(Fore.YELLOW + "length: ")
    if lenght == "1":
        len6()
    elif lenght == "2":
        len7()
    elif lenght == "3":
        len8()
    elif lenght == "4":
        len9()
    elif lenght == "5":
        len10()
    else:
        from colorama import Fore, init
        init()
        os.system("clear")
        print(Fore.RED + """
                    s____                    _               _____
                    |  _ \ _   _ _ __  _ __ (_)_ __   __ _  | ____|_ __ _ __ ___  _ __
                    | |_) | | | | '_ \| '_ \| | '_ \ / _` | |  _| | '__| '__/ _ \| '__|
                    |  _ <| |_| | | | | | | | | | | | (_| | | |___| |  | | | (_) | |
                    |_| \_\\__,_|_| |_|_| |_|_|_| |_|\__, | |_____|_|  |_|  \___/|_|
                                                     |___/
            """)
        os.system("pause")
    def about_me():
        print("hi")
    select = input("select: ")
    if select == "1":
        install()
    elif select == "2":
        app()
    elif select == "3":
        about_me()
    else:
        from colorama import Fore, init

        init()
        os.system("clear")
        print(Fore.RED + """
                    s____                    _               _____
                    |  _ \ _   _ _ __  _ __ (_)_ __   __ _  | ____|_ __ _ __ ___  _ __
                    | |_) | | | | '_ \| '_ \| | '_ \ / _` | |  _| | '__| '__/ _ \| '__|
                    |  _ <| |_| | | | | | | | | | | | (_| | | |___| |  | | | (_) | |
                    |_| \_\\__,_|_| |_|_| |_|_|_| |_|\__, | |_____|_|  |_|  \___/|_|
                                                     |___/
            """)
        os.system("pause")


platform = input("please enter your device platform: ")

if platform == "1":
    device()
elif platform == "2" :
    windows()
else:
        from colorama import Fore , init
        init()
        os.system("cls")
        print(Fore.RED + """
                s____                    _               _____
                |  _ \ _   _ _ __  _ __ (_)_ __   __ _  | ____|_ __ _ __ ___  _ __
                | |_) | | | | '_ \| '_ \| | '_ \ / _` | |  _| | '__| '__/ _ \| '__|
                |  _ <| |_| | | | | | | | | | | | (_| | | |___| |  | | | (_) | |
                |_| \_\\__,_|_| |_|_| |_|_|_| |_|\__, | |_____|_|  |_|  \___/|_|
                                                 |___/
        """)
        os.system("pause")

os.system("pause")