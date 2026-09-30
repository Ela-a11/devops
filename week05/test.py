def check_version():
    match "3.12":
        case "3.9":
            print("Python 3.9")
        case "3.12":
            print("Python 3.12")
        case _:
            print("Unknown")

check_version()
