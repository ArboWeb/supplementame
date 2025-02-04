# Wagtail Starter Kit - Template de démarrage pour projet Django avec Wagtail

Ce modèle de projet Django est conçu pour créer rapidement des projets Wagtail, destiné aux développeurs souhaitant amorcer le développement de leur site Wagtail à l’aide de la commande `wagtail start --template=`. Le modèle inclut des pages, des blocs, des fonctionnalités et des fixtures prédéfinis pour simplifier le processus de configuration initiale.

## Guide de démarrage

1. **Vérifiez que vous avez une version de Python compatible**  Commencez par vérifier que vous avez [version de python compatible](https://docs.wagtail.org/en/stable/releases/upgrading.html#compatible-django-python-versions) installée sur votre ordinateur:

    ```sh
    $ python --version
    # Ou:
    $ python3 --version
    # **Sur Windows** (powershell, avec le launcher Python sous Windows):
    $ py --version
    ```

Vous aurez également besoin d'installer Node.js sur votre système d'exploitation. Le site officiel vous propose des instructions d'installation et des installeurs pour [différents systèmes d'exploitation](https://nodejs.org/en/download/package-manager). Une fois Node installé, redémarrez votre ordinateur.

La commande suivante permet de vérifier si l'installation précédante s'est bien déroulée :

    ```sh
    $ npm --version
    ```

2. **Créez un répertoire de projet et un environnement virtuel**: Configurez le dossier du projet et un environnement virtuel pour isoler les dépendances de votre projet. Vous trouverez des [instuctions pour différents systèmes d'exploitation dans la documentation de Wagtail](https://docs.wagtail.org/en/stable/getting_started/tutorial.html#create-and-activate-a-virtual-environment).

    ```bash
    $ mkdir monproject
    $ cd monproject
    $ python -m venv .venv
    # **On MacOS/Linux**
    $ source .venv/bin/activate
    # **On Windows** (powershell)
    $ .venv/Scripts/activate
    ```


4. **Installez Wagtail**: Installez Wagtail CMS à l'aide de pip depuis votre répertoire de projet avec votre environnement virtuel activé.

Toutes les commandes à partir de ce point doivent être exécutées avec votre environnement virtuel
activé.

    ```bash
    $ pip install wagtail
    ```

5. **Initialisez le projet**: Utilisez la commande `wagtail start` pour créer un nouveau projet en utilisant ce kit de démarrage.

    ```bash
    $ wagtail start --template=https://placepython.com/templates/wagtail-blog.zip monprojet .
    ```

6. **Installez les dépendances de projet**: Installez les dépendances du projet de démarrage dans votre environnement virtuel à l'aide de pip.

    ```bash
    $ pip install -r requirements.txt
    ```

7. **Charger les données initiales**: Chargez les données initiales pour habiller le site de démarrage avec un peu de contenu.

    ```bash
    $ invoke load-data
    ```

8. **Démarrer le serveur**: Lancez le serveur de développement de Django.

    ```bash
    $ invoke start
    ```

9. **Dépendances front-end**: Installer les dépendances front-end avec npm et lancer le serveur de dev front-end

Ouvrez un nouveau terminal à la racine de projet et exécutez les commandes suivantes (Node.js doit être installé
sur votre ordinateur.)

    ```bash
    $ invoke start-front
    ```

11. **Accédez au site et à son admin**: Une fois le serveur lancé, vous pouvez visualiser le site à l’adresse [localhost:8000](http://localhost:8000) et accéder à l’interface d’administration de Wagtail à l’adresse [localhost:8000/admin](http://localhost:8000/admin). Connectez-vous avec les identifiants par défaut fournis par :

    - Username: admin
    - Password: password