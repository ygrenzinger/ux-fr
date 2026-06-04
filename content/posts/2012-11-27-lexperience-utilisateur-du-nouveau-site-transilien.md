---
title: "L’expérience utilisateur du nouveau site Transilien"
date: "2012-11-27T21:24:07"
lastmod: "2012-11-27T21:24:07"
url: "/2012/11/27/lexperience-utilisateur-du-nouveau-site-transilien/"
summary: "Transilien, le site des réseaux ferrés d’Ile de France a récemment refait son site avec une importante communication. Et le résultat me semble être un échec en termes d’expérience utilisateur. Le premier constat à l’utilisation du site est que l’ancien site (malheureusement non accessible même sur Google Cache) était plus clair. Seule question d’habitude ? […]"
author: "Yannick Grenzinger"
canonicalURL: "https://ux-fr.com/2012/11/27/lexperience-utilisateur-du-nouveau-site-transilien/"
draft: false
categories: ["Critique"]
aliases: ["/2012/11/27/lexperience-utilisateur-du-nouveau-site-transilien"]
---
[Transilien, le site des réseaux ferrés d’Ile de France a récemment refait son site avec une importante communication.](http://www.transilien.com/static/nouveau-site-transilien)
 Et le résultat me semble être un échec en termes d’expérience utilisateur. Le premier constat à l’utilisation du site est que l’ancien site (malheureusement non accessible même sur Google Cache) était plus clair. Seule question d’habitude ? Pas si sûr.
 Il ressort que le [rapport signal-bruit](/2010/09/16/le-rapport-signal-bruit/) du site est très mauvais.
 Surtout si on prend en compte le principal cas d’utilisation du site que je connais : **rechercher l’horaire et le trajet qui nous arrange plus d’un point de départ A à un point d’arrivée B**.

[![Recherche sur le site Transilien](/wp-content/uploads/2012/11/TransilienRecherche.png "Recherche sur le site Transilien")](/wp-content/uploads/2012/11/TransilienRecherche.png)

Commençons par le formulaire de recherche, je pense qu’on pourrait facilement enlever certains éléments et ainsi simplifier l’utilisation tout en gardant une interface classique, c’est-à-dire très proche de l’existant ou de sites similaires comme celui de la [RATP](http://www.ratp.fr/) ou de la [SNCF](http://www.sncf.com/fr/). Ce dernier est d’ailleurs une très bonne surprise en terme d’UX.
 Déjà les deux boutons « plans » affichent exactement la même fenêtre: pourquoi ne pas rapprocher les champs de recherche, unifier ce bouton et en profiter pour le remplacer par une icône ?
 Quelle est la valeur ajoutée de la flèche à coté de « De » et « A » ? A quoi renvoi l’astérisque ?
 Pourquoi ne pas indiquer seulement en titre « Votre trajet » en laissant les icones indiquant l’ensemble des moyens de transport (Bus, RER, Ratp ..). Ce sont des détails mais qui permettrait d’alléger sensiblement l’interface et la rendre plus agréable.

[![Résultats de la recherche sur le site Transilien](/wp-content/uploads/2012/11/TransilienResultat.png "Résultats de la recherche sur le site Transilien")](/wp-content/uploads/2012/11/TransilienResultat.png)
 On arrive ensuite à la page de résultats. Je ne suis pas designer visuel mais je la trouve beaucoup trop chargée visuellement avec un mauvais contraste visuel. Les éléments tels que l’heure de départ et d’arrivée ou encore se déplacer chronologiquement dans les trains ne sont pas mis en avant et pourtant sont normalement les plus importants. Mon œil est principalement attiré par la zone supérieure où il n’y a pas les boutons suivant et précédent qui se retrouvent dans la partie inférieure (au contraire du bouton Ajouter à mes favoris qui est présent 3 fois et dont je ne me suis jamais servi!). Le manque de direction et de clarté visuelle font que les informations sur le trajet (mode de transport, durée du trajet, heure de départ et arrivée) se retrouvent en double. Il y a aussi un manque de cohérence par exemple pourquoi ne pas garder le style en XX min pour la durée du trajet au lieu de mettre sur la durée totale du trajet XXhXX.
 Une action aussi importante que « modifier votre trajet » est mis en haut de l’interface sans design particulier pour la rendre facilement utilisable (surtout si on suit [la loi de fitts](/2010/08/03/la-loi-de-fitts/)).
 Je ne sais quelles sont les contraintes et raisons qui ont poussé vers ce nouveau design ni quels en était les objectifs mais, si je prends mon besoin de rechercher le trajet qui me convient le mieux entre 2 lieux, la nouvelle interface est clairement perfectible.
 C’est encore plus vrai quand on compare à des interfaces aussi simple et efficace que celle de Capitaine de Train ou celle de la [SNCF](http://www.sncf.com/fr/). Le plus étonnant c’est que l’interface de l’application Android ou iPhone de Transillien est bien plus claire et efficace !
 Peut être que le design de l’interface du site aurait du partir du design des versions mobiles (comme le préconise Luke Wroblewski dans son livre [Mobile First. N°6](http://www.amazon.fr/gp/product/2212134061/ref=as_li_ss_tl?ie=UTF8&tag=wwwuxfrcom-21&linkCode=as2&camp=1642&creative=19458&creativeASIN=2212134061))

J’espère que cet article génèrera des commentaires notamment de designers expérimentés.
