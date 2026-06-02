---
title: "Présentation Android"
date: "2010-05-13T13:25:45"
lastmod: "2010-05-13T13:25:45"
url: "/2010/05/13/presentation-android/"
summary: "Rappel généraux sur Android Google a annoncé Android en 2007. Le marché visé est principalement le téléphone mobile mais il peut facilement s’étendre à n’importe quel dispositif mobile. Android a été réalisé autours des choix suivants : ouvrir les possibilités des terminaux (open source, modérer les applications à posteriori, pas d’IDE obligatoire, personnalisation, applications internes […]"
author: "Yannick Grenzinger"
canonicalURL: "https://ux-fr.com/2010/05/13/presentation-android/"
draft: false
categories: ["Android", "Techno"]
tags: ["Android", "Mobile"]
aliases: ["/2010/05/13/presentation-android"]
---
[![minority_report - interactive UI](/wp-content/uploads/2010/05/Android1.png "Logo Android")](/wp-content/uploads/2010/05/Android1.png)

**Rappel généraux sur Android**

Google a annoncé Android en 2007. Le marché visé est principalement le téléphone mobile mais il peut facilement s’étendre à n’importe quel dispositif mobile. Android a été réalisé autours des choix suivants :

- ouvrir les possibilités des terminaux (open source, modérer les applications à posteriori, pas d’IDE obligatoire, personnalisation, applications internes ou tierces logées à la même enseigne)

- rendre accessible toutes les fonctionnalités

- réduire les couts de R&D et de réalisation d’applications (s’appuyer sur des standards java/XML)

- promouvoir une expérience utilisateur plus riche et sans besoin de notice

- réunir les acteurs majeurs dans l’ Open Handset Alliance, travailler avec les constructeurs et les opérateurs.

On remarque déjà de forte différence dans la philosophie avec ces concurrents notamment Apple.
 Android a déjà sorti plusieurs SDK apportant diverses fonctionnalités (le dernier étant le 2.1).

**Le marché d’Android**

Google a décidé (à l’origine) de ne pas créer un téléphone unique mais de travailler en collaboration avec les constructeurs de téléphone. De nombreux constructeurs ont lancé leur téléphone sous Android et à différent niveau du SDK. Le marché s’est donc très vite fragmenté avec différentes spécifications matérielles et un respect plus ou moins suivi des consignes de Google (SDK bloqué par exemple). Cette segmentation est à la fois la force et un des plus gros défauts pour Google qui a donc décidé de sortir le Nexus One pour donner leur vision d’un téléphone sous Android. La fragmentation est surtout un problème pour les développeurs qui doivent gérer plusieurs SDK et matériels (la taille de l’écran ? la présence d’un clavier ? GPS ?).

Google a aussi lancé son « Android Market ». Les applications y sont triées par zones géographiques ou types. Le prix des applications va de 0.99 à 200 euros (limitation de Google) avec bien sur les applications gratuites. Les revenus des achats sont répartis à 70% pour le développeur et 30% pour Google. L’inscription coute 25$ par an (contre 100$ pour Apple). La publicité est bien sur en projet de par le coeur de métier de Google.
 Quelques chiffres : 6 000 applications en juin, 22 000 en janvier 2010, 39% payante, 16% jeux, une augmentation forte du nombre d’applications.

Le développement d’une application Android représente quand même des difficultés :

- un framework difficile pour faire du travail pointu

- il faut penser java en environnement hostile

- uns système de paiement imposé : Checkout (contre Itunes sur Apple).

- Annulation des achats sous 48h : bien pour l’utilisateur mais problématique pour le développeur.

- Interaction actuellement trop faible entre le développeur et le potentiel client (descriptif avec uniquement 320 caractères et un screenshot, market uniquement visible par le téléphone).

De plus le succès d’Android est bien sur conditionné par la qualité du terminal. Cependant les pronostiques envers Android sont plutôt bons par exemple Gartner le place devant Apple en 2012 avec une petite avance.
 Le développement des applications va se partager entre les applications disponibles par l’intermédiaire du navigateur web et les applications natives.

**L’architecture d’Android**

![Architecture Android](/migrated-media/system-architecture-cabc9586f595.jpg "Architecture Android")

Comme le montre le schéma ci-dessus, la plateforme Android est basée sur 5 couches :

- un noyau linux. 2.6 qui fournit les drivers nécessaires

- un ensemble d’API C/C++ fournissant des fonctionnalités de plus haut niveau (SQLite, OpenGL ES 2.0…)

- un framework java exploitable par toutes les applications s’exécutant sur la machine virtuelle Dalvik

- un ensemble d’application déjà fourni couvrant les besoins standards.

Le noyau Linux offre la possibilité de créer des applications natives en C. Un des coeurs d’Android est bien sur la machine virtuelle Dalvik. Celle-ci ne correspond pas à une JVM standard. Elle a été réécrite pour correspondre aux besoins et limitations d’un téléphone mobile : un processeur lent, peu de mémoire, pas de swap, une batterie.

Si l’API et le langage sont quasi équivalents à Java 5 SE, le bytecode généré est spécifique (le code Dalvik interprété est contenu par un fichier .dex). De plus il y a de nombreuses différences plus ou moins contraignantes :

- il n’y pas de compilation à la volée

- les tables de constantes sont simplifiées

- il est impossible de faire la programmation orientée aspect

- le garbage collector est encore peu évolué.

Tout ceci nécessite des optimisations manuelles et spécifiques (voir chapitre bonnes pratiques). L’ensemble du code et des ressources est contenue dans un fichier nommé apk qui représente l’application.

Chaque application vit dans son propre monde. Par défaut une application est lancé dans un processus Linux contenant sa propre machine virtuelle ce qui permet de garantir une forte étanchéité entre les applications. Par défaut, chaque application à son propre utilisateur avec ces propres permissions. En conséquence, les fichiers d’une application ne sont visibles que par elle même mais il existe bien sur des moyens de les exporter. Il reste quand même possible de faire correspondre ces éléments pour différentes applications.
 Le code Java peut faire appel à l’API bas niveau par JNI.

Google propose un outillage dédié au développement : Android Development Toolkit disponible sur Windows (x86), Mac et Linux. Cet outil s’intègre directement à Eclipse avec le débugage, les logs et un éditeur d’interface graphique.
 Il y aussi d’autres outils tel que le hierarchy viewver, le Dalvik Debug Monitor Service…

**Anatomie d’une application Android**

Une application Android est donc principalement composée de code Java et fichiers XML. Le point central est le descripteur de l’application ou « AndroidManifest.xml » qui permet de configurer finement l’application ainsi que ces composants.

Elle se compose autour de quatre composants :

- « Actity » : les écrans

- « Service » : les services tournant en fond de tache

- « Content provider » : les fournisseurs de contenu

- « broadcast receiver » : les récepteurs des événements externes par exemple un appel.

Par défaut, ces composants ne sont pas accessible par une autre application. Pour qu’une application B utilise un composant de A, il faut déclarer une permission. L’utilisateur est informée des APIs utilisées par une application.
 Il n’y a pas de point d’entrée principal dans une application. Le système démarre le processus d’une application quand un des composants est requis.

Chaque activité représente un écran indépendant. L’interface utilisateur peut ainsi être composée d’une seule activité ou de plusieurs. Dans ce cas, chaque activité est chargée de lancer la suivante. L’ensemble des activités d’une application est géré par une hiérarchie attachée à une tache. La gestion de cette tache et de sa liste d’activité est entièrement configurable mais complexe.
 L’organisation d’une activité se construit sur un arbre dont la racine est un ViewGroup, les noeuds des layouts ou Viewgroup (linéaire, relatif, absolu, table …) et les feuilles les composants ou Views (boutons, liste de sélection, zone de texte…). Les vues parentes définissent l’agencement de leurs enfants. Cet agencement peut être décrit soit entièrement dans le code Java soit en XML ce qui permet de proposer facilement plusieurs dispositions (par exemple mode portrait et paysage). Les éléments XML sont bien sur accessible à partir de leur identifiants dans le code java. La description XML ne nuit pas à la performance vu qu’elle est compilée donc elle est à favoriser. Cependant, dans le cadre d’une interface dynamique, il faut passer obligatoirement par le code Java.
 Cette complexité n’est pas du tout visible du coté utilisateur.

Les services n’ont pas d’interface visuelle mais tournent en tache de fond pour une période de temps indéterminée. Le meilleur exemple est un lecteur de musique qui parcourt une liste de chansons.
 Comme les activités et les autres composants, les services tournent dans le thread principal du processus de l’application. Il est donc souvent nécessaire de les lancer dans un autre thread pour qu’il ne bloque pas l’application.

Les composants communiquent par l’intermédiaire d’ « Intent » ou intentions qui représente un message. Ce message contient les informations utiles au destinataire : l’action à effectuer et les données sur lesquelles travailler. Les données sont contenues dans un Bundle qui permettent de contenir une série de données (clés-valeurs, sérialisation ..).
 Il y a deux types d’intention :

- explicite qui sert au sein d’une même application. Le nom du composant est indiqué.

- Implicite qui permet d’activer une application qu’on ne connait pas. Le système cherche alors le composant le plus approprié ce qui permet un couplage lâche entre applications et composants.

Les composants sont associés à des filtres d’intentions qui peuvent recevoir des intentions, publient les fonctionnalités des composants et délimitent les intentions que peut traiter un composant.

Il est possible de gérer les processus des composants dans le fichier AndroidManifest. Chaque composant est instancié dans le thread principal du processus spécifié. Il faut donc faire en sorte qu’aucun composant ne fasse des traitements longs sans créer et gérer un nouveau thread (particulièrement vrai pour une activité qui doit répondre aux interactions de l’utilisateur).

Android offre un mécanisme léger d’appel distant de procédure (RPC) qui permet de communiquer avec des services dans un processus extérieurs (vu qu’un processus ne peut accéder à la mémoire d’un autre).

Comme dit, toutes les données d’une application y compris les fichiers sont privés. Android propose différents moyens de stockage : préférences, fichiers, base de données SQLite, réseau. Cependant il est possible de les rendre accessibles par l’intermédiaire de « content provider » ou fournisseurs de contenu. Android propose d’origine des fournisseurs pour les type de données communes. Tous les fournisseurs de contenus implémentent la même interface que les clients utilisent indirectement par l’intermédiaire d’objet « ContentResolver ». Il n’y a qu’une seul instance de chaque « ContentProvider » qui interagissent avec de multiples « ContentResolver » dans chaque application. Les fournisseurs de contenus expose leur données comme une simple table dans le modèle de base de données et sont accessibles par l’intermédiaire d’une URI. Les données sont récupérées à partir d’une requête dont le résultat se parcourt avec à l’aide d’un curseur (mécanisme classique du ResultSet). On peut bien sur aussi modifier les données et créer son fournisseur de données spécifique.

**Cycle de vie d’une application**

![Cycle de vie d'une Activité Android](/migrated-media/activity_lifecycle-c2d2f1b8bf9a.png "Cycle de vie d'une Activité Android")

Cycle de vie d'une Activité Android

Les activités ont principalement 3 états :

- active lorsqu’elle est en premier plan (au dessus de la pile d’activités d’une tache).L’utilisateur peut agir dessus.

- en pause si elle n’a plus le focus mais est encore partiellement visible

- stoppée si elle est entièrement cachée par une autre activité. Dans ce cas, elle peut être complètement tuée par le système si la mémoire est nécessaire ailleurs.

L’ensemble du cycle de vie d’une activité est comprise entre les méthodes onCreate et onDestroy. Le cycle de vie visible est compris entre les méthodes onStart et onStop. Le cycle de vie au premier plan est compris entre les méthodes onResume et onPause.

Une activité est tuable lorsqu’elle est entrée dans les états onPause, onStop ou onDestroy aussi bien par l’application que par le systeme lui même avec bien sur un niveau de possibilité. Il peut être important de sauver et gérer l’état du système. Pour cela, Android offre une méthode onSaveInstanceState appelée avant le onPause à partir duquel l’activité est tuable.

Les services ont aussi leur propre cycle de vie.

![Cycle de vie d'un service Android](/migrated-media/service_lifecycle-ffe44fb8d60b.png "Cycle de vie d'un service Android")

Cycle de vie d'un service Android

Un service peut être utilisé de deux facons :

- peut être démarré et tourner tant que personne ne l’arrête

- peut être contrôler par une interface qu’il expose. Le client doit alors se connecter au service ce qui démarre le service si celui-ci ne tourne pas déjà. Plusieurs clients peuvent se connecter au même service.

Android maintient aussi une liste des processus en cours avec le niveau d’importance suivant (dans l’ordre décroissant de priorité):

- processus en premier plan qui peut être soit une activité dans laquelle l’utilisateur interagit ou un service attaché

- processus visible qui n’a pas d’élément en premier plan mais peu influer sur la vision de l’utilisateur ainsi que les services attachés

- un service qui ne réponde pas au critère ci dessus

- une activité en arrière plan non visible.

Il y a de nombreuses activités dans cette état, Android maintient donc une liste ordonnée en fonction de la date d’utilisation (LRU).
 Un process vide qui permet normalement d’accélérer les temps de chargement de l’application.
 Les processus attachés à un autre processus ont toujours exactement le même niveau d’importance.

**Bonnes pratiques**
 Quelques bonnes pratiques ou astuces à connaître pour développer sur Android :
 La rotation de l’écran provoque le redémarrage de l’écran d’où la gestion du cycle de vie de l’application.
 Le composant NinePatch permet de définir des zones extensibles.
 Imbriquer les layouts coutent cher en terme de performance. Le RelativeLayout plus complexe à utiliser permet de réduire cette imbrication.
 L’accès au ressources du téléphone est vraiment à gérer (par exemple une utilisation massive du GPS peut faire ramer le tél et/ou vider sa batterie).

Il faut savoir faire de nombreuses optimisation de code :

- éviter la création d’instances inutiles car le garbage collector est lent et bloquant

- éviter les get et les set

- éviter d’utiliser les interfaces et les classes abstraites (par exemple quand on utilise une ArrayList, il ne faut mieux pas utiliser List comme classe de déclaration pour éviter de charger la classe List.).

- éviter les énumérations

- favoriser le mot clé final.

Il faut mieux faire du code « sale » afin de favoriser les performances.

**Conclusion**
 Android est un environnement de développement sur téléphone mobile agréable sur un marché prometteur. L’utilisation de Java et la disponibilité de nombreuses APIs en standard permet un développement rapide et souple permettant de répondre à des besoins spécifiques. Pour avoir approché le développement sur son grand concurrent l’Iphone, Android possède des avantages indéniables. L’ouverture des applications permet de créer, si les développeurs jouent le jeux, un énorme écosystème open source intégré au téléphone. Cependant la flexibilité du développement et son ouverture laisse apparaître une complexité difficile à appréhender.
 Je vais essayer de continuer les développements sur les deux plateformes pour me faire une comparaison plus poussée et plus concrète.

**Référence**
 Pour faire cet article je me suis principalement inspiré de ma petite expérience, de l’excellente documentation d’Android http://developer.android.com/guide/index.html , de la présentation organisée par Valtech et de la présentation effectuée par Oxiane au paris Jug (disponible ici : http://www.parisjug.org/xwiki/bin/download/Meeting/20091110/Android.pdf )

Je conseille trois autres liens :
 * [http://getsatisfaction.com/luci/topics/android_development_guide](http://getsatisfaction.com/luci/topics/android_development_guide)
 * [http://en.wikipedia.org/wiki/Android_(operating_system)](http://en.wikipedia.org/wiki/Android_(operating_system))
 * [http://www.ibm.com/developerworks/opensource/library/os-android-devel/](http://www.ibm.com/developerworks/opensource/library/os-android-devel/)

[Yannick Grenzinger](http://ygrenzinger.blogspot.com)
