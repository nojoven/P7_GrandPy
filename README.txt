Dis GrandPy, raconte-nous une histoire�!

PROJET 7�: LE CHATBOT GRANDPY
Trello: https://trello.com/b/4WEml9Lc/p7
GitHub https://github.com/nojoven/P7_GrandPy/tree/master/app
Site Web: https://gpy007.herokuapp.com/

Les objectifs du projet sont les suivants�:

-	Se familiariser avec le d�veloppement web 
(architecture client/serveur)
-	Se familiariser avec l�ex�cution de code dans le navigateur
-	D�velopper une interface interactive dans le navigateur avec HTML, CSS et Javascript ce dernier langage permettant de r�agir aux actions de l�utilisateur
- 	Se familiariser avec les frameworks de d�veloppement web en d�couvrant l�organisation MVT
-	D�couvrir Flask qui est l�un des principaux frameworks utilis�s par les entreprises
-	Apprendre � faire communiquer le code Python et le code Javascript
-	Faire appel � plusieurs APIs Web afin d�afficher des donn�es 	    
-	Utiliser Bootstrap 4, beaucoup utilis� en entreprise pour r�utiliser et combiner rapidement des �l�ments HTML et CSS

Je connaissais HTML, CSS, Bootstrap et Jquery.
On ne peut pas vraiment parler de programmation concernant HTML et CSS cependant obtenir un r�sultat satisfaisant demande beaucoup de pers�v�rance, Bootstrap m�a �t� d�un grand secours,

J�ai surtout appris � utiliser un framework, Flask afin de d�velopper une application.
Il a fallu comprendre comment coder le point d�entr�e de l�application et faire le lien avec les scripts JS. J�ai pu constater aussi � quel point Python �tait lisible compar� � Javascript. 

Une autre �tape importante du projet a �t� l�affichage de la carte Google Maps. J�ai d� cr�er une cl� d�API, appeler deux API (Geocode et Maps Static) et encoder l�image re�ue pour pouvoir l�afficher.

Enfin la derni�re grande �tape a �t� de r�cup�rer les donn�es Wikipedia correspondant � la localisation souhait�e par l�utilisateur, en �liminant les homonymes et en affichant uniquement le r�sum� de la page Wikipedia.

Lancer l'application:
$env:FLASK_APP = "C:\Users\Megaport\Documents\OPC\Projet 7\P7_JOSEPH_Cedric\app\main.py"
flask run

Variables d'environnement
heroku logs -a gpy007 --tail
FLASK_RUN_HOST=${HEROKU_APP_NAME}.herokuapp.com -a gpy007
heroku config:set FLASK_RUN_PORT=$PORT -a gpy007

Fonctionnement: 
1) L'utilisateur pose une question de type "GrandPy connais-tu L'arc de Triomphe?" et appuie sur ENTER
2) Le bot lui r�pond avec une carte google et une description wikip�dia s'il en existe une.

  


