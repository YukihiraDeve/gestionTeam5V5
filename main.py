from itertools import combinations

class Joueur:
    def __init__(self, nom, rank, poste):
        self.nom = nom
        self.rank = rank
        self.poste = poste
        self.value = self.get_value()

    def get_value(self):
        rank_values = {
            "Fer": -3,
            "Bronze": -2,
            "Silver": -1,
            "Gold": 0,
            "Platine": 1,
            "Emeraude": 2,
            "Diamant": 3,
            "Master": 4,
        }
        return rank_values[self.rank]

def equilibrer_teams(joueurs):
    postes = ["Top", "Jungle", "Mid", "Adc", "Support"]
    joueurs_par_poste = {poste: [j for j in joueurs if j.poste == poste] for poste in postes}

    best_diff = float('inf')
    best_teams = None

    for comb in combinations(joueurs, 5):
        team1 = list(comb)
        team2 = [j for j in joueurs if j not in team1]

        if all(any(p.poste == poste for p in team1) for poste in postes) and all(any(p.poste == poste for p in team2) for poste in postes):
            diff = abs(sum(j.value for j in team1) - sum(j.value for j in team2))
            if diff < best_diff:
                best_diff = diff
                best_teams = (team1, team2)

    return best_teams[0], best_teams[1], sum(j.value for j in best_teams[0]), sum(j.value for j in best_teams[1])

def afficher_team(team):
    for joueur in team:
        print(joueur.nom, "-", joueur.rank, "-", joueur.poste)

if __name__ == "__main__":
    joueurs = [
        Joueur("Joueur1", "Emeraude", "Top"),
        Joueur("Joueur2", "Gold", "Jungle"),
        Joueur("Joueur3", "Platine", "Mid"),
        Joueur("Joueur4", "Emeraude", "Adc"),
        Joueur("Joueur5", "Diamant", "Support"),
        Joueur("Joueur6", "Emeraude", "Top"),
        Joueur("Joueur7", "Emeraude", "Jungle"),
        Joueur("Joueur8", "Bronze", "Mid"),
        Joueur("Joueur9", "Silver", "Adc"),
        Joueur("Joueur10", "Gold", "Support"),
    ]

    team1, team2, team1_value, team2_value = equilibrer_teams(joueurs)

    print("Team 1:")
    afficher_team(team1)
    print("Valeur totale de Team 1:", team1_value)

    print("\nTeam 2:")
    afficher_team(team2)
    print("Valeur totale de Team 2:", team2_value)
