def type_animal(deplacement):
    match deplacement:
        case "vole":
            return "oiseau"
        case "nage":
            return "poisson"
        case "marche":
            return "mammifère"
        case "rampe":
            return "reptile"
        case _:
            return "inconnu"

deplacement = "vole"
print(f"Si je {deplacement}, je suis un {type_animal(deplacement)}.")