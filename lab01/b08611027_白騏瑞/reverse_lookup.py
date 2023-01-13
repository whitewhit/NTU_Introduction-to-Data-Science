def reverse_lookup(d, v):
    k = []
    for key, value in d.items():
        if v == value:
            k.append((value, key))
    return k

d = {"red" : "apple", "orange" : "orange", "yellow" : "banana", "green" : "watermelon", "black" : "watermelon"}
print(reverse_lookup(d, "watermelon"))