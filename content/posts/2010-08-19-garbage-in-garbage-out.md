---
title: "Garbage In, Garbage Out"
date: "2010-08-19T16:43:35"
lastmod: "2010-08-22T18:35:30"
url: "/2010/08/19/garbage-in-garbage-out/"
summary: "L’observation générale est que la qualité des entrées fait la qualité des sorties et, à moins d’une intervention du design, les mauvaises entrées donnent généralement des mauvaises sorties. Ce principe a été étendu à de nombreux domaines comme le business, l’éducation, la nutrition ou l’ingénieurie. La métaphore des « déchets entrants » fait référence à deux types […]"
author: "Yannick Grenzinger"
canonicalURL: "https://ux-fr.com/2010/08/19/garbage-in-garbage-out/"
draft: false
categories: ["Notes de lecture"]
tags: ["Affordance", "Confirmation", "Contrainte", "Gestion de l'erreur", "Principe de design"]
aliases: ["/2010/08/19/garbage-in-garbage-out"]
---
L’observation générale est que la qualité des entrées fait la qualité des sorties et, à moins d’une intervention du design, les mauvaises entrées donnent généralement des mauvaises sorties. Ce principe a été étendu à de nombreux domaines comme le business, l’éducation, la nutrition ou l’ingénieurie. La métaphore des « déchets entrants » fait référence à deux types de problèmes d’entrée : les problèmes de type et les problèmes de qualité.

Les **problèmes de type** apparaissent quand le système est alimenté par le mauvais type d’entrée par exemple indiquer un numéro de téléphone dans le champ lié à la carte de crédit. Les problèmes de type sont graves car l’entrée fournie peut être complètement différente de l’entrée attendue. L’avantage c’est que ces problèmes sont facilement détectable. Les problèmes de type sont généralement causés par des [erreurs de but](/2010/07/13/les-erreurs/), une action incorrecte causée par une action consciente. La stratégie principale pour minimiser ces problèmes sont les affordances et les contraintes.

Les **problèmes de qualité** apparaissent quand le type d’entrée est correct mais comporte des erreurs par exemple bien entrer un numéro de téléphone dans le champ téléphone mais un mauvais numéro. En fonction de la fréquence et de la sévérité des erreurs, le problème de qualité peuvent être plus ou moins sérieux. Faire une faute de frappe dans un champs de recherche n’est pas grave, par contre demander le téléchargement de 5000 éléments au lieu de 50 peut bloquer le système. Les problèmes de qualité sont généralement causés par des [erreurs d’inattention](/2010/07/13/les-erreurs/), action incorrecte causée par une action accidentelle ou inconsciente. Les premières stratégies pour minimiser les problèmes de qualité sont les pré-visualisations et les confirmations. Ces stratégies permettent de vérifier les conséquences d’une action avant l’entrée dans le système.

[![Garbage In, Garbage Out](/wp-content/uploads/2010/08/GarbageInOut.png "Garbage In, Garbage Out")](/wp-content/uploads/2010/08/GarbageInOut.png)

Le meilleur moyen d’éviter les « déchets sortants » est d’empêcher les « déchets entrants ». Il faut utiliser les affordances et les contraintes pour minimiser les problèmes de type. il faut utiliser la pré-visualisation et les confirmations pour minimiser les problèmes de qualité. Quand l’intégrité des entrées est critique, il faut utiliser des tests de validation pour vérifier l’intégrité avant l’entrée et considérer des étapes de validation qui exigent la vérification indépendante de multiples personnes. Il faut aussi considérer l’utilisation de mécanismes pour signaler et, dans certains cas, corriger automatiquement les mauvaises entrées (par exemple la correction orthographique).

Texte traduit provenant de [Universal Principles of Design](http://www.amazon.fr/gp/product/1592535879?ie=UTF8&tag=wwwuxfrcom-21&linkCode=as2&camp=1642&creative=6746&creativeASIN=1592535879)
