from simulation.controller.controller import *
from simulation.controller.proxy import ProxySimu, ProxyReal

def initializeProxy(rob, env):

	if config.simu_or_real == 1: #importe proxy simulation
		proxy = ProxySimu(rob, env)
		
	elif config.simu_or_real == 2: #importe proxy réel
		proxy = ProxyReal(rob)

	return proxy

class SetStrategies :

	def __init__(self,rob, env) :
		proxy = initializeProxy(rob,env)

		#Prépare des séquences de stratégies que le controleur va executer
		self.sequences = [] #la liste contenant les séquences de stratégies 
		seq2=StrategySeq(proxy)


		#Test des Strategies :
		
		#test 1 : Strategie pour avancer
		#s1=moveForwardStrategy(proxy, 500, 50) 
		#seq2.addStrategy(s1)
		#test 2 : Strategie pour tourner
		#s2=TurnStrategy(proxy, 90, 30) # Strategie pour 
		#seq2.addStrategy(s2)
		#test 3 : Strategie pour faire un arc 
		#s3 = ArcStrategy(proxy, 180, 50, 20, 0) 
		#seq2.addStrategy(s3)
		#test 4 : Strategie Pour naviger le robot 
		#s4=Navigate(proxy,250,48) # grande distance pour voir le comportement du robot. 
		#seq2.addStrategy(s4)

		#self.sequences.append(seq2)


		#Test des Sequences de strategie
		#seq1 = SquareStrategy(proxy,300,50)
		seq2=TriangleEquiStrategy(proxy,40,50)
		#seq3=RepeatMotif1Strategy(proxy, 100)
		#seq4 = detect_balise(proxy, "B", 50)
		
		self.sequences.append(seq2)


