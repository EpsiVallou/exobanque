import uuid
from abc import ABC


class Compte(ABC):
    """
        Abstract class Compte
    """
    def __init__(self, nom_proprietaire, **kwargs):
        self.nom_proprietaire = nom_proprietaire
        self.numero_compte = uuid.uuid4()
        self.solde = 0

    def retrait(self, montant=0):
        if montant > 0:
            if montant > self.solde:
                raise Exception("Vous avez demandé plus d'argent que stocké, retrait annulé")
            else:
                self.solde -= montant
                print(f"Votre fonds est maintenant de {self.solde}")
        else:
            raise Exception("Veuillez donner une valeur positive")

    def versement(self, montant=0):
        if montant > 0:
            self.solde += montant
        else:
            raise Exception("Veuillez donner une valeur positive")

    def afficherSolde(self):  # pragma: no cover
        print(f"Votre balance est de {self.solde} €.")

    def __repr__(self):
        return f"CompteCourant - Solde : {self.solde}"


class CompteCourant(Compte):
    def __init__(self, nom_proprietaire, autorisation_decouvert= -10, pourcentage_agios=10, **kwargs):
        super().__init__(nom_proprietaire)
        self.autorisation_decouvert = autorisation_decouvert
        self.pourcentage_agios = pourcentage_agios / 100
        print(f"Vous, {nom_proprietaire}, avez créer un compte courant d'une solde de départ de {self.solde}.")

    def appliquer_agios(self,montant):
        print("Votre compte est dans le rouge. Les agios s'appliquent. Ah ah.")
        if self.solde - montant < self.autorisation_decouvert:
            raise Exception("Ce retrait vous passerai en dessous de votre autorisation de découvert. Retrait annulé.")
        else:
            self.solde -= abs(self.solde * self.pourcentage_agios)

    # def retrait(self, montant=0):  # Commenter cette ligne pour les tests de retrait d'une somme supérieure aux fonds
        if montant > 0:
            if montant > self.solde + self.autorisation_decouvert:
                self.appliquer_agios(montant)
            else:
                self.solde -= montant
                print(f"Votre fonds est maintenant de {self.solde}")
        else:
            raise Exception("Veuillez donner une valeur positive")


class CompteEpargne(Compte):
    def __init__(self, nom_proprietaire, **kwargs):
        super().__init__(nom_proprietaire)
        self.pourcentage_interets = 8 / 100
        print(f"Vous, {nom_proprietaire}, avez créer un compte épargne d'une solde de départ de {self.solde}.")
        print(f"Le numéro de votre compte est {self.numero_compte}")

    def appliquer_interets(self):
        self.solde += self.solde * self.pourcentage_interets
        print(f"Les intérêts ({self.pourcentage_interets}) sont appliqués.")


print("Bonsoir")
print("c est lab anquela")
while False:  # passer False pour les tests auto, passer True pour tester soi-même
    print("apuyér sûr 1 pour que fous cré et un conte")
    print("2 pour fermer le programme")
    userPrompt = input("Que veuillez vous faisez")
    print(f"fous aveé cri {userPrompt}")
    if userPrompt == "1":
        print("créè un  contpe")
        accountInput = input("apui sur un pou fere 1 comptep qui courent, 2eux puor compet et pargn")
        if accountInput == "1":
            userName = input("cré un courant. cestquoi ton ptit non")
            userCompteCourant = CompteCourant(userName)
            gereCompte = True
            while gereCompte:
                print("1 pour quitter la gestion du compte")
                print("2 pour faire un versement")
                print("3 pour faire un retrait")
                userCompteCourant.afficherSolde()
                userManage = input(f"Que voulez-vous")
                if userManage == "1":
                    gereCompte = False
                elif userManage == "2":
                    try:
                        userVerse = int(input("Combien d'argent voulez vous verser ?"))
                        userCompteCourant.versement(userVerse)
                    except:
                        raise Exception("Mauvaise valeur entrée: DEATH")
                elif userManage == "3":
                    try:
                        userRetire = int(input("Combien voulez vous retirer ?"))
                        userCompteCourant.retrait(userRetire)
                    except:
                        raise Exception("PAS BON PAS BON")
                else:
                    print("Lapin compris")
        elif accountInput == "2":
            userName = input("et par gneu gneu gneu. commen ttut appel")
            userCompteEpargne = CompteEpargne(userName)
            gereCompte = True
            while gereCompte:
                print("1 pour quitter la gestion du compte")
                print("2 pour faire un versement")
                print("3 pour faire un retrait")
                print("4 pour appliquer les intérêts")
                userCompteEpargne.afficherSolde()
                userManage = input(f"Que voulez-vous")
                if userManage == "1":
                    gereCompte = False
                    print("Quitte la gestion de compte.")
                elif userManage == "2":
                    try:
                        userVerse = int(input("Combien d'argent voulez vous verser ?"))
                        userCompteEpargne.versement(userVerse)
                    except:
                        raise Exception("Mauvaise valeur entrée: DEATH")
                elif userManage == "3":
                    try:
                        userRetire = int(input("Combien voulez vous retirer ?"))
                        userCompteEpargne.retrait(userRetire)
                    except:
                        raise Exception("PAS BON PAS BON")
                elif userManage == "4":
                    userCompteEpargne.appliquer_interets()
                else:
                    print("Raté. Essaie encore.")
        else:
            print("bah alors Jack, c'est la piquette Jack")
    elif userPrompt == "2":
        print("Quitte le programme")
        break
    else:
        print("T'es MAUVAIS !")
