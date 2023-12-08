Terminal de supervision

Afin de pouvoir gérer au mieux l'entièreté de votre centre de données, vous avec besoin d'un point d'accès à partir duquel vous pouvez communiquer facilement et rapidement avec toutes vos machines.

Pour cela vous avez connecté une première machine, faisant office de terminal, à une deuxième machine qui elle fait le relais avec toutes les autres machines de votre centre de données. Or, après une erreur de manipulation, vous avez perdu toutes les informations sur le rôle de chacune des machines.

Votre réseau s'apparente à un graph dirigé (https://fr.wikipedia.org/wiki/Graphe_orienté), où une machine m1 ayant accès à une machine m2 ne signifie pas nécessairement que la machine m2 a accès à la machine m1.

Vous devez retrouver votre machine de supervision, qui se trouve être la seule qui est reliée à une seule machine, elle-même reliée à toutes les autres.
Données
Entrée

Ligne 1 : Deux entiers M et C, représentant respectivement le nombre de machines au sein du centre de données et le nombre de connexions entre machines.

Ligne 2 à C+1 : Deux chaînes de charactère m1 et m2, définissant le fait que la machine ayant pour identifiant m1 a une connexion vers la machine ayant pour identifiant m2. m1 et m2 sont toutes deux toujours constituées de 5 lettres en minuscule.

M est compris entre 2 et 100 et C est compris entre M-1 et M*M-M.
Sortie

L'identifiant de la machine répondant au critère. Il en existe toujours une et une seule.
Exemple

Pour l'entrée :

4 4
chene frene
saule chene
hetre saule
saule frene

Votre programme devra renvoyer :

hetre

La machine hetre est reliée à la machine saule qui elle-même est reliée aux deux machines restantes chene et frene. C'est donc bien le terminal de supervision que l'on cherche.
