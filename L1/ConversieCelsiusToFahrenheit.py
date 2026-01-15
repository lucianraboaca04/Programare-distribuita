
try:
    celsius_input = input("Introduceti temperatura in grade Celsius (folositi . sau , ca separator): ")


    if not celsius_input.strip():
        print("\nEroare: Nu ați introdus nicio valoare.")
    else:

        celsius_curat = celsius_input.replace(',', '.')


        celsius = float(celsius_curat)


        fahrenheit = celsius * 9 / 5 + 32


        print(f"\nTemperatura de {celsius}°C este egală cu {fahrenheit:.2f}°F")


except ValueError:
    print(
        "\nEroare: Ați introdus o valoare invalidă (text sau format incorect). Vă rog să introduceți o cifră numerică.")