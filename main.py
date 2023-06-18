import asyncio
import sys
from moviestarplanet import AsyncClient
import os



async def main():
    # Création d'une instance de AsyncClient
    client = AsyncClient()

    try:
        # Paramètres de connexion
        username = input("Entrez votre nom d'utilisateur : ")
        password = input("Entrez votre mot de passe : ")


        # Connexion
        login_result = await client.login_async(username, password, "fr")

        if login_result.Status == "Success":
            print("Connexion réussie !")
            print("ActorId :", login_result.ActorId)
            print("StarCoins :", login_result.StarCoins)
            print("Fame :", login_result.Fame)
            print("Diamonds :", login_result.Diamonds)
            print("Ticket :", login_result.Ticket)
            print("ProfileId :", login_result.ProfileId)
            print("AccessToken :", login_result.AccessToken)
        else:
            print("Échec de la connexion.")

    except Exception as e:
        print("Une erreur s'est produite :", str(e))

    finally:
        # Fermer la session
        await client.close()


# Rediriger les erreurs vers une sortie vide (null)
sys.stderr = open(os.devnull, 'w')

# Exécuter la coroutine principale
asyncio.run(main())
