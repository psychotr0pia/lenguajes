#funcion para quitar las stopwords de forma recursiva
def quitarStopwords(paginasWeb, listaStopwords):

    #si la stopword no esta en el texto, la quitamos de la lista
    if listaStopwords and listaStopwords[0] not in paginasWeb:
        #quitar stopword
        listaStopwordsActualizada = listaStopwords[1:]
        #llamamos la funcion de nuevo
        return quitarStopwords(paginasWeb, listaStopwordsActualizada)
    elif not listaStopwords: #lista vacia, no hay mas stopwords que sacar!
        return paginasWeb
    else: #si la stopword esta en el texto, la quitamos del texto
        stopword = listaStopwords[0]
        print(f"Quitando stopword {stopword}")
        paginasWebActualizada = paginasWeb.replace(stopword, '') #la quitamos y la reemplazamos por ''
        return quitarStopwords(paginasWebActualizada, listaStopwords)

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
