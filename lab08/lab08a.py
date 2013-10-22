
import string

def build_word_set( input_file ):
    
    word_set = set()
    
    for line in input_file:

        # sets variable equal to the line which has been strip of leading and trailing characters (removed)
        # The line was also split of arbitrary strings of whitespace characters(spaces,tabs,etc.)
        word_lst = line.strip().split()

        # Sets variable to lowercase while also striping it of all punctuation for each w in the word_lst
        word_lst = [w.lower().strip(string.punctuation) for w in word_lst]
        
        for word in word_lst:
            
            if word != "":

                # If word isn't blank, then adds word to the set
                word_set.add( word )
                
    return word_set


def compare_files( file1, file2 ):

    # Build two sets:
    #   all of the unique words in file1
    word_set1=build_word_set(file1)
    #   all of the unique words in file2
    word_set2=build_word_set(file2)

    # Display's the total number of unique words between the
    # two files.  If a word appears in both files, it should
    # only be counted once.
    count=0
    total=word_set1&word_set2
    for i in total:
        count+=1
    print(count)

    # Display's the number of unique words which appear in both
    # files.  A word should only be counted if it is present in
    # both files.
    totalcount=0
    compared_total = set()
    compared_total = word_set1|word_set2
    #compared_total = {x for x in word_set1 if x in word_set2}
    for i in compared_total:
        totalcount+=1
    print(totalcount)
  
     
######################################################################

f1 = open( "document1.txt" )
f2 = open( "document2.txt" )

compare_files( f1, f2 )

f1.close()
f2.close()
  
    
    
