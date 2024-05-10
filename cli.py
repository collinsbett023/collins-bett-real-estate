from helpers import (exit_program, list_properties, list_clients, list_contracts, list_realtors, create_realtor,
                     create_client, create_contract, create_property, delete_contract, delete_realtor, delete_client,
                     delete_property, find_contract_by_id, find_property_by_id, find_client_by_id, find_realtor_by_id,
                     owner_name, contract_details)


def menu():
    print("\nWelcome to Real Estate Application, Please select an option")
    print("0 -> Exit the program\n")
    print("1 -> List all Properties")
    print("2 -> List all Clients")
    print("3 -> List all Contracts")
    print("4 -> List all Realtors")

    print("5 -> Add Property")
    print("6 -> Add Client")
    print("7 -> Add Contract")
    print("8 -> Add Realtor")

    print("9 -> Delete Property")
    print("10 -> Delete Client")
    print("11 -> Delete Realtor")
    print("12 -> Delete Contract")

    print("13 -> Find Property by id:")
    print("14 -> Find Client by id:")
    print("15 -> Find Realtor by id:")
    print("16 -> Find Contract by id:")
    print("17 -> Get the property owner: ")
    print("18 -> Get the contract details: \n")


def main():
    while True:
        menu()
        selection = input("---> ")
        if selection == "0":
            exit_program()
        elif selection == "1":
            list_properties()
        elif selection == "2":
            list_clients()
        elif selection == "3":
            list_contracts()
        elif selection == "4":
            list_realtors()
        elif selection == "5":
            create_property()
        elif selection == "6":
            create_client()
        elif selection == "7":
            create_contract()
        elif selection == "8":
            create_realtor()
        elif selection == "9":
            delete_property()
        elif selection == "10":
            delete_client()
        elif selection == "11":
            delete_realtor()
        elif selection == "12":
            delete_contract()
        elif selection == "13":
            find_property_by_id()
        elif selection == "14":
            find_client_by_id()
        elif selection == "15":
            find_realtor_by_id()
        elif selection == "16":
            find_contract_by_id()
        elif selection == "17":
            owner_name()
        elif selection == "18":
            contract_details()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
