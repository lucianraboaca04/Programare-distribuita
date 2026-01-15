def gaseste_multipli():


    x = None
    y = None

    # Bucla pentru a forța input valid pentru ambele numere
    while x is None or y is None:
        try:
            # Citim ambele numere pe o singură linie, separate prin spațiu
            input_linie = input("Introdu două numere întregi, x (multiplu) și y (limită), separate prin spațiu: ")

            # Verificăm input-ul gol
            if not input_linie.strip():
                print("Eroare: Nu ați introdus nicio valoare.")
                continue  # Reîncepem bucla

            # Procesăm input-ul: înlocuim virgula cu punct și apoi split
            valori_str = input_linie.replace(',', '.').split()

            # Verificăm dacă sunt exact două numere introduse
            if len(valori_str) != 2:
                print("Eroare: Vă rog să introduceți exact două numere.")
                continue

            # Convertim la numere intregi (int)
            x = int(valori_str[0])
            y = int(valori_str[1])

            # Verificare suplimentara: Asiguram că x este pozitiv și y e mai mare decât x
            if x <= 0:
                print("Eroare: Numărul x (multiplu) trebuie să fie mai mare decât zero.")
                x = None  # Resetam x pentru a reancepe bucla
            if y <= x:
                print(f"Eroare: Limita y ({y}) trebuie să fie mai mare decât x ({x}).")
                x = None  # Resetam x pentru a reancepe bucla

        except ValueError:
            print("Eroare: Ambele valori trebuie să fie numere întregi valide.")
            # Nu resetam x și y, deoarece x și y raman None și bucla while continua



    print(f"\n--- Multiplii lui {x} mai mici decât {y} ---")

    multiplu = x  # Primul multiplu este chiar x
    gasit_multiplu = False

    while multiplu < y:
        print(multiplu)
        multiplu += x  # Trecem la urmatorul multiplu (x + x + x...)
        gasit_multiplu = True

    if not gasit_multiplu:
        print(f"Nu există multiplii ai lui {x} mai mici decât {y}.")

    print("-----------------------------------------------------")


# Rulăm funcția
gaseste_multipli()