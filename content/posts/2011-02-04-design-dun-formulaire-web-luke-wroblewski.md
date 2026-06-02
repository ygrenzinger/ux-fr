---
title: "Design d’un formulaire web – Luke Wroblewski"
date: "2011-02-04T09:20:24"
lastmod: "2011-02-04T00:21:26"
url: "/2011/02/04/design-dun-formulaire-web-luke-wroblewski/"
summary: "Résumé de la vidéo Web form design par Luke Wroblewski Cette présentation est passionnante, bien riche et remplie d’exemples concrets. Je conseille fortement de la voir pour tout ceux qui veulent améliorer l’expérience utilisateur et l’ergonomie de leur formulaire web (et clairement je pense que je vais essayer d’acheter le livre Première constatation : les […]"
author: "Yannick Grenzinger"
canonicalURL: "https://ux-fr.com/2011/02/04/design-dun-formulaire-web-luke-wroblewski/"
draft: false
categories: ["General"]
tags: ["Erreur", "expérience utilisateur", "formulaire"]
aliases: ["/2011/02/04/design-dun-formulaire-web-luke-wroblewski"]
---
[Résumé de la vidéo Web form design par Luke Wroblewski](http://videos.visitmix.com/MIX09/C17F)

Cette présentation est passionnante, bien riche et remplie d’exemples concrets. Je conseille fortement de la voir pour tout ceux qui veulent améliorer l’expérience utilisateur et l’ergonomie de leur formulaire web (et clairement je pense que je vais essayer d’acheter le livre
 Première constatation : les formulaires sont souvent mal faits.
 Pourtant ils sont une part très importante du net aussi bien pour le client que l’entreprise. Énormément d’actions passent par un formulaire. Ils représentent même le dialogue du client avec l’entreprise.

Ils ont leur role dans :

- le commerce car ils permettent à l’utilisateur d’acheter en ligne et à l’entreprise de maximiser ces ventes

- l’engagement car ils permettent à l’utilisateur d’entrer et de manipuler des informations et à l’entreprise d’accumuler des données et du contenu

- l’adhésion car ils permettent la participation de l’utilisateur et pour l’entreprise d’augmenter le nombre de client et de faire grandir des communautés

Par exemple, le formulaire d’upload des videos de Youtube a été redessiné de nombreuses fois vu sa fonction centrale.

**Comment faire de meilleurs formulaires web ? Les dix meilleures pratiques**

**1 – chemin vers la complétion**
 Le but premier d’un formulaire est sa complétion en offrant une ligne de visualisation claire.

[![Ligne de visualisation non claire du formulaire](/wp-content/uploads/2011/01/NotClearLine2.png "Ligne de visualisation non claire du formulaire")](/wp-content/uploads/2011/01/NotClearLine2.png)

Ligne de visualisation non claire du formulaire

[![Ligne de visualisation claire du formulaire](/wp-content/uploads/2011/01/ClearLine2.png "Ligne de visualisation claire du formulaire")](/wp-content/uploads/2011/01/ClearLine2.png)

Ligne de visualisation claire du formulaire

L’exemple ci dessus montre clairement l’importance de l’alignement et de la cohérence pour que l’utilisateur ne se « perdent » pas.
 Il faut créer un flux visuel clair.

Il faut montrer à l’utilisateur son avancement par la portée, le progrès ou le statut.

[![Indicateur de progression pour l'utilisateur](/wp-content/uploads/2011/01/ProgressIndicator.png "Indicateur de progression pour l'utilisateur")](/wp-content/uploads/2011/01/ProgressIndicator.png)

Indicateur de progression pour l'utilisateur

En conclusion, il faut :

- mettre en avant un chemin clair vers la complétion du formulaire

- utiliser des barres de progression pour communiquer la portée, l’état et la position dans le formulaire

- Si besoin de plus de temps ou d’une recherche d’information, fournir une page de départ

- utiliser des indicateurs de progression plus généraux pour les formulaires avec des séquences variables suivant les besoins

**2 – l’alignement**
 Il explique l’alignement des labels : au-dessus, a droite ou encore a gauche.
 Le titre au-dessus se révèle le plus rapide pour les données familières mais demande plus d’espace vertical. Il permet aussi plus de flexibilité pour la localisation et les entrées complexes.
 L’alignement à droite permet une bonne association entre le label et la zone de saisie, requiert moins d’espace vertical et a une complétion rapide mais il se révèle plus difficile à lire.
 L’alignement a gauche est plus pratique pour les données non familières et permet de parcourir rapidement les labels par contre changer la longueur des labels peut invalider l’alignement du formulaire et la complétion est plus lente.
 Mixer plusieurs alignement n’est pas bon.

Les labels dans la zone de saisie sont pratiques mais il faut être sur que l’utilisateur se rappellera de la question.
 Il faut aussi les utiliser avec modération (formulaire avec uniquement des réponses mais pas de questions ?)

En conclusion, il faut :

- utiliser l’alignement au dessus pour réduire les temps de complétion d’un formulaire avec des données familières

- utiliser l’alignement à droite quand l’espace vertical est limité

- utiliser l’alignement à gauche quand les données ne sont pas familières ou complexes

**3 – Les aides et astuces**
 Elles sont utiles quand :

- le formulaire demandent des données non familière

- l’utilisateur peut se demander pour quel raison cette donnée est demandée

- une manière recommandée de fournir la donnée

- certaines données sont optionnelles

Cependant, les aides et astuces ne doivent pas envahir le formulaire.
 Si c’est obligatoire, il faut peut être passer à une solution dynamique.
 Par exemple quand l’utilisateur arrive dans le champs, une aide apparait. On peut aussi utiliser un bouton d’aide ou encore faire apparaitre une section d’aide.

[![Section d'aide à droite dans un formulaire](/wp-content/uploads/2011/02/HelpSection.png "Section d'aide")](/wp-content/uploads/2011/02/HelpSection.png)

Section d'aide à droite dans un formulaire

En conclusion, il faut :

- minimiser le besoin d’aide et astuces pour remplir un formulaire

- favoriser une aide visible et proche qui est plus utile

- utiliser un système activé par l’utilisateur pour formulaire complexe et souvent réutilisé

- utiliser une aide directement inclue dans le champs de saisie à moins que vous ayez beaucoup de contenu (texte, graphique, tableau)

- utiliser un système cohérente si vous avez beaucoup d’aide

**4 – validation en ligne**
 Il faut fournir une validation directement à l’insertion des données, suggérer des données valides ou encore aider l’utilisateur à rester dans les limites.
 Il faut aussi bien faire en sorte que les validations soient cohérentes (exemple du « confirm » qui vérifie juste l’égalité des deux champs ou encore ne refait pas la vérification quand la valeur initiale change).
 Il compare énormément la qualité d’enregistrement entre Yahoo et Twitter.

[![Validation du formulaire sur Twitter](/wp-content/uploads/2011/02/TwitterValidation.png "Validation du formulaire sur Twitter")](/wp-content/uploads/2011/02/TwitterValidation.png)

Validation du formulaire sur Twitter

[![Validation du formulaire sur Yahoo](/wp-content/uploads/2011/02/YahooValidation.png "Validation du formulaire sur Yahoo")](/wp-content/uploads/2011/02/YahooValidation.png)

Validation du formulaire sur Yahoo

En conclusion, il faut :

- utiliser une validation directement dans le champs de saisie pour les champs de saisie où il y a potentiellement beaucoup d’erreurs

- utiliser des suggestions d’entrées pour lever des ambiguïtés

- communiquer les limites

**5 – Actions**
 Toutes les actions sur un formulaire (bouton) ne sont pas équivalentes.
 Par exemple « Effacer tout », « Annuler » et « Retour en arrière » sont des actions secondaires rarement utilisées. « Sauver », « Continuer » et « Soumettre » sont des actions primaires directement responsables de la complétion du formulaire.

[![Différentier les actions primaires et secondaires dans un formulaire](/wp-content/uploads/2011/02/PrimaryAndSecondaryActions.png "Actions primaires et secondaires dans un formulaire")](/wp-content/uploads/2011/02/PrimaryAndSecondaryActions.png)

Différentier les actions primaires et secondaires dans un formulaire

Il faut les différentier (Gras, taille, couleur, etc..).

En conclusion, il faut :

- éviter les actions secondaires si possible

- faire une distinction visuelle claire entre les actions primaires et secondaires

- aligner les actions primaires avec les champs de saisie pour un chemin de complétion clair

**6 – Actions en attente**
 Certaines actions nécessitent du temps de traitement (soumission de formulaires, calculs, uploads).
 Il faut fournir un retour d’informations par exemple désactiver le bouton de soumission le temps du traitement.
 On peut profiter du temps d’attente pour afficher des informations.

**7 – Erreurs**
 Quand une erreur se produit, c’est l’information la plus importante du formulaire car elle vous empêche d’aller plus loin.

[![Indiquer clairement les erreurs et les associer avec le champs responsable.](/wp-content/uploads/2011/02/Erreurs.png "Indiquer les erreurs dans un formulaire")](/wp-content/uploads/2011/02/Erreurs.png)

Indiquer clairement les erreurs et les associer avec le champs responsable.

En conclusion, il faut :

- indiquer clairement qu’une erreur à eu lieu : placement au dessus et contraste visuel

- fournir des actions de correction

- associer le champ erroné avec le message d’erreur

- ne pas hésiter à « doubler » les informations où l’erreur a eu lieue

**8 – Les entrées non nécessaires**
 Chaque question demande aux utilisateurs de la comprendre, de formuler une réponse et d’entrer cette réponse.
 Soyez vigilant sur chaque question en se posant ces trois questions :

- Peut elle être enlevée ?

- Peut elle être remise à plus tard ?

- Peut elle être devinée ?

Enlever des informations peut avoir un grand impact sur la complétion d’un formulaire par exemple le type de carte de paiement n’est pas nécessaire.
 Utiliser le code postal pour renseigner directement la ville et l’état.
 Il ne faut pas non plus compliquer le traitement dans le seul but d’enlever question.

**9 – l’organisation du formulaire**
 Cela dépend. Il faut essayer d’avoir une conversation, de parler d’une seul voix ou encore d’utiliser les coupures naturelles.
 Luke montre un superbe exemple d’un « simple » formulaire de contact qui au fil des besoins (ingénieurs, marketing, légal…) devient très complexe et inutilisable.

[![Exemple d'un formulaire sous forme d'une conversation.](/wp-content/uploads/2011/02/Conversation.png "Exemple d'un formulaire sous forme d'une conversation")](/wp-content/uploads/2011/02/Conversation.png)

Exemple d'un formulaire sous forme d'une conversation.

En conclusion, il faut :

- prendre le temps d’évaluer chaque question que l’on pose

- assurer la cohérence

- se forcer à être succinct

- utiliser une seule page web si le formulaire peut se diviser en plusieurs sujets courts

- utiliser une seule longue page quand il y a de nombreuses questions mais sur un seul sujet

- au contraire utiliser plusieurs pages quand un formulaire contient de nombreuses questions avec peu de sujets

**10 – L’engagement graduel**
 Un bouton de soumission avec un label en rapport avec le titre de la page.
 D’après Luke, les formulaires d’inscription doivent disparaître.
 Les services web devraient provoquer l’engagement :

- expliquer ce que fait le service

- permettre aux personnes de l’utiliser

- avoir l’inscription comme résultat

En conclusion, il faut :

- essayer d’éviter les formulaires

- mettre en avant le cœur de votre service avec le moins d’interaction possible

- faire en sorte que l’utilisateur réussisse du premier coups

- , si vous générer des comptes automatiquement, faire en sorte que l’utilisateur puisse y accéder des façon claire

- utiliser une seule longue page quand il y a de nombreuses questions mais sur un seul sujet

- ne pas distribuer divers champs de saisie dans des formulaires sans prendre en compte l’engagement
