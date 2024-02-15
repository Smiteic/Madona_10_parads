def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        return "Kļūda: Fails nav atrasts."
    except PermissionError:
        return "Kļūda: Nav atļaujas lasīt failu."
    except Exception as e:
        return f"Kļūda: Neizdevās nolasīt failu. ({e})"

def main():
    file_name = input("Lūdzu, ievadiet faila nosaukumu: ")
    file_extension = input("Lūdzu, ievadiet faila paplašinājumu (piemēram, txt, csv, utt.): ")
    full_file_name = f"{file_name}.{file_extension}"
    file_content = read_file(full_file_name)
    print(file_content)

if __name__ == "__main__":
    main()