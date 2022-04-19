# pip install requests
# pip install python-firebase
# pip install git+https://github.com/ozgur/python-firebase

from firebase import firebase
firebase = firebase.FirebaseApplication("https://zombie-email-scraper-default-rtdb.firebaseio.com/", None)




def CofCRUD():
    name = input("Instert name here: ")
    email = input("Instert email here: ")
    phoneNumber = input("Instert phone number here: ")
    
    data = {
        'Name': name,
        'Email':email,
        'Phone':phoneNumber
    }

    result = firebase.post('/Zombie/Information', data)
    print(result)


def RofCRUD():
    result = firebase.get('/Zombie/Information', '')
    print(result)

def UofCRUD():
    firebase.put('/Zombie/Information/-N01Ak-3QXyyMrii2p45', 'Name', 'Blake Yaratch')
    print("Updated")

def DofCRUD():
    firebase.delete('Zombie/Information', '-N01Ak-3QXyyMrii2p45')
    print("Deleted")




def option():
    i = input("Input def you want: ")
    match i:
        case "1":
            CofCRUD()
        case "2":
            RofCRUD()
        case "3":
            UofCRUD()
        case "4":
            DofCRUD()


option()
