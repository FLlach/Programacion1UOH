paris = {
    'país': 'Francia',
    'idioma': 'Francés',
    'moneda': 'Euro'
}

tokio = {
    'país': 'Japón',
    'idioma': 'Japonés',
    'moneda': 'Yen'
}

nueva_york = {
    'país': 'Estados Unidos',
    'idioma': 'Inglés',
    'moneda': 'Dólar estadounidense'
}

rancagua = {
    'país': 'Chile',
    'idioma': 'español',
    'moneda': 'Peso Chileno'
}

lugares_favoritos = {
    'Ana': [paris, tokio],
    'Luis': [nueva_york],
    'Marta': [paris, nueva_york],
    'Felipe':[rancagua, tokio]
}


for persona, ciudades in lugares_favoritos.items():
    print(f"\n{persona} quiere visitar:")
    for ciudad in ciudades:
        print(f"- {ciudad['país']} donde se habla {ciudad['idioma']} y se usa {ciudad['moneda']}.")
