git, commandes de base
======================


configuration (une seule fois sur votre machine)
------------------------------------------------

  $ git config --global user.name "PRENOM NOM"
  $ git config --global user.email "MON@ADRESSE.EMAIL"


information (à utiliser sans modération)
----------------------------------------

  $ git status
  affiche l'état du dépot (en fait, de la branche courante) : nouveaux 
  fichiers, fichiers modifiés, etc.

  $ git log
  affiche la liste des commits du dépot (en fait, de la branche 
  courante)

  $ git diff
  ou
  $ git diff FICHIERS
  affiche les différences entre le dépot actuel et le dernier commit 
  (éventuellement, seulement pour les fichiers donnés en argument)


sauvegarde des modifications ("commit")
---------------------------------------

  $ git add FICHIERS
  demande à git de gérer les fichiers FICHIERS
  (On peut donner plusieurs fichiers en même temps, ou utiliser les 
  motifs du shell comme "git add *.py")
  ATTENTION : le fichier n'est pas sauvegardé par cette commande

  $ git commit
  ou plus souvent
  $ git commit -a -m "MESSAGE"
  enregistre l'état du dépot (en fait, de la branche courante)
     - l'option '-a' permet d'enregistrer **tous** les fichiers 
       modifiés. Sans elle, il faut faire "git add FICHIERS" avant le 
       "git commit"
       ATTENTION, les nouveaux fichiers ne sont pas ajoutés par l'option 
       '-a', il faut impérativement faire "git add FICHIERS" pour les 
       nouveaux fichiers.
     - l'option '-m "MESSAGE"' permet de donner une description de ce 
       commit
       Sans cette option, un éditeur de texte (probablement vi) sera 
       lancé pour taper la description du commit. (Si vous ne savez pas 
       utiliser vi, vous pouvez configurer un autre éditeur avec
       $ git config --global core.editor "MON_EDITEUR_FAVORI"
       )


communication avec un autre dépot
---------------------------------

  $ git pull REMOTE
  ou
  $ git pull
  récupère l'état du dépot (en fait de la branche) depuis REMOTE
  Si un dépot distant est configuré (automatiquement si vous avez 
  récupéré le dépot avec "git clone URL"), vous pouvez omettre REMOTE

  $ git push REMOTE
  ou
  $ git push
  envoie l'état du dépot (en fait de la branche) vers REMOTE.
  Si un dépot distant est configuré (automatiquement si vous avez 
  récupéré le dépot avec "git clone URL"), vous pouvez omettre REMOTE


importer un nouveau dépot ("fork", "clone")
-------------------------------------------
  $ git clone URL
  récupère un dépot git dans un nouveau répertoire dans le répertoire 
  courant.
  Typiquement, URL est récupérée sur github ("Clone or download")


revenir en arrière
------------------

  $ git checkout HASH
  remet le dépot dans l'état correspondant au commit de hash HASH
  Le hash d'un commit est affiché par "git log". Ça ressemble à 
  ddca8e4f15958e4f5151c5e23c4d673a132334b2
  (il faut donner au moins les 4 premiers caractères du hash...)

  ATTENTION, ceci n'est possible que si vous n'avez aucun changement non 
  enregistré.

  ATTENTION, il est déconseillé de modifier les fichiers lorsque le 
  dépot est dans un état antérieur. Au besoin, vous pouvez faire
  $ git reset --hard
  pour remettre votre dépot dans l'état exact du commit correspondant.

  $ git checkout main
  ou
  $ git checkout -
  remet le dépot dans l'état final


Utilisation typique
-------------------

0/ création d'un dépot vide depuis github ("New" depuis la page 
"Repositories" de votre compte github)

ou bien

0'/ "fork" d'un dépot existant depuis github

ou bien

0''/ récupération d'un dépot existant avec "git clone URL"



Lors d'une séance de travail :

1/ synchronisation pour récupérer les changement du dépot central (sur 
github)
  $ git pull
Normalement, il n'y aura jamais de conflit à cette étape.

2/ visualiser les nouveautés avec
  $ git log

3/ travail, modification de fichiers, création de fichiers, etc.

4/ lorsque vos modifications fonctionnent et sont finies :
  $ git add NOUVEAUX_FICHIERS
  $ git commit -a -m "MESSAGE"

5/ sauvegarde sur le dépot central
  $ git push


5/ en cas de conflit (parce que quelqu'un a modifié le dépot central 
entre temps), résolution du conflit et nouveau commit :
  $ git commit -a -m "RESOLUTION CONFLIT"
  $ git push


Pour aller plus loin
--------------------

Lorsque vous maitrisez les commandes et concepts précédents, vous pouvez 
vous renseigner sur

  - les "branches" qui permettent d'avoir plusieurs versions du dépots 
    "en parallèle"

  - les "remotes" qui permettent de communiquer avec plusieurs dépots 
    lors des "git pull" et "git push"

  - "git stash" qui permet de mettre de coté des modification 
    momentanément

  - les "pull-requests", qui permettent d'avoir plusieurs dépots 
    principaux, et d'échanger des modifications entre eux. (Ceci est un 
    mécanisme propre à github)
