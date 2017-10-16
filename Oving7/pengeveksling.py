from sys import stdin

def min_coins_greedy(coins, value):
    min_coins = 0
    index = len(coins) - 1
    for i in range(len(coins)):
        if coins[index] <= value:
            min_coins += value // coins[index]
            value %= coins[index]
        index -= 1
    return min_coins

def make_memoization_table(table, coins, value):
    # Benytter meg av at jeg kan bruke tidligere tabeller dersom de finnes
    # Dette fordi samme myntsett brukes hver gang
    # Om value er større enn tidligere lagd tabell trenger jeg kun å utvide den gamle tabellen
    # Dersom value er mindre eller lik tidligere tabell, kan jeg bruke den denne tabellen direkte
    t = len(table)
    if value >= t:
        inf = 1000000000
        # Lager liste med hver verdi opp til den ønskede verdien (value)
        # Indeksene representerer tallet vi vil lage
        # Hvert element er minste antall mynter som trengs for å lage verdien (indeksen)
        table += [inf]*(value + 1 - t)
        if t == 0:
            table[0] = 0  # Trenger 0 mynter for å lage 0kr
            t = 1         # For å starte på riktig indeks

        # Utvider gammel tabell ved å starte på indeks t = len(table)
        # For hver i ser vi på hver av de tilgjengelige myntene og finner minste antall mynter som trengs for å lage i
        for i in range(t, value + 1):
            for coin in coins:
                # Her kan vi nå verdien (i) ved å først nå verdien av l = i - coin,
                # (som enten er mulig eller ikke mulig å nå (infinity)),
                # og deretter legge til coin
                if coin < i:
                    l = table[i - coin]
                    if l + 1 < table[i]:
                        table[i] = l + 1
                # Trenger ikke sjekke resten av myntene hvis nåværende mynt er større enn i
                # Dette fordi myntene er sortert i stigende rekkefølge
                elif coin > i:
                    break
                # Hvis verdien finnes i de tilgjengelige myntene, vet vi at 1 er minste antall vi vil trenge
                # Trenger derfor ikke å sjekke for de andre myntene som er tilgjengelig
                else:
                    table[i] = 1
                    break
    return table


def can_use_greedy(coins):
    for i in range(len(coins)-2):
        if coins[i+1] < coins[i]*2:
            return False
    return True


def main():
    coins = sorted([int(c) for c in input().split()])
    method = stdin.readline().strip()
    if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
        for line in stdin:
            print(min_coins_greedy(coins, int(line)))
    else:
        table = []
        for line in stdin:
            # Memoisering, lagrer tabell til senere bruk
            memoization_table = make_memoization_table(table, coins, int(line))
            table = memoization_table
            print(table[int(line)])

main()