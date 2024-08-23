# You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence. It can be the only one.
# Input: Non-empty list of string (str).
# Output: A string (str).

def most_frequent(data: list[str]) -> str:
    result_dict = {}
    for elem in data:
        if result_dict.__contains__(elem):
            result_dict[elem] = result_dict[elem] + 1
        else:
            result_dict.update({elem: 1})
    max_val = max(result_dict, key=result_dict.get)
    print('The most frequently occuring string is "{}"\n'.format(max_val))
    return max_val


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

# These "asserts" are used for self-checking
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
