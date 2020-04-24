def create_deck():
    suits = ["copas", "espadas", "paus", "ouros"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Rainha", "Rei", "As"]
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} de {suit}')

    return deck