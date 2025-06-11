

dictionary={"Alice":75,"Jammie":60,"Tyrion":90,"Arya":80,"Daenerys":95,"John":100}
name=input("Enter student's name: ")
if name in dictionary.keys():
    print(name+"'s marks:",dictionary[name])
else:
    print("Student not found")


