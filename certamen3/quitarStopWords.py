
#funcion para quitar las stopwords de forma recursiva
def quitarStopwords(texto, listaStopwords):
    # Dividemos el texto en lineas
    lineas = texto.split('\n')

    # BUscamos en cada linea
    for i in range(len(lineas)):
        # Limpieza
        linea = lineas[i].strip()

        # checkamos si el stopword esta en las lineas
        for stopword in listaStopwords:
            if linea.startswith(stopword):
                # si encontramos la stopword, la quitamos de la lista
                listaStopwords.remove(stopword)
                #quitamos la palabra de la linea
                linea = linea[len(stopword):].strip()
                print(f"quitamos stop word {stopword} de la linea {i}")
                #volvemos a unir las lienas en un puro texto
                textoMod = '\n'.join(lineas)
                #llamada recursiva con el texto modificado
                quitarStopwords(textoMod, listaStopwords)
    #si no encontramos mas stopwords, devolvemos el texto
    texto = '\n'.join(lineas)
    return texto


with open('indexINvertido.txt', 'r', encoding='utf-8') as paginasWeb:
    paginasWeb = paginasWeb.read()

listaStopwords = stopwords = [
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd",
    'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself',
    'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this',
    'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
    'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while',
    'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above',
    'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once',
    'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some',
    'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don',
    "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't",
    'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn',
    "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren',
    "weren't", 'won', "won't", 'wouldn', "wouldn't"
]

paginasWebStopwordnt = quitarStopwords(paginasWeb, listaStopwords)
with open('indexInvertidoFiltrado.txt', 'w', encoding='utf-8') as indexInvertidoFiltrado:
    indexInvertidoFiltrado.write(paginasWebStopwordnt)
