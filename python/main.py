tekst = input("sprawdz czy palindrom: ")

if tekst[::-1].upper().strip() == tekst[::1].upper().strip():
    print("Palindrom")
else:
    print("Nie Palindrom")

