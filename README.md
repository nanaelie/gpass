# gpass.py

Un générateur de dictionnaires de mots de passe basé sur des permutations, utile pour créer des listes de mots de passe personnalisées.

## Fonctionnalités

- Génère toutes les combinaisons possibles des mots fournis, dans une plage de longueur définie.

- Offre une interface conviviale via la ligne de commande.

- Inclut une barre de progression pour suivre le processus de génération.

---

## Installation

### Prérequis

- **Python 3.x**

- Bibliothèque Python : `tqdm`

### Cloner le projet

Pour cloner le dépôt contenant le script, utilisez la commande suivante :

    git clone https://github.com/nanaelie/gpass.git

Naviguez dans le répertoire cloné :

    cd gpass

### Installer les dépendances

Installez tqdm avec :

    pip install tqdm

Commande de base:

Utilisez la commande suivante pour exécuter le script :

    python gpass.py --min <min_length> --max <max_length> --in <input_file> --out <output_file>


Options

–min : Longueur minimale des mots de passe générés.

–max : Longueur maximale des mots de passe générés.

--in : Chemin du fichier d’entrée contenant les mots (un mot par ligne).

--out : Chemin du fichier de sortie où les mots de passe générés seront sauvegardés.

Exemple

    python gpass.py --min 8 --max 12 --in words.txt --out passwords.txt


Dans cet exemple :

Les mots de passe générés auront une longueur entre 8 et 12 caractères. Les mots fournis dans words.txt seront utilisés pour générer les combinaisons. Les résultats seront enregistrés dans passwords.txt.

Exemples d’applications

* Test de robustesse des mots de passe (pentesting).

* Génération de mots de passe personnalisés pour des outils spécifiques.

* Génération de listes pour des tests en cybersécurité.

Ce projet est sous licence MIT. Vous êtes libre de l’utiliser, le modifier et le distribuer.

Les contributions sont les bienvenues !

Nana Elie
