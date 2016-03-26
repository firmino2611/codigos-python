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
			if x >= limInferior and x < limSuperior:  #os valores de cada classe deve ser colocado manualmente
				frequencia += repetidos[x]
		somatorio += frequencia
		print limInferior,'|--' ,limSuperior, '        ',frequencia,'      ', somatorio	
		frequencia = 0
		limInferior += intervalo
		limSuperior += intervalo
		iteracoes -= 1
	print '     somatorio = ',somatorio

numeros = input("digite os valores separados somente por virgula \n")	
intervalo = input("\nDigite o intervalo das classes: ") #intervalo das classes
inicial = input("\nDigite o limite inferior inicial: ") #limite mínimo 
final = input("\nDigite limite superior final: ") #limite máximo
frequencia(numeros,intervalo,inicial,final)
