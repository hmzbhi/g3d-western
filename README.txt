ORDINATEURS SUR LEQUEL LE PROJET FONCTIONNE:
    - Nous avons remarqué que la texture de notre terrain ne s'applique pas selon l'ordinateur sur lequel on run le projet 
    (surement à cause du fichier "Normal Map.exr" qui ne doit pas être pris en charge sur tous les ordinateurs)

    - C'est pourquoi, il faut run le projet sur un ordinateur de la salle E301 (les ordis déjà testés et OK):
        ~ ensipc 468
        ~ ensipc 469
        ~ ensipc 462

INSTRUCTIONS A SUIVRE POUR LANCER LE PROJET:
    - Vérifiez dans un premier temps que tous les modules pythons utilisés sont bien installés:
        ~ PyOpenGL
        ~ Assimpcy
        ~ glfw
        ~ numpy
        ~ sys
        ~ os
    
    - Pour lancer le projet, il suffit d'executer "make run" dans votre terminal de commande

    - Si vous souhaitez relancer le projet sans que les repertoires __pycache__ soient présent,
    il suffit d'executer la commande "make clean" toujours dans votre terminal de commande

CRITERES IMPLEMENTEES:
    - Animation Rivière et Nuage 
        (mais pas eu le temps de faire une animation Utilisant KeyFrame pour Horse)

    - Skybox avec vue infinie

    - Création de trois objets à la main (Cactus, rivière et Pancarts)
    
    - Hierarchie des objets utilisée pour Cactus et Pancate

    - Importation des textures sur les objets
    
    - Importation d'OBJ Feu de camp, cheval, charrette, Terrain
    
    - Implémentation des particules au dessus du feu
    
    - Light_dir ajoutée sur le nuage mais pas sur le reste des objets
    
    - Optimation du code pour limiter les ressources  

