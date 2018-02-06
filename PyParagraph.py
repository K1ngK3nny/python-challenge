# assigning variables
filename = "paragraph_1.txt"
numWords = 0
numChar = 0
# reading the file
with open(filename, 'r') as file:
    file_contents = file.read()
    sentence_count = file_contents.count('.')
# reading file and itterating
with open(filename, 'r') as file:
    for line in file:
        # create a list for words
        wordList = line.split()
        numWords += len(wordList)
        numChar += len(line)

# average word length by letter count
# average sentence length by word count
avg_ltr_cnt = numChar / numWords
avg_snt_ln = numWords / sentence_count
print("Paragraph Analysis")
print("-------------------------")
print("Total Word Count:", numWords)
print("Sentence Count:", sentence_count)
print("Average Letter Count:", avg_ltr_cnt)
print("Average Sentence Length:", avg_snt_ln)
