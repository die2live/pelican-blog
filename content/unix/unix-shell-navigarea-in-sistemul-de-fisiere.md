Title: Unix Shell - Navigarea în sistemul de fişiere
Date: 2014-02-12 13:31
Author: Alexandr Dermenji
Category: Unix
Slug: unix-shell-navigarea-in-sistemul-de-fisiere

Sistemul de fişiere în sistemele de operare de tip \*unix au formă de
arbore. Astfel este un director de cel mai înalt nivel, care se numeşte
root (rădăcină), din care se pornesc multe alte ramuri, cum ar fi bin,
usr, temp, src, var, etc, şi altele, fiecare cu subramurile lor.

![](http://www.december.com/unix/tutor/tree1.gif)

Când ne aflăm în mediul shell, întotdeauna putem vedea în care director
din ierarhie ne aflăm. Aceasta este arătată chiar înainte de semnul \$
şi prompter. În următoarea imagine putem vedea că ne aflăm la cel mai
înalt nivel, adică în root (directorul root se indică cu un slash `/` ).

![](http://content.screencast.com/users/die2live/folders/Jing/media/6bce8f76-a2e4-46d1-8885-bf58bc4a058a/root%20slash.png)

Există şi alte caractere speciale pentru indicarea unui anumit director
din sistem. De exemplu, tilda (*\~*) indică la directorul *home* al
utilizatorului curent.  
Pentru a schimba directorul curent folosim
comanda `cd <directory_path>` (change directory),
unde *\<directory\_path\>* este calea spre directorul dorit.

![](http://content.screencast.com/users/die2live/folders/Jing/media/b885a70c-c9ac-43aa-8aa0-b9e3cd39cbe4/cd%20tilde.png)

Aici am folosit `cd ~` care a schimbat directorul curent să fie home.
Putem vedea calea deplină la directorul curent folosind
comanda *pwd* (present working directory).

![](http://content.screencast.com/users/die2live/folders/Jing/media/f9c9cf57-12fd-4925-86e5-3b00413a09e9/pwd%20home.png)

Vedem că ne aflăm în directorul /home/dai. Astfel am fi putut ajunge
aici accesând comanda `cd /home/dai`

![](http://content.screencast.com/users/die2live/folders/Jing/media/dd1379ec-fe4e-432c-bb56-1239dab2b74e/cd%20home_dai.png)

Pentru a ne deplasa cu un nivel mai sus, folosim comanda `cd ..`

![](http://content.screencast.com/users/die2live/folders/Jing/media/c8369679-f3f2-434f-a8c5-f36914910361/cd%20back.png)
