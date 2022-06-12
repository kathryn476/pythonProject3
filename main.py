# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


#a=open("story.txt", "r")
#print(a.read())
def read_file_content(filename):
    f = open('story.txt')
    filename = f.read
    return filename

def count_words():
    # [assignment] Add your code here
    text = read_file_content("story.txt")
    words_of_text = text.split()
    count = dict()
    for word in words_of_text:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1


a = count_words()
print(a)









