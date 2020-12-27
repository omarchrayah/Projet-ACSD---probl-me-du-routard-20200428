# -*- coding: utf-8 -*- 

#nom_prenom: omar_chrayah n:2184900

from priority_dict import priority_dict

def dijkstra(G,posInit,posFinal):#on s'intéresse à la recherche d'un plus court chemin dans un graphe entre deux sommets donnés.
    d={}
    pi={}
    F=priority_dict()#creer la file de priorite
    trajet=[posFinal]#liste contenante le sommet d'arrivé
    
    for v in G : #on ajouter dans la file de priorité les sommets avec leurs distances
        d[v]=float('+infinity')
        pi[v]=None
        
    
    d[posInit]=0 #initialiser tout à 0 pour le sommet de depart
    F[posInit]=0
  
    while F :
        u= F.pop_smallest() #extraire le sommet de plus petite distance
        for v in  G[u] : #relacher
            if d[v] > d[u] + G[u][v] :
                d[v] = d[u] + G[u][v]
                pi[v]=u
                F[v]=d[u]+G[u][v]
                
                
    #return d
    
    #grace aux lignes suivantes , le code va prendre en compte le sommet d'arrivéé et pourra calculer le plus court chemin entre un sommet de depart et un sommet d'arrivé  donnée en argument
    pere=pi[posFinal] #la variable pere prendre la valeur de la clé posFinal 
    while pere :
        trajet.insert(0,pere) #on insere pere à la position 0 au niveau de trajet 
        pere=pi[pere]
 
    return trajet    #on retourne le chemin que j'ai crée en remontant les peres
        
   
    
#dijkstra(H,'a','f')       

import random
def prim(G): #on trouve un sous - ensemble des arêtes formant un arbre qui inclut chaque sommet , où le poids total de tous les bords de l'arbre est réduit au minimum
    s=random.choice(list(G.keys())) #On choisit un sommet s aléatoirement

    F=priority_dict() #creer la file de priorite
    pi={} #creer un dico vide qui va contenir les peres
    for i in (list(G.keys())) :
        F[i]=float('+infinity')
    F[s] = 0
    pi[s] = None #initialiser le sommet initial avec une valeur None
    
    while F :
        u=F.pop_smallest() 
        for v in (list(G[u].keys())): #pour chaque v appartient à l'adjacent de de u 
            if v in F and  G[u][v] <F[v] : #si v appartient à F et le poids entre u et v est inferieur à clé[v]
                pi[v]=u 
                F[v]=G[u][v] #clé[v] prends le poids entre u et v 
            
    return pi #on retourne le dico qui contient les peres 
#prim(H)

def prefixe(T):
    liste=[]
    k=dict()
    def recursive(x):
        for i in T.keys(): #dans cette boucle for , on transforme le dico des peres que prim a retourné en une liste qui contient les sommets et leurs fils
            if i in T.values():
                k[i]= [key for key, value in T.items() if value == i] #recupere les clés qui ont la meme valeur 
            else:
                k[i]=list()
        
        if k[x]!='': # on verifie si le sommet a bien les fils 
            liste.insert(len(liste),x) #inserer le sommet à la fin de la liste 
            for pos in range (0,len(k[x])):
                for j in (k[x][pos]): #on parcourit les fils suivant leurs positions 
                    recursive(j)
        else : #sinon , si le sommet n'as pas de fils on ajoute jste le sommet à la fin de la liste 
            liste.insert(len(liste),x)
        return liste
    return recursive(list(T.keys())[0]) #on recupere  le sommet initial 

#prefixe(prim(H))    
                        
def RoutardApprox(G) :
    P=prim(G)
    rho=prefixe(P)
    sigma=list()
    sigma.insert(len(sigma),rho[0]) #on insere le sommet initial de position 0 de la liste qui renvoie le parcours prefixe , dans sigma
    for i in range(0, len(rho)-1):
        mu=dijkstra(G,rho[i],rho[i+1]) #calculer le plus court chemin entre rho[i] et rho[i+1] , on la stock dans la variable mu 
        del mu[0] #on retire de mu le premier sommet de position 0
        sigma.extend(mu) #ajouter mu à la fin de sigma
    #On referme le cycle σ en revenant au point de départ : 
    mu=dijkstra(G,rho[-1],rho[0]) 
    del mu[0]
    sigma.extend(mu)
    
    
    return sigma #retourner la sequence sigma
                
#RoutardApprox(H)     







#GRAPHE POUR TESTER , 
"""Q = {
    'a': {'b':1, 'c':1,'d':2 ,'e':2},
     'b': {'a':1, 'c':5, 'd':2 ,'e':2},
     'c': {'a':1, 'b':5, 'd':4},
     'd' : {'a':2 , 'b':6 , 'c':4},
    'e' : {'a':2 , 'b':2}
    }
    
H= {
    'a': {'b':1.54, 'c':2.97},
     'b': {'a':1.54, 'f':5, 'c':10.5},
     'c': {'a':2.97, 'b':10.5, 'f':2.33, 'e':4.25},
     'd': {'f':8.01, 'e':3.73},
     'e': {'c':4.25, 'd':3.73}, 
     'f': {'b':5, 'c':2.33, 'd':8.01} 
    }    """

