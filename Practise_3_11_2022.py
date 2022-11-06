from functools import reduce


def title(name):
    print(name)  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    title("Practise_3_11_2022")

    '''

    new_list = []

    def multiply_by2(li):
        for item in li:
            new_list.append(item * 2)
        return new_list


    new_list = ''
    print(multiply_by2([1, 2, 3]))
    '''

    #     map, filter,, zip and reduce
    my_list = [1, 2, 3]


    def multiply_by2(item):
        return item * 2


    print(list(map(multiply_by2, my_list)))
    print(my_list)


    #    filter

    def only_odd(item):
        return item % 2 != 0


    print(list(filter(only_odd, my_list)))

    your_list = (10, 20, 30)
    their_list = (5, 4, 3)
    print(list(zip(my_list, your_list, their_list)))


    # reduce

    def accumulator(acc, item):
        print(acc, item)
        return acc + item


    print(reduce(accumulator, my_list, 0))

    # lambda

    print(reduce(lambda acc, item: acc + item, my_list))

    #   Tasks

    #   square
    print(list(map(lambda item: item ** 2, my_list)))

    #   list sorting (sort second element in each tuple in the list)
    a = [(0, 2), (4, 3), (10, -1), (9, 9)]
    a.sort(key=lambda x: x[1])
    print(a)

    #   Comprehension (list, set, dictionary)

    my_list2 = [char for char in 'hello']
    my_list3 = [num for num in range(0, 100)]
    my_list4 = [num ** 2 for num in range(100)]
    my_list5 = [num for num in my_list4 if num % 2 == 0]

    print(my_list2)
    print(my_list3)
    print(my_list4)
    print(my_list5)

    simple_dict = {
        'a': 1,
        'b': 2
    }

    my_dict = {key: value ** 2 for key, value in simple_dict.items()}
    my_dict_1 = {num: num ** 2 for num in [1, 2, 3]}

    print(my_dict)
    print(my_dict_1)

    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

    some_list1 = list(set([num for num in some_list if some_list.count(num) > 1]))

    print(some_list1)

    """
    
    Practise_3_11_2022
    [2, 4, 6]
    [1, 2, 3]
    [1, 3]
    [(1, 10, 5), (2, 20, 4), (3, 30, 3)]
    0 1
    1 2
    3 3
    6
    6
    [1, 4, 9]
    [(10, -1), (0, 2), (4, 3), (9, 9)]
    ['h', 'e', 'l', 'l', 'o']
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801]
    [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500, 2704, 2916, 3136, 3364, 3600, 3844, 4096, 4356, 4624, 4900, 5184, 5476, 5776, 6084, 6400, 6724, 7056, 7396, 7744, 8100, 8464, 8836, 9216, 9604]
    {'a': 1, 'b': 4}
    {1: 1, 2: 4, 3: 9}
    ['n', 'b']
    
    Process finished with exit code 0

    
    """