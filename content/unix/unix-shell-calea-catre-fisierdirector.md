Title: Unix Shell - Calea către fişier/director
Date: 2014-02-13 14:10
Author: Alexandr Dermenji
Category: Unix
Slug: unix-shell-calea-catre-fisierdirector

Sistemul de fişiere în sistemele de operare de tip \*nix au formă de
arbore. Astfel este un director de cel mai înalt nivel, care se numeşte
root (rădăcină), din care se pornesc multe alte ramuri, cum ar fi bin,
usr, temp, src, var, etc, şi altele, fiecare cu subramurile lor.

![](http://www.openbookproject.net/tutorials/getdown/unix/images/lesson2/UnixDirectoryTree.png)

Pentru a indica unde se află un director sau fişier în sistemul de
fişiere al computerului este necesar să ştim calea spre acest
director/fişier. Astfel calea este adresa spre o resursă de pe discul
local sau din reţea. Deosebim 2 tipuri de căi: cale completă şi cale
relativă.  
**NB:** *Pentru toate exemplele din acest articol se va folosi ierarhia
de fişiere din imagine şi se presupune că directorul curent este
/users/john*  
**Calea completă** se indică de la rădăcina sistemului de fişiere, până
la fişierul/directorul dorit. Astfel, calea completă spre directorul
curent este */users/john*, iar calea spre directorul "work" din
directorul curent este */users/john/work*.  
**Calea relativă** se indică pornind de la directorul curent. Astfel,
calea relativă spre directorul "work" din directorul curent este *work*.
De asemenea, am putea folosi şi construcţia *./work*, în care punctul
(.) indică directorul curent.  
Un al exemplu ar fi calea relativă spre directorul
"carol" - *./../carol* (din directorul curent ne ridicăm cu un nivel mai
sus, iar de acolo in jos, spre "carol").
