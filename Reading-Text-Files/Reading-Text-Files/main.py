# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 

    
    return "Hello World"
    


def count_words():
    #text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text = open("./story.txt", 'r')
    word_count_container = dict()
    for line in text:
        line = line.rstrip()
        words = line.split()
        words = [word.strip(".,!?:;") for word in words]

        for word in words:
            if word in word_count_container:
                word_count_container[word] = word_count_container[word] + 1

            else:
                word_count_container[word] = 1
        
    return word_count_container

print(count_words())
