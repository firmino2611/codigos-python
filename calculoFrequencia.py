#-*- coding: utf-8 -*-

def frequencia(valores,intervalo,inicial,final):
	repetidos = {}
	limInferior = inicial
	limSuperior = limInferior + intervalo
	frequencia = 0
	somatorio = 0
	iteracoes = (final-inicial)/intervalo
	for c in valores:
		if c in repetidos:
			repetidos[c] += 1
		else:
			repetidos[c] = 1
	print 'Classe        |   fi   |    Fi  '
	while iteracoes:
		for x in repetidos:
			if x >= limInferior and x < limSuperior:	#os valores de cada classe deve ser colocado manualmente
				frequencia += repetidos[x]
		somatorio += frequencia
		print limInferior,'|--' ,limSuperior, '        ',frequencia,'      ', somatorio	
		frequencia = 0
		limInferior += intervalo
		limSuperior += intervalo
		iteracoes -= 1
	print '     somatorio = ',somatorio

#68,85,33,52,65,77,84,65,74,57,71,35,81,50,35,64,74,47,54,68,80,61,41,91,55,73,59,53,77,45,41,55,78,48,69,85,67,39,60,76,94,98,66,66,73,42,65,94,88,89

numeros = input("digite os valores separados somente por virgula \n")	#3.9,7.4,10.0,11.8,2.3,4,5,10.5,8.4,15.6,7.6,18.8,2.9,0.4,5.0,9.0,5.5,9.2,12.4,8.7,4.5,4.4,10.6,5.6,8.5,2.4,17.8,11.6,0.8,4.4,7.1,3.2,2.7,16.2,2.7,9.5,13.1,3.8,6.3,7.9,4.8,5.3,12.9,6.9,6.3,7.5,2.6,3.3,4.6,16.0
intervalo = input("\nDigite o intervalo das classes: ") #intervalo das classes
inicial = input("\nDigite o limite inferior inicial: ") #limite mínimo 
final = input("\nDigite limite superior final: ") #limite máximo
frequencia(numeros,intervalo,inicial,final)
