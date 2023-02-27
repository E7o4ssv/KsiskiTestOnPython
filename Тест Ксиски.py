import math


def kasiski_test(ciphertext, ngram_length=4):
    ngram_to_indices = {}
    for i in range(len(ciphertext) - ngram_length + 1):
        ngram = ciphertext[i:i+ngram_length]
        if ngram in ngram_to_indices:
            ngram_to_indices[ngram].append(i)
        else:
            ngram_to_indices[ngram] = [i]
    distances = []
    for ngram, indices in ngram_to_indices.items():
        if len(indices) > 1:
            for i in range(len(indices) - 1):
                distance = indices[i+1] - indices[i]
                distances.append(distance)
    return distances


def find_key_length(distances):
    gcds = []
    for i in range(len(distances) - 1):
        for j in range(i+1, len(distances)):
            gcd = math.gcd(distances[i], distances[j])
            if gcd > 1:
                gcds.append(gcd)
    if len(gcds) == 0:
        return None
    else:
        return max(set(gcds), key=gcds.count)

print("___________________________________________________________________________________________")
print("*ВАЖНО!*")
print("Для корректной работы программы удалите из текста все знаки припинания и пробелы!")
print("___________________________________________________________________________________________")

ciphertext = input("Введите зашифрованный текст: ")

distances = kasiski_test(ciphertext)
key_length = find_key_length(distances)

print("Длина ключа:", key_length)