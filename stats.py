def sort_on(dict):
    return dict["count"]

def word_count(text):
    return len(text.split())

def char_count(text):
    lower_text = text.lower()
    result = {}

    for char in lower_text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result

def sort_dictionaries(dictionary):
    sorted = []

    for entry in dictionary:
        new_dictionary = {}
        new_dictionary["char"] = entry
        new_dictionary["count"] = dictionary[entry]

        sorted.append(new_dictionary)

    sorted.sort(reverse=True, key=sort_on)

    return sorted