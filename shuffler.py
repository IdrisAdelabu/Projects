def index_map(word):
    index_list = []
    place = []
    for x in word_list:
        if word_list.count(x) > 1:
            if x not in place:
                a = des_copy.index(x)
                index_list.append(a)
                des_copy.pop(a)
            else:
                jk = len(place)
                a = des_copy.index(x)
                index_list.append(a + jk)
                des_copy.pop(a)
            place.append(x)

        else:
            a = des_list.index(x)
            index_list.append(a)

    return index_list

def word_swap(word):
    cond = True
    counter = 0

    while cond:
        i = 0


        scond = True
        for y in word_list:
            j = arb_list.index(y)
            k = arb_list.index(y)
            if scond == False:
                continue
            else:

                while y != arb_list[position[i]] and j < l:

                    if position[i] - arb_list.index(y) > 0:
                        if arb_list[j] == arb_list[j + 1]:
                            j += 1
                            c = arb_list[j]
                            d = arb_list[j + 1]
                            arb_list[j + 1] = c
                            arb_list[j] = d
                            print(''.join(arb_list))
                            scond = False

                        else:
                            c = arb_list[j]
                            d = arb_list[j + 1]
                            arb_list[j + 1] = c
                            arb_list[j] = d
                            print(''.join(arb_list))
                            scond = True

                    elif position[i] - arb_list.index(y) < 0:
                        if arb_list[k] == arb_list[k - 1]:
                            k -= 1
                            c = arb_list[k]
                            d = arb_list[k - 1]
                            arb_list[k - 1] = c
                            arb_list[k] = d
                            print(''.join(arb_list))
                            scond = False

                        else:
                            c = arb_list[k]
                            d = arb_list[k - 1]
                            arb_list[k - 1] = c
                            arb_list[k] = d
                            print(''.join(arb_list))
                            scond = True

                    else:
                        print(''.join(arb_list))
                        scond = True
                        break
                    k -= 1
                    j += 1
                counter += 1

            i += 1

        if arb_list == des_list:
            cond = False

    print(f"The number of iterations is: {counter}")


word = input('type the word to be shuffled here: ').upper()
word_list = list(word)

des_word = input('input the desired anagram: ').upper()
des_list = list(des_word)
l = len(word_list)
des_copy = des_list.copy()

position = index_map(word)
arb_list = word_list.copy()

print(word)
word_swap(word)

