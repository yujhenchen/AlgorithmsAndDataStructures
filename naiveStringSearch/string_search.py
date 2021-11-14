def string_search(str, sub_str):
    # count the frequency of sub_str in str
    # use a window to sub str and compare with sub_str
    count = 0
    str_len = len(str)
    sub_str_len = len(sub_str)
    for i in range(str_len - sub_str_len + 1):
        # print(str[i : sub_str_len + i ])
        if str[i : sub_str_len + i] == sub_str:
            count += 1
    return count


print(string_search("abc", "abcd"))
print(string_search("abc", "abc"))
print(string_search("dabc", "abc"))
print(string_search("abcd", "abc"))
print(string_search("abcddabc", "abc"))
print(string_search("abcabcdd", "abc"))
