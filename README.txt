Dis GrandPy, raconte-nous une histoire !

PROJET 7 : LE CHATBOT GRANDPY
Trello: https://trello.com/b/4WEml9Lc/p7
GitHub https://github.com/nojoven/P7_GrandPy/tree/master/app
Site Web: https://gpy007.herokuapp.com/

Les objectifs du projet sont les suivants :

-	Se familiariser avec le développement web 
(architecture client/serveur)
-	Se familiariser avec l’exécution de code dans le navigateur
-	Développer une interface interactive dans le navigateur avec HTML, CSS et Javascript ce dernier langage permettant de réagir aux actions de l’utilisateur
- 	Se familiariser avec les frameworks de développement web en découvrant l’organisation MVT
-	Découvrir Flask qui est l’un des principaux frameworks utilisés par les entreprises
-	Apprendre à faire communiquer le code Python et le code Javascript
-	Faire appel à plusieurs APIs Web afin d’afficher des données 	    
-	Utiliser Bootstrap 4, beaucoup utilisé en entreprise pour réutiliser et combiner rapidement des éléments HTML et CSS

Je connaissais HTML, CSS, Bootstrap et Jquery.
On ne peut pas vraiment parler de programmation concernant HTML et CSS cependant obtenir un résultat satisfaisant demande beaucoup de persévérance, Bootstrap m’a été d’un grand secours,

J’ai surtout appris à utiliser un framework, Flask afin de développer une application.
Il a fallu comprendre comment coder le point d’entrée de l’application et faire le lien avec les scripts JS. J’ai pu constater aussi à quel point Python était lisible comparé à Javascript. 

Une autre étape importante du projet a été l’affichage de la carte Google Maps. J’ai dû créer une clé d’API, appeler deux API (Geocode et Maps Static) et encoder l’image reçue pour pouvoir l’afficher.

Enfin la dernière grande étape a été de récupérer les données Wikipedia correspondant à la localisation souhaitée par l’utilisateur, en éliminant les homonymes et en affichant uniquement le résumé de la page Wikipedia.

Lancer l'application:
$env:FLASK_APP = "C:\Users\Megaport\Documents\OPC\Projet 7\P7_JOSEPH_Cedric\app\main.py"
flask run

Variables d'environnement
heroku logs -a gpy007 --tail
FLASK_RUN_HOST=${HEROKU_APP_NAME}.herokuapp.com -a gpy007
heroku config:set FLASK_RUN_PORT=$PORT -a gpy007

Fonctionnement: 
1) L'utilisateur pose une question de type "GrandPy connais-tu L'arc de Triomphe?" et appuie sur ENTER
2) Le bot lui répond avec une carte google et une description wikipédia s'il en existe une.

  


