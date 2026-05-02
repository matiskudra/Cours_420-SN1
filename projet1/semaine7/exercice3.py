info = {
    "lieu": "Raccon City",
    "date": "2025-07-12",
    "temperatures_C": {
        "Matin": 18.2,
        "Midi": 22.5,
        "Après-midi": 24.1,
        "Soir": 20.3
    }
}

print(f"Températures à Raccon City: {info['date']}")
print()
print(f"\tMatin         : {info['temperatures_C']['Matin']} °C")
print(f"\tMidi          : {info['temperatures_C']['Midi']} °C")
print(f"\tAprès-midi    : {info['temperatures_C']['Après-midi']} °C")
print(f"\tSoir          : {info['temperatures_C']['Soir']} °C")
moyenne = (info['temperatures_C']['Matin'] + info['temperatures_C']['Midi'] + info['temperatures_C']['Soir'] + info['temperatures_C']['Après-midi'])/len(info['temperatures_C'])
print()
print(f"Température moyenne : {round(moyenne, 2)} °C")