import os.path
from Ej1_Preprocesamiento.ej1 import readBook
from Ej2_Indexación.ej2 import buildIndex

if __name__ == "__main__":
    for i in range(6):
        readBook(i + 1)
    buildIndex()