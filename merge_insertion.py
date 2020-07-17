def merge_insertion_sort(collection):
    def binary_search_insertion(sorted_list, item):
        left = 0
        right = len(sorted_list) - 1
        while left <= right:
            middle = (left + right) // 2
            if left == right:
                if sorted_list[middle] < item:
                    left = middle + 1
                    break;
                else:
                    break;
            elif sorted_list[middle] < item:
                left = middle + 1
            else:
                right = middle - 1
        sorted_list.insert(left, item)
        return sorted_list

    def sortlist_2d(list_2d):
        def merge(left, right):
            result = []
            while left and right:
                if left[0][0] < right[0][0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            return result + left + right

        length = len(list_2d)
        if length <= 1:
            return list_2d
        middle = length // 2
        return merge(sortlist_2d(list_2d[:middle]), sortlist_2d(list_2d[middle:]))

    if len(collection) <= 1:
        return collection

    two_paired_list = []
    is_surplus      = False
    for i in range(0, len(collection), 2):
        if (i == len(collection) - 1):
            is_surplus = True
        else:
            if collection[i] < collection[i+1]:
                two_paired_list.append([collection[i], collection[i+1]])
            else:
                two_paired_list.append([collection[i+1], collection[i]])
    sorted_list_2d = sortlist_2d(two_paired_list)
    result = [i[0] for i in sorted_list_2d]
    result.append(sorted_list_2d[-1][1])

    if is_surplus:
        pivot = collection[-1]
        result = binary_search_insertion(result, pivot)

    is_surplus_inserted_before_this_index = False
    for i in range(len(sorted_list_2d) - 1):
        if result[i] == collection[-i]:
            is_surplus_inserted_before_this_index = True
        pivot = sorted_list_2d[i][1]
        if is_surplus_inserted_before_this_index:
            result = result[:i+2] + binary_search_insertion(result[i+2:], pivot)
        else:
            result = result[:i+1] + binary_search_insertion(result[i+1:], pivot)

    return result

A = [100, 2000, 999, -2, 5]
print(merge_insertion_sort(A))
B = []
print(merge_insertion_sort(B))
C = ['A', 'Z', 'T', 'C']
print(merge_insertion_sort(C))
