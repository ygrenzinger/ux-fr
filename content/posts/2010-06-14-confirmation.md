---
title: "Confirmation"
date: "2010-06-14T14:25:51"
lastmod: "2011-09-11T15:43:41"
url: "/2010/06/14/confirmation/"
summary: "La confirmation est une technique largement répandue qui permet de prévenir les actions non souhaitées en requérant une vérification avant qu’elle ne soit effectuée (aussi connue comme le principe de vérification ou « forcing function »). Elle est principalement utilisée dans le cadre d’erreur appellée « slips » (erreur dans l’exécution d’une action destinée à atteindre un objectif). Cependant la confirmation […]"
author: "Yannick Grenzinger"
canonicalURL: "https://ux-fr.com/2010/06/14/confirmation/"
draft: false
categories: ["Notes de lecture"]
tags: ["Confirmation", "Principe de design", "Tolerance"]
aliases: ["/2010/06/14/confirmation"]
---
La confirmation est une technique largement répandue qui permet de prévenir les actions non souhaitées en requérant une vérification avant qu’elle ne soit effectuée (aussi connue comme le principe de vérification ou « forcing function »). Elle est principalement utilisée dans le cadre d’erreur appellée « slips » (erreur dans l’exécution d’une action destinée à atteindre un objectif).

Cependant la confirmation diminue les performances. Elle devrait donc être réservée pour les actions critiques ou irréversibles.
 Il y a deux techniques basiques : le dialogue et l’opération en deux temps.
 Le dialogue nécessite d’établir une interaction verbale avec la personne utilisant le système. Dans le cadre des interfaces graphiques, c’est communément représenté par une boite de dialogue posant une question à l’utilisateur (« Vous êtes sur le point d’effacer ce fichier. Voulez vous continuer ? Oui ou Non »). Il faut utiliser les boites de dialogue de confirmation avec modération sinon les utilisateurs finissent par les ignorer et sont frustrés par les constantes interruptions.

[![Boite de dialogue de confirmation](/wp-content/uploads/2010/06/DeleteConfirm.jpg "DeleteConfirm")](/wp-content/uploads/2010/06/DeleteConfirm.jpg)

L’opération en deux temps induit une étape préliminaire qui doit intervenir avant la commande ou l’entrée souhaitée. C’est souvent plus utilisé dans le cadre du hardware et est alors référencé comme une opération visée/tir. Par exemple, deux personnes doivent utiliser deux clés uniques pour activer un missile nucléaire ou tout simplement une premier bouton doit être enclenché pour activer le fonctionnement d’une tronçonneuse. Le but est de prévenir une activation accidentelle d’un élément critique.

[![Confirmation du nouveau mot de passe](/wp-content/uploads/2010/06/PasswordReenter.jpg "PasswordReenter")](/wp-content/uploads/2010/06/PasswordReenter.jpg)

Il peut être intéressant de diminuer le nombre de confirmation voir de les désactiver après une première confirmation.

Texte traduit provenant de [Universal Principles of Design](http://www.amazon.fr/gp/product/1592535879?ie=UTF8&tag=wwwuxfrcom-21&linkCode=as2&camp=1642&creative=6746&creativeASIN=1592535879)

[Yannick Grenzinger](http://ygrenzinger.blogspot.com)
