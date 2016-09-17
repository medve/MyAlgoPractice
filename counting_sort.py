def zeros(n):
    return [0 for _ in range(n)]

def counting_sort(lst, max_n, key = None):
    number_countings = zeros(max_n + 1)
    for number in lst:
        number_countings[key(number)] += 1
    for i, (cur_num, prev_num) in enumerate(zip(number_countings[1:],
                                             number_countings)):
        number_countings[i+1] = cur_num + prev_num
    result_list = zeros(len(lst))
    for number in lst[::-1]:
        number_idx = number_countings[key(number)] - 1
        result_list[number_idx] = number
        number_countings[key(number)] -= 1
    return result_list


def radix_sort(lst, rad = 32):
    result_list = lst
    for shift in range(rad):
        result_list = counting_sort(result_list, 10, 
                                     key = lambda x:(x//10**shift)%10)
    return result_list

if __name__ == "__main__":
    print(counting_sort([2,4,1,5,1,51,2,1,5,15,123,55,1,21,23,124],124, 
                         key = lambda x:x%10))

    print(radix_sort([1,2214,41245,161345,51235213,11345,511259567,
                         26784,1547567,545867373,15458769,123,679755,
                         13586,21,23,1241345]))