def main_menu():
    while True:
        print("\n--- Pizza Ordering App ---")
        print("1. Vytvořit objednávku")
        print("2. Platba")
        print("3. Admin menu")
        print("4. Ukončit aplikaci")

        choice = input("Vyberte možnost: ")

        if choice == '1':
            create_order()
        elif choice == '2':
            process_payment()
        elif choice == '3':
            admin_menu()
        elif choice == '4':
            print("Ukončuji aplikaci.")
            break
        else:
            print("Neplatná volba, zkuste znovu.")