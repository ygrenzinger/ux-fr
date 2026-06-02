---
title: "Coefficient de sécurité"
date: "2010-07-14T12:27:44"
lastmod: "2011-09-11T16:12:25"
url: "/2010/07/14/coefficient-de-securite/"
summary: "Le coefficient de sécurité correspond à l’utilisation de plus d’éléments que nécessaire pour compenser les effets des variables inconnues et prévenir les défaillances du système. Le design requiert de faire face à l’inconnu. Quelque soit le niveau de connaissance du designer et la qualité des spécifications, les hypothèses sont inévitables dans n’importe quel processus de […]"
author: "Yannick Grenzinger"
canonicalURL: "https://ux-fr.com/2010/07/14/coefficient-de-securite/"
draft: false
categories: ["Principe de design"]
tags: ["methodologie", "Principe de design", "Tolerance"]
aliases: ["/2010/07/14/coefficient-de-securite"]
---
Le coefficient de sécurité correspond à l’utilisation de plus d’éléments que nécessaire pour compenser les effets des variables inconnues et prévenir les défaillances du système.

Le design requiert de faire face à l’inconnu. Quelque soit le niveau de connaissance du designer et la qualité des spécifications, les hypothèses sont inévitables dans n’importe quel processus de design. Les facteurs de sécurité sont utilisé pour compenser les effets potentiels de ces inconnues. L’idée est de rajouter des matériaux et des composants au système afin de que le design dépasse les spécifications définies comme nécessaire pour atteindre les besoins.
 Par exemple, designer un service internet pouvant supporter des milliers d’utilisateurs est direct et simple. Cependant, pour prendre en compte des besoins non anticipés par exemple le téléchargement de gros fichiers, les spécifications du besoin peuvent être multipliées (ici par trois). Dans ce cas, le coefficient de sécurité de trois signifie que le service est qualifié comme pouvant supporter 1000 utilisateurs mais est désigné pour en supporter réellement 3000.

Le niveau du coefficient de sécurité correspond directement au niveau d’ignorance des paramètres du design. Plus le niveau d’ignorance est grand, plus le coefficient de sécurité sera augmenté.
 Plus d’éléments signifie un coût plus important. Les nouveautés nécessitent un coefficient de sécurité important. Si un design devient fiable au cours du temps, la confiance que les inconnus du systèmes disparaissent combiné à la pression pour réduire les coûts provoque un processus de réglage et de réduction du coefficient de sécurité. Malheureusement ce processus se poursuit généralement jusqu’à ce qu’un accident ou une défaillance se produisent.

Il faut utiliser le coefficient de sécurité pour minimiser les risques de défaillance d’un design. Lorsque le niveau de confiance dans le design augmente, on peut alors diminuer en conséquence le coefficient de sécurité mais il faut faire attention à ne pas aller trop loin. Il faut observer la capacité nominale d’un système pour prendre des décisions qui stressent les limites du système et non pas la capacité prévue

[Wikipedia en parle avec des formules.](http://fr.wikipedia.org/wiki/Coefficient_de_s%C3%A9curit%C3%A9)
