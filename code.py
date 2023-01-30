password = input("password : ")
while password != 'example' and count<3 :
    print("access denied")
    password = input("password : ")
while password == "example" :
    print("access accepted")
    break
