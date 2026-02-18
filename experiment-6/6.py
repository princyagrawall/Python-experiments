"""Write a lambda function which gives tuple of max and min from a list.
Sample input: [10, 6, 8, 90, 12, 56]
Sample output: (90,6)"""

find_max_min = lambda lst: (
    (lambda m, n: (m, n))(
        (lambda l: l[0] if len(l) == 1 else (l[0] if l[0] > find_max_min(l[1:])[0] else find_max_min(l[1:])[0]))(lst),
        (lambda l: l[0] if len(l) == 1 else (l[0] if l[0] < find_max_min(l[1:])[1] else find_max_min(l[1:])[1]))(lst)
    )
)

lst = [10, 6, 8, 90, 12, 56]
print(find_max_min(lst))
