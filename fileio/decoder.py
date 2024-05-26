def main():
    #initialize some variables for counting and for the lists
    end = 0
    lst_full = []
    lst_ordered = []
    lst_short = []

    #read the file into lst_full[] read it in once, just the words into a numbered array, then close the file and be done with it
    with open('fileio/coding_qual_input.txt') as file:
        for line in file: 
            line = line.strip() # optional
            lst_full.append(line)
            #print(line)
    
    #initialize the ordered list to the size of the randomly ordered list of words
    lst_ordered = [None] * len(lst_full)

    #iterate through line_words and populate lst_ordered with properly placed words
    for line_words in lst_full:
        #split the line string into an array of substrings by space separator 
        line_words = line_words.split(" ")
        if len(line_words) > 1:
            #first split item is the number index of the word
            num = int(line_words[0]) 
            #second split item is the word
            word = line_words[1]
            #assign just the word to the lst_ordered array with an index of num-1
            lst_ordered[num -1] = word

    #initialize end to 0 outside the loop
    end = 0
    collected_words = []
    #cycle through the list appending only the relevant words according to the code
    for row in range(1, len(lst_ordered) - 1, 1):
        end = row + end
        if end < len(lst_ordered):
            collected_words.append(lst_ordered[end - 1])
    result_string = " ".join(collected_words)
    print(result_string)

    #write the result_string to a text file
    file_path = "fileio/resultstring.txt"

    with open(file_path, "w") as file:
        file.write(result_string)

if __name__ == "__main__":
    main()