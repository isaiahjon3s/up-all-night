import random


def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]
    list3 = [11, 12, 13, 14, 15]
    list4 = [16, 17, 18, 19, 20]
    list5 = [21, 22, 23, 24, 25]
    list6 = [26, 27, 28, 29, 30]
    list7 = [31, 32, 33, 34, 35]
    list8 = [36, 37, 38, 39, 40]
    list9 = [41, 42, 43, 44, 45]
    list10 = [46, 47, 48, 49, 50]
    list11 = [51, 52, 53, 54, 55]

    list_of_lists = [list1, list2, list3, list4, list5, list6, list7, list8, list9, list10, list11]

    random_list1 = random.choice(list_of_lists)
    random_list2 = random.choice(list_of_lists)

    mulitplied_list = multiply_list(random_list1, random_list2)
    print(mulitplied_list)


def multiply_list(list1, list2):
    mulitplied_list = []
    for i in range(len(list1)):
        mulitplied_list.append(list1[i] * list2[i])
    return mulitplied_list


if __name__ == "__main__":
    main()