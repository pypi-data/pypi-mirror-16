Jouets — Programmes « amusants » à connotation mathématique ou informatique
===========================================================================

|sources| |pypi| |build| |documentation| |license|

Ces programmes n'ont pas ou peu d'utilité pratique, si ce n'est mettre en œuvre
des concepts des deux disciplines.

Les programmes sont :

- `aperitif <http://jouets.readthedocs.io/fr/latest/aperitif>`_ : Recherche de solutions au problème des apéritifs
- `chemin <http://jouets.readthedocs.io/fr/latest/chemin>`_ : Recherche du score maximal d’un jeu
- `dobble <http://jouets.readthedocs.io/fr/latest/dobble>`_ : Création de jeu de cartes de Dobble
- `egyptienne <http://jouets.readthedocs.io/fr/latest/egyptienne>`_ : Décomposition en fractions égyptiennes
- `erathostene <http://jouets.readthedocs.io/fr/latest/erathostene>`_ : Crible d’Érathostène optimisé en espace
- `fractale <http://jouets.readthedocs.io/fr/latest/fractale>`_ : Tracé de fractale itératif et infini
- `labyrinthe <http://jouets.readthedocs.io/fr/latest/labyrinthe>`_ : Construction de labyrinthes
- `mafia <http://jouets.readthedocs.io/fr/latest/mafia>`_ : Calcul de probabilités de victoire au jeu de `mafia <https://fr.wikipedia.org/wiki/Mafia_%28jeu%29>`__
- `peste et choléra <http://jouets.readthedocs.io/fr/latest/peste>`_ : Simulation de propagation d'épidémies
- `sudoku <http://jouets.readthedocs.io/fr/latest/sudoku>`_ : Solveur de sudoku
- d'autres `en cours <https://git.framasoft.org/spalax/jouets/merge_requests?label_name=id%C3%A9e>`_ ou `en projet <https://git.framasoft.org/spalax/jouets/issues?label_name=id%C3%A9e>`_ …

Quoi de neuf ?
--------------

Voir le `journal des modifications
<https://git.framasoft.org/spalax/jouets/blob/master/CHANGELOG.md>`_.

Documentation
-------------

* `Voir la version compilée <http://paternault.fr/informatique/jouets/>`_.

* Pour la compiler depuis les sources, télécharger le paquet, et lancer::

      cd doc && make html

Téléchargement, installation et exécution
-----------------------------------------

Voir à la fin de la liste pour une installation par un paquet Debian.

* Depuis les sources :

  * Téléchargement : https://pypi.python.org/pypi/jouets
  * Installation (dans un `virtualenv`, pour éviter les conflits avec le
    gestionnaire de paquets de votre distribution)::

        python3 setup.py install

* Avec `pip`::

    pip install jouets

* Pour utiliser les programmes sans les installer, il suffit de les exécuter
  depuis la racine du projet. Par exemple ::

      ./bin/erathostene

* Paquet Debian (et Ubuntu ?) rapide :

  Cela nécessite l'installation de `stdeb <https://github.com/astraw/stdeb>`_ ::

      python3 setup.py --command-packages=stdeb.command bdist_deb
      sudo dpkg -i deb_dist/jouets-<VERSION>_all.deb

.. |documentation| image:: http://readthedocs.org/projects/jouets/badge
  :target: http://jouets.readthedocs.io
.. |pypi| image:: https://img.shields.io/pypi/v/jouets.svg
  :target: http://pypi.python.org/pypi/jouets
.. |license| image:: https://img.shields.io/pypi/l/jouets.svg
  :target: http://www.gnu.org/licenses/gpl-3.0.html
.. |sources| image:: https://img.shields.io/badge/sources-jouets-brightgreen.svg
  :target: http://git.framasoft.org/spalax/jouets
.. |build| image:: https://git.framasoft.org/spalax/jouets/badges/master/build.svg
  :target: https://git.framasoft.org/spalax/jouets/builds

