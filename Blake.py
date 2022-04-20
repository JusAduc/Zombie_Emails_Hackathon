# pip install requests
# pip install python-firebase
# pip install git+https://github.com/ozgur/python-firebase
# FirebaseInstallations.getId()

from firebase import firebase
firebase = firebase.FirebaseApplication("https://zombie-email-scraper-default-rtdb.firebaseio.com/", None)




def Create():
    name = input("Insert name here: ")
    email = input("Insert email here: ")
    
    newName = name.lower()
    print(newName)
    
    data = {
        'name': newName,
        'email':email
    }

    result = firebase.post(f'/Zombie/Information/{newName}', data)
    
    global x
    x = result.get('name')
    print (x)
    
    # print (list(iter(result)))
    
    # for i in result:
    #     print( i, result[i])
    
    print(result.keys())
    print(result)

def Read():
    userName = input("Input name you would like to read: ")
    newName = userName.lower()
    
    result = firebase.get(f'/Zombie/Information/{newName}', '')
    
    # x = result.get("Name")
    # print(x)
    for i in result:
        print(i)
    print(result)

def Update():
    userName = input("Input name you would like to update: ")
    userInput = input("Input the subject you would like to change (Email, Name): ")
    userInput2 = input("Input what you would like to change it to: ")
    
    newName = userName.lower()
    newUserInput = userInput.lower()
    newUserInput2 = userInput2.lower()
    
    result = firebase.get(f'/Zombie/Information/{newName}', '')
    for x in result:
        print(x)
    # x= result.get('name')
    # print(x)
    
    if (newUserInput=="name"):
        result = firebase.put(f'/Zombie/Information/{newName}/{x}', newUserInput, newUserInput2)
    
    
    
    print("Updated")

def Delete():
    userName = input("Input name you would like to delete: ")
    newName = userName.lower()

    firebase.delete(f'Zombie/Information/{newName}', "")
    print("Deleted")




def option():
    i = input("Input C R U D: ")
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
