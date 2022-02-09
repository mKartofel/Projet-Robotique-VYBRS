from environment import Environment
from robot import Robot
from obstacle import Obstacle,Wall

class FoV:
    #FOV pour Field of View : le but est de permettre au robot de pouvoir detecter
    #des obstacles pour éviter la collision
    def __init__(self,degree,length):
        """
            :length:int
            :degree:int
            :safespace:int
        """
        self.degree=degree #degree du champs de vision
        self.length=length #longueur jusqu'à laquelle le robot peut percevoir
        self.collision=False
        self.safespace=None
        #self.safespace

    def setSafespace(self,newss): #newss: new safe space
        """
            :newss:int
            Set le safe space de none a newss
        """
        self.safespace=newss

#    def addObstacle(object,collision):
#        """
#            #:collision:bool
#            Ajoute un obstacle dans une liste d'obstacle
#        """
#        est ce qu'on peut rendre la methode pour ajouter des objets dans l'environnement statique ?
#        if(collision):
#            if isinstance(Obstacle,object):
#                robot.listobjects.append(object)

    def calculCollision(self):
        """
            Mesure la distance actuelle de collision
        """


    def defCollision(self):
        """
            Actualise la variable collision
        """
        if(self.length<self.safespace):#utiliser le safespace ?
            self.collision=True
        if(self.length>=self.safespace):
            self.collision=False
