def write_to_file(file_name, user_name):
    try:
        with open(file_name, 'w') as file:
            file.write(user_name)
        print("Vārds veiksmīgi ierakstīts failā.")
    except PermissionError:
        print("Kļūda: Nav atļaujas rakstīt failā.")
    except Exception as e:
        print(f"Kļūda: Neizdevās ierakstīt failā. ({e})")

def main():
    user_name = input("Lūdzu, ievadiet savu vārdu: ")
    file_name = "lietotajs.txt"
    write_to_file(file_name, user_name)

if __name__ == "__main__":
    main()