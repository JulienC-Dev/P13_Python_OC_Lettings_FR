## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Déploiement

### Overview
Pour pouvoir déployer la chaine CI/CD, les applications suivantes sont nécessaires:

- [Compte GitHub](https://github.com)
- [Compte CircleCi](https://app.circleci.com)
- [Compte Heroku](https://id.heroku.com/login)
- [Compte Sentry](https://sentry.io)


1. Explication de la Pipeline CircleCI

Les modification apportés sur la branch ```master``` déclenche la compilation du projet et les différents tests de 
celui-ci. En cas de succès, la pipeline réalise un déploiement de l'image sur DockerHub et un déploiment sur 
Heroku. En cas d'échecs, le pipeline s'arrête et le déploiement n'est pas réalisé. Les mises à jour sur les branch
n'entraînent pas de déploiement, seulement des tests.

2. Déploiement de la pipeline

Le fichier ```config.yml``` constitue le coeur de la pipeline, il se trouve dans le dossier ```.circleci```.
Vous devez commencer par relier votre compte GitHub avec Circle Ci, puis cliquer sur ajouter le projet 
```P13_Python_OC_lettings```. Selectionner le fichier config.yml prééxistant sur la branch ```master```.

Veuillez ajouter les variables d'environnement pour pouvoire faire fonctionner la pipeline: 

* DOCKER_PASS: le mot de passe docker

* DOCKER_USER: le username docker

* HEROKU_TOKEN: votre API key heroku

* SECRET_KEY_DJANGO: la clé de l'application django

* SENTRY_DNS: le DNS de votre projet Sentry

La variable ```SENTRY_DNS``` permet de relier le projet à Sentry. 

La pipeline est relié maintenant à DockerHub, heroku et sentry

3. Deploiement sur Heroku

Lancer un nouveau projet sous le nom ```app_oc_lettings_100```. Vous pourrez maintenant visualiser le site en ligne lors
d'une exécution réussie de la pipeline.

4. Suivi du projet via Sentry

Pour pouvoir bénéficier des différents services du Sentry, veuillez créer un nouveau projet, et 
choisir le framework Django.
Vous pouvez récupérer le ```SENTRY_DNS``` via le paramétrage

Le pipeline est maintenant en place

### Récupérer une image DockerHub et la faire tourner en local 

Vous pouvez exécuter la commande : 

```docker run --env-file .env -e "PORT=8000" -p 8000:8000 julienx2/app_oc_lettings_site:latest```