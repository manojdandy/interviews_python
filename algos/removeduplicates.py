def remove_duplicates(input:str):
    unique_chars = set()
    result = ""
    for char in input:
        if char not in unique_chars:
            unique_chars.add(char)
            result  += char
    return result


def count_words_sentenct(input:str)->dict:
    words_count = {}
    for word in input.split():
        if word in words_count:
            words_count[word] = words_count[word] + 1
        else:
            words_count[word] = 1
    return words_count

def reverse_words(input:str):
    reverse_words = "" 
    words = input.split()
    for word in words[::-1]:
        reverse_words = reverse_words + " " + word
    return reverse_words

        
if __name__=="__main__":
    output = remove_duplicates("hello world")
    print(output)
    count_words_sentence = count_words_sentenct("hello ram ram is here, hello ram")
    print(count_words_sentence)
    print(reverse_words("hello world"))