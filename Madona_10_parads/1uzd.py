def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        return "Fails nav atrasts."
    except Exception as e:
        return f"Kļūda: {e}"

def main():
    file_path = input("Lūdzu, ievadiet teksta faila ceļu: ")
    file_content = read_text_file(file_path)
    if isinstance(file_content, str):
        print("Faila saturs:")
        print(file_content)
    else:
        print(file_content)

if __name__ == "__main__":
    main()