import os

client_ident = []
client_fullname = []
client_address = []
client_mobile = []
client_email = []
client_gender = []
client_age = []

product_code = []
product_name = []
product_quantity = []
product_unit_val = []


def register_client():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n--- REGISTER CLIENT ---")

    ident = input("Identification: ")

    if ident in client_ident:
        print("Client already exists.")
        input("Press Enter...")
        return

    client_ident.append(ident)
    client_fullname.append(input("Full name: "))
    client_address.append(input("Address: "))
    client_mobile.append(input("Mobile: "))
    client_email.append(input("Email: "))
    client_gender.append(input("Gender: "))
    client_age.append(int(input("Age: ")))

    print("\nClient registered successfully.")
    input("Press Enter...")


def list_clients():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n--- CLIENT LIST ---")

    if len(client_ident) == 0:
        print("No clients registered.")
    else:
        for i in range(len(client_ident)):
            print("-" * 40)
            print("ID:", client_ident[i])
            print("Name:", client_fullname[i])
            print("Address:", client_address[i])
            print("Mobile:", client_mobile[i])
            print("Email:", client_email[i])
            print("Gender:", client_gender[i])
            print("Age:", client_age[i])

    input("\nPress Enter...")


def search_client():
    os.system('cls' if os.name == 'nt' else 'clear')

    ident = input("Enter identification: ")

    if ident in client_ident:
        pos = client_ident.index(ident)

        print("\nClient found")
        print("ID:", client_ident[pos])
        print("Name:", client_fullname[pos])
        print("Address:", client_address[pos])
        print("Mobile:", client_mobile[pos])
        print("Email:", client_email[pos])
        print("Gender:", client_gender[pos])
        print("Age:", client_age[pos])

    else:
        print("Client not found.")

    input("\nPress Enter...")


def update_client():
    os.system('cls' if os.name == 'nt' else 'clear')

    ident = input("Identification to update: ")

    if ident in client_ident:
        pos = client_ident.index(ident)

        client_fullname[pos] = input("New name: ")
        client_address[pos] = input("New address: ")
        client_mobile[pos] = input("New mobile: ")
        client_email[pos] = input("New email: ")
        client_gender[pos] = input("New gender: ")
        client_age[pos] = int(input("New age: "))

        print("Client updated.")
    else:
        print("Client not found.")

    input("\nPress Enter...")


def delete_client():
    os.system('cls' if os.name == 'nt' else 'clear')

    ident = input("Identification to delete: ")

    if ident in client_ident:
        pos = client_ident.index(ident)

        del client_ident[pos]
        del client_fullname[pos]
        del client_address[pos]
        del client_mobile[pos]
        del client_email[pos]
        del client_gender[pos]
        del client_age[pos]

        print("Client deleted.")
    else:
        print("Client not found.")

    input("\nPress Enter...")


def register_product():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n--- REGISTER PRODUCT ---")

    code = input("Code: ")

    if code in product_code:
        print("Product already exists.")
        input("Press Enter...")
        return

    product_code.append(code)
    product_name.append(input("Product name: "))
    product_quantity.append(int(input("Quantity: ")))
    product_unit_val.append(float(input("Unit value: ")))

    print("Product registered.")
    input("Press Enter...")


def list_products():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n--- PRODUCT LIST ---")

    if len(product_code) == 0:
        print("No products registered.")
    else:
        for i in range(len(product_code)):
            print("-" * 40)
            print("Code:", product_code[i])
            print("Name:", product_name[i])
            print("Quantity:", product_quantity[i])
            print("Unit value:", product_unit_val[i])

    input("\nPress Enter...")


def search_product():
    os.system('cls' if os.name == 'nt' else 'clear')

    code = input("Product code: ")

    if code in product_code:
        pos = product_code.index(code)

        print("\nProduct found")
        print("Code:", product_code[pos])
        print("Name:", product_name[pos])
        print("Quantity:", product_quantity[pos])
        print("Unit value:", product_unit_val[pos])

    else:
        print("Product not found.")

    input("\nPress Enter...")


def update_product():
    os.system('cls' if os.name == 'nt' else 'clear')

    code = input("Code to update: ")

    if code in product_code:
        pos = product_code.index(code)

        product_name[pos] = input("New name: ")
        product_quantity[pos] = int(input("New quantity: "))
        product_unit_val[pos] = float(input("New value: "))

        print("Product updated.")
    else:
        print("Product not found.")

    input("\nPress Enter...")


def delete_product():
    os.system('cls' if os.name == 'nt' else 'clear')

    code = input("Code to delete: ")

    if code in product_code:
        pos = product_code.index(code)

        del product_code[pos]
        del product_name[pos]
        del product_quantity[pos]
        del product_unit_val[pos]

        print("Product deleted.")
    else:
        print("Product not found.")

    input("\nPress Enter...")


def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("===================================")
    print("      MARKET MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Register client")
    print("2. Register product")
    print("3. List clients")
    print("4. List products")
    print("5. Search client")
    print("6. Search product")
    print("7. Update client")
    print("8. Update product")
    print("9. Delete client")
    print("10. Delete product")
    print("11. Exit")
    print("===================================")


while True:

    main_menu()

    option = int(input("Select an option: "))

    if option == 1:
        register_client()

    elif option == 2:
        register_product()

    elif option == 3:
        list_clients()

    elif option == 4:
        list_products()

    elif option == 5:
        search_client()

    elif option == 6:
        search_product()

    elif option == 7:
        update_client()

    elif option == 8:
        update_product()

    elif option == 9:
        delete_client()

    elif option == 10:
        delete_product()

    elif option == 11:
        print("Goodbye!")
        break

    else:
        input("Invalid option. Press Enter...")
