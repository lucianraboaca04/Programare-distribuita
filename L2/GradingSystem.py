def sistem_de_notare():
    """Program care citeste un scor procentual si afiseaza nota corespunzatoare."""

    try:
        # 1. Citirea input-ului de la utilizator
        scor_input = input("Introduceti scorul procentual (0-100): ")

        # Pre-procesare: Inlocuim virgula cu punct 
        scor_curat = scor_input.replace(',', '.')

        # 2. Conversia la float. Aici poate aparea ValueError
        scor = float(scor_curat)

        # 3. Verificarea Validității (Intervalul 0-100)
        if scor < 0 or scor > 100:
            print("\nEroare: Scorul trebuie să fie o valoare între 0 și 100.")
            return  # Ieșim din funcție

        # 4. Structura de Decizie (if, elif, else)
        nota = ""

        if scor >= 90:
            nota = "A"
        elif scor >= 80:
            # Nu trebuie sa verificam si scor <= 89, pentru ca daca nu a intrat in primul IF,
            # automat scorul este < 90.
            nota = "B"
        elif scor >= 70:
            nota = "C"
        elif scor >= 60:
            nota = "D"
        else:
            nota = "F"

        # 5. Afișarea Rezultatului
        print(f"\nScorul dvs. de {scor:.2f}% corespunde Notei: {nota}")

    except ValueError:
        # Prindem eroarea dacă input-ul nu poate fi convertit la float (ex: text invalid)
        print("\nEroare: Vă rugăm să introduceți doar o valoare numerică validă.")


# Rulam funcția
sistem_de_notare()