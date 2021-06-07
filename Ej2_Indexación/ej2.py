def buildIndex():
    load = {}
    for bookNumber in range(6):
        with open("Ej1_Preprocesamiento/preprocesados/" + str(bookNumber + 1) + ".txt", 'r') as book:
            temp = {}
            for term in book.read().split('\n'):
                if term not in temp:
                    if term not in load:
                        load[term] = ((bookNumber + 1),)
                    else:
                        newTuple = list(load[term])
                        newTuple.append(bookNumber + 1)
                        load[term] = tuple(newTuple)
                temp[term] = True
    keys = sorted(load.items(), key=lambda x: len(x[1]), reverse=True)
    keys = keys[:501]
    keys.sort(key=lambda x: x[0])
    with open("Ej2_Indexación/inverted_index.txt", 'w') as index:
        for value in keys[1:]:
            index.write(value[0] + ':')
            books = ''
            for book in value[1]:
                books += str(book) + ','
            index.write(books[:-1] + '\n')