bailarines = [9,8,7,6,5,4,3,2,1]

def ordenamiento_burbuja(vector):

    for i in range(len(vector)):

        cambiado = False
        for j in range(0, len(vector) - i - 1):

            if vector[j] > vector[j + 1]:
                cambiado = True
                vector[j], vector[j + 1] = vector[j + 1], vector[j]

        if not cambiado:
            return vector

print(bailarines)
print(ordenamiento_burbuja(bailarines))