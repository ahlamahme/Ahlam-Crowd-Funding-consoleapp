import datetime
import phonenumbers
import sys
import fileinput
#---------------------------------------------validate date-----------
def is_valid_date(inputDate):
    day, month, year = inputDate.split('/')
    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False
    if (isValidDate):
        return True
    else:
        return False
#---------------------------------------------------------------------
#----------------------------------veiw specific project-----------
def vewi():
    f2 =open("project")
    print("Enter the project name: ")
    text = input()
    lines = f2.readlines()
    for line in lines:
        if text in line:
            print(line)
    f2.close()
#----------------------------------delete project------------------
def delete ():
    # remove a line containing a name
    file_to_read= open("project", 'r')
    lines = file_to_read.readlines()
    file_to_write=open("project", 'w')
    print("Enter file name to delete:")
    deleted_project=input()
    for line in lines:
    # find() returns -1 if no match is found
        if line.find(deleted_project) != -1:
            pass
        else:
                file_to_write.write(line)
#----------------------------------------------------------------------------------
#---------------------------veiw all project ---------------------------------------
def vewi_all_project():
    f2 =open("project")
    print("The projects")
    lines = f2.readlines()
    for line in lines:
            print(line)
    f2.close()
#--------------------------------------edit in project data---------------------------------------
def edit():
    x = input("Enter text to be replaced:")
    y = input("Enter replacement text")
    for l in fileinput.input(files="project"):
        l = l.replace(x, y)
        sys.stdout.write(l)
#---------------------------------------------login----------------------------------------------
def login ():
    my_list = []
    user_name = input(print("please enter username:"))
    f = open("person")
    lines = f.readlines()
    for line in lines:
        if user_name in line:
                print(f"hi{user_name}!")
                user_passwrd = input(print("please write your password:"))
                my_list = line.split(":")
                if user_passwrd == my_list[3]:
                    print("sussfully login")
                    main_menu()
                else:
                    print("wrong passwrd")
        else:
            print("no such user name")
    f.close()
#----------------------create new project---------------------------------------------
def project():
    pfile =open("project","a")
    print("plaese enter project title:")
    ptitle = input()
    print("plaese enter project details:")
    pdetals = input()
    print("plaese enter total target:")
    ttarget = input()
    print("Enter the start date format 'dd/mm/yy' : ")
    while True:
          sdate = input()
          if is_valid_date(sdate):
           break
          else:
             print("wrong date formate")
    print("Enter the end date format 'dd/mm/yy' : ")
    while True:
          edate = input()
          if is_valid_date(edate):
           break
          else:
              print("wrong date formate")
    projects =[ptitle,pdetals,ttarget,sdate,edate]
    x = ":".join(projects)
    pfile.write(x)
    pfile.write("\n")
    pfile.close()
#----------------------------------register--------------------------------------
def register():
    f = open("person",'a')
    print("plaese enter your firstname:")
    fname = input()
    print("plaese enter your lastname:")
    lname = input()
    print("plaese enter your email:")
    email = input()
    print("plaese enter your passwd:")
    password = input()
    print("plaese confirme passwd:")
    while True:                               #check if confirm password = passwrd
      confirm_password = input()
      if password == confirm_password:
       break
      else:
         print("please write the same password")
    print("plaese write your phone:")
    while True:                               #check validation phon number
       phone = input()
       phone = phonenumbers.parse(phone, "EG")
       if phonenumbers.is_possible_number(phone):
        break
       else:
           print("Invalid phone number ! please try again ")
    projects =[fname,lname,email,password,confirm_password,str(phone)]
    x = ":".join(projects)
    f.write(x)
    f.write("\n")
    f.close()
    print("Registration completed successful")
    print("Plese login to sea our amazing system")
    login()
#-------------------------------main project menu------------------------
def main_menu():
  process = input("choose process ( new project - view projects - delete_project- edit project )")
  match process:
    case "new project":
         project()
    case "view projects":
        vewi_all_project()
    case "delete_project":
        delete()
    case "ediet_project":
        edit()
    case _:
        print("No such process wait the new verion of the project ;)")
