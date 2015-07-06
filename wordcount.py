# put your code here.
def word_count(filename):
    """ Counts the number of times the word appears in the file.

    Outputs key-value pairs in a dictionary.
    """
    file_object = open(filename)
    word_count = {}
    list_of_words = []
    occurances = 1

    for line in file_object:
        each_line = line.rstrip().split(" ")
        list_of_words.append(each_line)

    for sentence in list_of_words:
        for word in sentence:
            if word in word_count:
                occurances += 1
            else:
                word_count[word] = occurances
               
    return word_count

print word_count("test.txt")


