# mt_recursion.py

def zip_with_rec(op, list1, list2):
    # Base case: if both lists are empty, return an empty list
    if not list1 and not list2:
        return []
    # Recursive case: combine the first elements and recurse on the rest
    return [op(list1[0], list2[0])] + zip_with_rec(op, list1[1:], list2[1:])

if __name__ == '__main__':
    print(f'{zip_with_rec(lambda a, b: a + b, [1, 2, 3, 4, 5], [-1, 0, 1, 2, 3]) = }')
    # output: zip_with_rec(lambda a,b: a + b, [1,2,3,4,5], [-1,0,1,2,3]) = [0, 2, 4, 6, 8]

    print(f'{zip_with_rec(lambda a, b: a - b, [1, 2, 3, 4, 5], [-1, 0, 1, 2, 3]) = }')
    # output: zip_with_rec(lambda a,b: a - b, [1,2,3,4,5], [-1,0,1,2,3]) = [2, 2, 2, 2, 2]

print(f'{zip_with_rec(lambda a, b: a * b, [1, 2, 3, 4, 5], [-1, 0, 1, 2, 3]) = }')
  # output: zip_with_rec(lambda a,b: a * b, [1,2,3,4,5], [-1,0,1,2,3]) = [-1, 0, 3, 8, 15]