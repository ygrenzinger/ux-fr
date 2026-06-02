---
title: "Le rapport Signal-Bruit"
date: "2010-09-16T10:40:59"
lastmod: "2010-09-17T14:58:09"
url: "/2010/09/16/le-rapport-signal-bruit/"
summary: "Toute communication implique la création, transmission et réception d’informations. Durant chaque étape de ce processus, la forme de l’information – le signal – est dégradée et des informations non pertinente – du bruit – sont ajoutées. La dégradation réduit la quantité d’information utile en modifiant sa forme. Le bruit réduit la clarté en diluant l’information […]"
author: "Yannick Grenzinger"
canonicalURL: "https://ux-fr.com/2010/09/16/le-rapport-signal-bruit/"
draft: false
categories: ["Notes de lecture"]
tags: ["communication", "Principe de design"]
aliases: ["/2010/09/16/le-rapport-signal-bruit"]
---
Toute communication implique la création, transmission et réception d’informations. Durant chaque étape de ce processus, la forme de l’information – le signal – est dégradée et des informations non pertinente – du bruit – sont ajoutées. La dégradation réduit la quantité d’information utile en modifiant sa forme. Le bruit réduit la clarté en diluant l’information utile avec de l’information inutile. La clarté de l’information peut être comprise comme le ratio de signal restant par rapport au bruit ajouté. Par exemple, un graphique élément inutile aura un ratio signal-bruit élevé.

Le but du design est donc de maximiser le signal et de diminuer le bruit, produisant ainsi un ratio signal-bruit élevé.

[![Mauvais rapport signal - bruit](/wp-content/uploads/2010/09/Bad_Signal_To_Noise_Ratio.jpg "Mauvais rapport signal - bruit")](/wp-content/uploads/2010/09/Bad_Signal_To_Noise_Ratio.jpg)

Mauvais rapport signal - bruit

[![Bon rapport signal - bruit](/wp-content/uploads/2010/09/Good_Signal_To_Noise_Ratio.jpg "Bon rapport signal - bruit")](/wp-content/uploads/2010/09/Good_Signal_To_Noise_Ratio.jpg)

Bon rapport signal - bruit

Maximiser le signal signifie clairement communiquer de l’information avec une dégradation minimale. La dégradation du signal apparait quand l’information est présentée de façon inefficace : écriture non claire, graphique inapproprié ou des labels et icônes ambigus. La clarté du signal est améliorée à travers une présentation simple et concise. Un design simple nécessite une charge de performance (voir article) minimale, permettant aux gens de se concentrer sur l’information. Par exemple, l’utilisation du mauvais type de graphique pour présenter certains types données peut modifier le sens de l’information. Mettre en avant les aspects clés de l’information peut aussi réduire la dégradation du signal : par exemple mettre en surbrilliance ou la répétition des éléments importants d’un design.

Minimiser le bruit signifie enlever les éléments non nécessaires. Il est important de réaliser que chaque élément non nécessaire (graphiques, textes, lignes, symboles …) détourne l’attention des éléments pertinents. Les éléments nécessaires devrait être eux aussi réduit au strict minimum tout en conservant leur fonction ou leur message pour accentuer leur efficacité. Par exemple, les lignes de séparation des cellules d’une table devraient être amoindries, éclaircies voir supprimées. L’excès crée du bruit.

En conclusion, il faut maximiser le ratio signal-bruit, augmenter le signal en gardant un design simple et sélectionner les stratégies de design avec soin. Il ne faut pas hésiter à utiliser des standards et des règles bien répandus pour créer un effet levier sur les conventions et promouvoir une implémentation cohérente.

Texte traduit provenant de [Universal Principles of Design](http://www.amazon.fr/gp/product/1592535879?ie=UTF8&tag=wwwuxfrcom-21&linkCode=as2&camp=1642&creative=6746&creativeASIN=1592535879)
