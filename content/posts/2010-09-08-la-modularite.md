---
title: "La modularité"
date: "2010-09-08T08:34:50"
lastmod: "2010-09-09T08:03:10"
url: "/2010/09/08/la-modularite/"
summary: "La modularité est un principe structurel utilisé pour manager la complexité des systèmes. Cela implique d’identifier les ensembles fonctionnels similaires et ensuite transformer ces ensembles en systèmes autonomes interdépendants (modules). Par exemple, le design modulaire des barrettes de mémoire d’un ordinateur permet à son propriétaire de changer ou d’augmenter la mémoire sans changer d’ordinateur. La […]"
author: "Yannick Grenzinger"
canonicalURL: "https://ux-fr.com/2010/09/08/la-modularite/"
draft: false
categories: ["Notes de lecture"]
tags: ["Principe de design", "système"]
aliases: ["/2010/09/08/la-modularite"]
---
La modularité est un principe structurel utilisé pour manager la complexité des systèmes. Cela implique d’identifier les ensembles fonctionnels similaires et ensuite transformer ces ensembles en systèmes autonomes interdépendants (modules). Par exemple, le design modulaire des barrettes de mémoire d’un ordinateur permet à son propriétaire de changer ou d’augmenter la mémoire sans changer d’ordinateur. La possibilité d’améliorer facilement et à moindre coût un système donne au design modulaire un avantage intrinsèque par rapport au design non modulaire.

Les modules devraient être désignés pour cacher leur complexité interne et interagir avec les autres modules grâce à des interfaces simples. Le résultat est une réduction globale de la complexité et une décentralisation de l’architecture système ce qui améliore la fiabilité, la flexibilité et permet une meilleure maintenance. De plus, un design modulaire encourage l’innovation sur chaque module ainsi que la compétition sur leur design et leur fabrication.

[![La modularité dans un ordinateur](/wp-content/uploads/2010/09/PC_Modularity.jpg "La modularité dans un ordinateur")](/wp-content/uploads/2010/09/PC_Modularity.jpg)

La modularité du PC est un des facteurs de son succès

Le bénéfice d’un design modulaire n’est pas sans coût : celui-ci est plus complexe qu’un design non modulaire. Les designers doivent avoir une connaissance significative du fonctionnement interne du système et de son environnement pour décomposer en modules et faire que ceux-ci fonctionnent comme un tout. La plupart des systèmes modulaires existants n’ont pas commencé ainsi, mais se sont peu à peu transformer pour être modulaire comme la connaissance du système augmente.

En conclusion, il faut considérer la modularité quand on désigne ou modifie des systèmes complexes. Cependant, il ne faut pas tenter un système modulaire complexe sans designer expérimenté et une connaissance approfondie du système.

Texte traduit provenant de [Universal Principles of Design](http://www.amazon.fr/gp/product/1592535879?ie=UTF8&tag=wwwuxfrcom-21&linkCode=as2&camp=1642&creative=6746&creativeASIN=1592535879)
