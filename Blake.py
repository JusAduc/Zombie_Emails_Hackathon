# pip install requests
# pip install python-firebase
# pip install git+https://github.com/ozgur/python-firebase
# FirebaseInstallations.getId()

from firebase import firebase
firebase = firebase.FirebaseApplication("https://zombie-email-scraper-default-rtdb.firebaseio.com/", None)




def Create():
    name = input("Insert name here: ")
    email = input("Insert email here: ")
    phoneNumber = input("Insert phone number here: ")
    
    data = {
        'Name': name,
        'Email':email,
        'Phone':phoneNumber
    }

    result = firebase.post(f'/Zombie/Information/{name}', data)
    print(result)

def Read():
    userName = input("Input name you would like to read: ")
    result = firebase.get(f'/Zombie/Information/{userName}', '')
    print(result)

def Update():
    userName = input("Input name you would like to update: ")
    userInput = input("Input the subject you would like to change (Email, Name, Phone): ")
    userInput2 = input("Input what you would like to change it to: ")
    firebase.put(f'/Zombie/Information/{userName}/-N02rTKR0OYxvwfPl_S1', userInput, userInput2)
    print("Updated")

def Delete():
    userName = input("Input name you would like to delete: ")
    firebase.delete(f'Zombie/Information/{userName}', "")
    print("Deleted")




def option():
    i = input("Input def you want: ")
    match i:
        case "C":
            Create()
        case "R":
            Read()
        case "U":
            Update()
        case "D":
            Delete()


option()
