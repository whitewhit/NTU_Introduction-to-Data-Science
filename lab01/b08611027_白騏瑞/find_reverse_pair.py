def find_reverse_pair(word_list):
    reverse_pair_list = []
    for words1 in word_list:
        reverse_word = words1[::-1]

        for words2 in word_list:
            if reverse_word == words2:
                reverse_pair_list.append((words1, words2))
                word_list.remove(words2)
    return reverse_pair_list

a = ["geeks", "best", "tseb", "for", "skeeg"]
print(find_reverse_pair(a))