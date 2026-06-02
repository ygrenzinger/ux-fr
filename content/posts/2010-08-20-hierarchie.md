---
title: "hierarchie"
date: "2010-08-20T10:45:40"
lastmod: "2010-08-20T10:45:40"
url: "/2010/08/20/hierarchie/"
summary: "Augmenter la visibilité des relations hiérarchiques dans un système est une des façons les plus efficaces d’améliorer la connaissance du système et donc son utilisabilité. Les exemples des hiérarchies visibles sont la structure d’un livre, les menus d’application à plusieurs niveaux et les diagrammes de classification. La perception des relations hiérarchiques à travers les éléments […]"
author: "Yannick Grenzinger"
canonicalURL: "https://ux-fr.com/2010/08/20/hierarchie/"
draft: false
categories: ["Notes de lecture"]
tags: ["organisation des données", "Principe de design", "Utilisabilité"]
aliases: ["/2010/08/20/hierarchie"]
---
Augmenter la visibilité des relations hiérarchiques dans un système est une des façons les plus efficaces d’améliorer la connaissance du système et donc son utilisabilité.

Les exemples des hiérarchies visibles sont la structure d’un livre, les menus d’application à plusieurs niveaux et les diagrammes de classification. La perception des relations hiérarchiques à travers les éléments est principalement dû à leur position relative gauche-droite et haut-bas mais est aussi influencé par leur proximité, leur taille et la présence de ligne de raccord. Les éléments supérieurs sont référencés comme les éléments parents et les éléments inférieurs comme les enfants.
 Il y a trois façons possibles de représenter une hiérarchie : les arbres, les nids et les escaliers.

Les **structures en arbre** illustrent les relations hiérarchiques en plaçant les enfants en dessous ou a droite de l’élément parent ou par l’utilisation d’autres stratégies indiquant la hiérarchie par exemple les lignes de connexion. Les arbres sont des stratégies efficaces pour représenter des hiérarchies d’une complexité modérée mais grossit très rapidement et devient un enchevêtrement quand plusieurs parents partagent des enfants communs.

[![Organigramme d'une famille royale](/wp-content/uploads/2010/08/Organigramme-famille-royale-300x134.jpg "Organigramme d'une famille royale")](/wp-content/uploads/2010/08/Organigramme-famille-royale.jpg)

Organigramme d'une famille royale est un exemple de structure en arbre

Les structures en nid illustrent les relations hiérarchiques en faisant contenir visuellement les éléments enfants dans les éléments parents comme dans un [diagramme de Venn](http://fr.wikipedia.org/wiki/Diagramme_de_Venn). Les structure en nid sont efficaces pour représenter des hiérarchies simples. Quand les relations deviennent trop denses ou complexes, les nids sont moins efficaces. Ceux-ci sont le plus généralement utilisés pour grouper des informations ou des fonctions et pour représenter des relations logiques simples.

[![Poupées russes](/wp-content/uploads/2010/08/Russian-Matroshka_no_bg-300x240.jpg "Poupées russes")](/wp-content/uploads/2010/08/Russian-Matroshka_no_bg.jpg)

Les poupées russes sont un très bon exemple de structure en nid

Les structures en escalier illustrent les relations hiérarchiques en empilant les éléments enfants en bas et à droite des éléments parents comme dans un sommaire de livre. Les structures en escalier sont efficaces pour représenter des hiérarchies complexes mais sont difficilement navigable et impliquent de façon erroné une relation séquentielle entre les enfants empilés. Les escaliers interactifs qu’on trouve dans les logiciels résolvent le problème précédent en cachant les éléments enfants tant que le parent n’est pas sélectionné. Les structures en escalier sont généralement utilisées pour représenter pour représenter de larges structures qui change à travers le temps.

[![Sommaire d'un livre](/wp-content/uploads/2010/08/sommaireLivre-257x300.jpg "Sommaire d'un livre")](/wp-content/uploads/2010/08/sommaireLivre.jpg)

Le sommaire d'un livre est un bon exemple de structure en escalier

Il est utile d’explorer différentes façons de révéler et cacher la complexité d’une structure hiérarchique pour augmenter leur clarté et leur efficacité.

Texte traduit provenant de [Universal Principles of Design](http://www.amazon.fr/gp/product/1592535879?ie=UTF8&tag=wwwuxfrcom-21&linkCode=as2&camp=1642&creative=6746&creativeASIN=1592535879)
