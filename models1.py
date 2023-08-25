from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import joblib
import pandas as pd
import numpy as np
import torch

tokenizer = joblib.load('tokenizer_albert_VF.pkl')
model = joblib.load('ALBERT_VF.pkl')



def try_model(M, data, text = False, cm = False):
    
    X_train = data[0]
    X_test = data[1]
    y_train = data[2]
    y_test = data[3]
    
    if text == True:
        vectorizer = TfidfVectorizer(max_features = 1000, stop_words = stopwords + ['si', 'según', 'tras'])
        X_train = vectorizer.fit_transform(X_train)
        X_test = vectorizer.transform(X_test)
    
    M.fit(X_train, y_train)
    y_pred_train = M.predict(X_train); y_pred = M.predict(X_test)
    
    acc_train = metrics.accuracy_score(y_train, y_pred_train)
    acc = metrics.accuracy_score(y_test, y_pred)

    if cm == True:
        cm_test = confusion_matrix(y_test, y_pred, labels = M.classes_)
        disp = ConfusionMatrixDisplay(confusion_matrix = cm_test, display_labels = M.classes_)  

        disp.plot()
        plt.show()
    
    print(f'accuracy en train: {acc_train}, accuracy en test: {acc}')
    
    

def newspaper_classifier(lista):
    # Se podría haber utilizado aquí también el modelo ALBERT, que proporciona mejores resultados, pero como el objetivo no es predecir periódico individual sino clasificar por veracidad, he preferido utilizar algo más sencillo en este punto y así mostrar cómo el algoritmo funciona relativamente bien incluso con un enfoque consideráblemente más simple y en clasificación múltiple.
    
    noticia = lista[0]
    
    vectorizer = joblib.load('tfidf_vectorizer1.pkl')
    logit = joblib.load('regresion_logistica1.pkl')
    
    string_vect = vectorizer.transform(lista)
    pred = logit.predict(string_vect)[0]
    
    y = ''
    # X_test_final = pd.read_csv('X_test_final.csv')
    # y_test_final = pd.read_csv('y_test_final.csv')
    
    textos = X_test_final.values.tolist()
    subcadena = noticia[5:-5]
    
    resultados = np.char.find(textos, subcadena)
    
    if np.any(resultados >= 0):
        i = np.where(resultados >= 0)[0][0]
        texto_encontrado = textos[i][0]  # Obtenemos el texto encontrado
        if len(texto_encontrado) <= len(subcadena) + 10:
            y = y_test_final.iloc[i].Periódico

    return y, pred


def VF_classifier(lista):
    
    noticia = lista[0]
    
    val_encoding = tokenizer(noticia, truncation=True, padding=True, return_tensors="pt")#.to(device)
    outputs = model(**val_encoding)
    logits = outputs.logits.cpu().detach().numpy()
    pred = (np.argmax(logits))

    return pred