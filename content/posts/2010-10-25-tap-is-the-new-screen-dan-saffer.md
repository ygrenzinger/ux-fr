---
title: "Tap is the new screen – Dan Saffer"
date: "2010-10-25T08:17:23"
lastmod: "2010-10-30T13:40:54"
url: "/2010/10/25/tap-is-the-new-screen-dan-saffer/"
summary: "Résumé de cette video : Tap is the new screen. – Dan Saffer Les interfaces tactiles et gestuelles envahissent le marché. C’est le début d’une révolution dans le design de l’interaction. La question est donc : comment designer cette nouvelle interaction ? Cette interaction est basé sur les gestes : tous mouvements physiques qui peuvent […]"
author: "Yannick Grenzinger"
canonicalURL: "https://ux-fr.com/2010/10/25/tap-is-the-new-screen-dan-saffer/"
draft: false
categories: ["General"]
tags: ["tactile", "wireframe"]
aliases: ["/2010/10/25/tap-is-the-new-screen-dan-saffer"]
---
Résumé de cette video : [Tap is the new screen. – Dan Saffer](http://www.vimeo.com/2761844)

Les interfaces tactiles et gestuelles envahissent le marché. C’est le début d’une révolution dans le design de l’interaction. La question est donc : comment designer cette nouvelle interaction ?
 Cette interaction est basé sur les gestes : tous mouvements physiques qui peuvent être détectés et répondus par un système numérique sans l’aide d’un périphérique d’entrée traditionnel comme la souris ou le stylet.
 Deux types d’interaction gestuelle : écran tactile (simple ou multi-touch) ou formes libres dans l’espace (exemple de la Wii mote).
 L’ensemble est basé sur des senseurs communs : pression, lumière, proximité, sonore, inclinaison, mouvement, orientation. C’est les senseurs qui définissent les possibilités de l’interaction gestuelle.

Physiologie : contraintes de la main.
 Il faut aussi se rappeler qu’un doigt est moins précis qu’un curseur ou que la main peut cacher les informations. Il faut donc éviter de mettre les fonctionnalités ou des informations essentielles en dessous d’un élément de l’interface qui peut être touché.
 [![Sliders dans une interface tactile](/wp-content/uploads/2010/10/Sliders.png "Sliders dans une interface tactile")](/wp-content/uploads/2010/10/Sliders.png)

Il faut se rappeler [la loi de Fitts](/2010/08/03/la-loi-de-fitts/) : plus la distance est petite ou plus la cible est grande, plus la cible (icône) est atteinte rapidement.
 Éviter au maximum au utilisateur de couvrir l’écran avec leur main.
 Créer des cibles de tailles raisonnable : pas plus petites qu’un cm² (la taille du bout des des doigts).
 Deux astuces pour les éléments touchables :

- Iceberg : l’icône représentant l’élément touchable est en fait plus petite que cet élément.

- Adaptatif : créer un iceberg en devinant ce que l’utilisateur va utiliser (le clavier de l’Iphone par exemple).

Les éléments qui suivent deviennent difficile à faire voir disparaît avec les interfaces tactiles : curseur (vous savez ou sont vos mains), MouseOver action, double-clic, clic droit.
 Annuler une action devient aussi une question complexe.

Comment documenter les gestes ?
 Les « maquettes » (wireframes) marchent toujours.
 Utilisation d’images-clés voir de storyboards, de « Swim lanes framework » avec le storyboard du scénario en haut et différentes niveaux (techniques, fonctionnels, etc), animations ou encore films.
 [![Swim Lanes Framework](/wp-content/uploads/2010/10/SwimLanesFramework-300x214.png "Swim Lanes Framework")](/wp-content/uploads/2010/10/SwimLanesFramework.png)

Transformer le geste en code.

- Variables : Que mesure-t-on ?

- Données : récupérer les données du senseurs

- Calculs : déterminer les différences entre les données

- Structures : Que signifie la somme ?

- Action : si la structure correspond, faire quelque chose.

Communiquer les interactions gestuelles ?
 Trois zones d’engagement de l’utilisateur : attraction > observation > interaction ( en fonction de la distance).
 Les utilisateurs peuvent avoir du mal à se lancer sur une interface gestuelle : peur de le casser ou de paraître stupide en public.
 Il faut utiliser des affordances naturelles, des illustrations pour attirer les gens.

Comment déterminer les gestes appropriés ?
 C’est une équation en trois parties :

1. les senseurs et entrées disponibles

1. la tache qui doit être effectuée

1. la physiologie du corps humain

Il faut garder en mémoire que plus le geste sera compliqué moins il y aura de personnes pouvant le réaliser. Il faut donc que la complexité du geste soit en rapport avec la complexité de la tache à réaliser.

Les meilleurs designs sont ceux qui font correspondre le comportement du système aux gestes que l’humain fait déjà naturellement pour permettre ce comportement.
