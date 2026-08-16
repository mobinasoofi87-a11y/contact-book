contacts=[]

def add_contact():
    name=input("نام: ")
    phone=input("شماره: ")
    contacts.append({"name":name , "phone":phone})

def show_contacts():
    for contact in contacts:
        print(contact["name"] , "-" , contact["phone"])

def search_contact():
    name=input("نام براي جستجو: ")
    for contact in contacts:
        if contact ["name"] ==  name:
            print(contact["name"] , "-" , contact["phone"])
            return
    print("مخاطب پيدا نشد. ")

def delete_contact():
    name=input("نام براي حذف: ")
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print("حذف شد. ")
            return
    print("مخاطب پيدا نشد. ")

while True:
    print("\n 1.اضافه 2.نمايش 3.جستجو 4.حذف 5.خروج .")
    choice=input("انتخواب: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break
    else:
        print("گذينه نامعتبر است. ")
