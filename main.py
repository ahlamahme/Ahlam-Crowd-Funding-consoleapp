import Ahlam_function as fun
#-------------------start file---------
print("Hi body here Ahlam system :)")
user_choic = input("type (LOGIN) if you are one of our system partner and type (REGISTER) if you are new here;)")
match user_choic:
    case "LOGIN":
         fun.login()
    case "REGISTER":
         fun.register()
    case _:
        print("I can not help you ;)")