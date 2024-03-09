#27. Napisati program kojim provjeravati da li String sadrži bar jedan samoglasnik.

s = input("Unesi string: ")

if 'a' not in s:
    if 'e' not in s:
        if 'i' not in s:
            if 'o' not in s:
                if 'u' not in s:
                    print("Nema samoglasnika.")
                else:
                    print("Ima samoglasnika.")
            else:
                print("Ima samoglasnika.")
        else:
            print("Ima samoglasnika.")
    else:
        print("Ima samoglasnika.")
else:
    print("Ima samoglasnika.")