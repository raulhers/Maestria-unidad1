import csv
import re
import json

def busca_palabras(param,parchivo_mt):
#	archivo_mt='/Users/RaulHernandez/Documents/GitHub/Maestria/unidad1/python/Sentimientos.txt'
	archivo_mt=parchivo_mt
	sentimientos=open(archivo_mt)
	valores={}
	for linea in sentimientos:
		termino, valor = linea.split("\t")
		valores[termino] = int(valor)
		texto=valores.keys()
			#print(texto)
		if valores.get(param):
			#print(valores.get(param))
			respuesta=int(valores.get(param))
			break
		else:
			respuesta=0
	return respuesta


#busca_palabras('good')
#print(calificacion)
#tweets=open(archivo_tw)
def califica_tweets(pbuscar,parchivo_tw,parchivo_mt):
	contarTotal=0
	contarNo=0
	contarSi=0
	descarte='delete'
	encontrar=pbuscar
	mtweets=[]

	tweets=open(parchivo_tw)
	for lineas in tweets:
		califica=0
		test = lineas
		contarTotal=contarTotal+1
		if re.findall(descarte,test):
			
			contarNo=contarNo+1
		
		elif re.findall(encontrar,test):
		    contarSi=contarSi+1
		    #lee liea a linea el archivo de tweets
		    data=json.read(test)
		    #separa en un diccionario los valores
		    if encontrar in data.keys():
		    	#almacenar los valores
		    	mtweets.append(data[encontrar].lower().split(" "))
		    	#recorrer cada palabra y calificarla
		    	for palabras in mtweets:
		    		#setear calificacion en 0 ya que vamos a recorrer el archivo y puede quedar pegado la calificacion, lo que genera un error
		    		califica=0
		    		cal2=0
		    		#recorrer la estructura para sacar palabra por palabra y buscarla en el archivo por parametro.
		    		for i in palabras:
		    			imprimir=i
		    			calificacion = busca_palabras(i,parchivo_mt)
		    			if calificacion !=0:
		    				print(imprimir+ ": "+ str("No mostramos esta palabra, dado que tiene un sentimiento ya asociado anteriormente."))
		    			else:
		    				print(imprimir+ ": 3")


		mtweets.clear()
		    	#print("EL TWEET: ", palabras, "TIENE UN SENTIMIENTO ASOCIADO DE ----->", califica, "\n")
	return contarTotal, contarSi, contarNo

if __name__ == "__main__":
	archiv_sentimiento = input("Ingrese el nombre del archivo ó matriz de SENTIMIENTOS: ")
	archivo_tweeter = input("Ingrese el nombre del archivo de TWEETS: ")
	#archiv_sentimiento = 'Sentimientos.txt'
	#archivo_tweeter = 'salida_tweets.txt'
	#archivo_tweeter = 'salida1.txt'
	total,si,no = califica_tweets('text',archivo_tweeter,archiv_sentimiento)
print("Total de tweets en el archivo:",total)
print("Total de tweets descartados:",no)
print("Total de tweets analizados:",si)