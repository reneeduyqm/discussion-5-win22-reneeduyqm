# Your name: Renee Du
# Your student id: 97626101
# Your email: reneedu@umich.edu
# List who you have worked with on this homework: Loria Sun

import re, os, unittest
from tempfile import tempdir
from xml.etree.ElementPath import find

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """

    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r', encoding='utf-8')

    # Read the lines from the file object into a list
    lines = infile.readlines()

    # Close the file object
    infile.close()

    # return the list of lines
    return lines

def find_movie_titles(string_list):
    """
    This function returns a dictionary with the keys being numbers, (1 - 8)
    and the values being the names of movies.
    """
    # pass

    dict = {}
    idx = 1
    for value in (string_list):
        if re.search("^Title: (\w+)",value): 
            value = value.strip()           
            temp = re.findall("Title: ([\w+\S*\s*]*)",value) 
            # temp =''.join(re.findall("[^Title: ]",value))
            dict[idx]=  temp[0]
            idx += 1
    # print(dict)

def find_and_phrases(string_list):
    """
    This function finds all phrases with the word "and"
    and then returns them in a list.
    """
    lst = []
    for w in string_list:
        if re.search("(\w+\s+and\s+\w+)",w):
            temp = re.findall("(\w+\s+and\s+\w+)",w)
            for t in temp:
                lst.append(t)
    

def find_urls(string_list):
    """
    This functions returns a list of valid urls in the list of strings
    """
    lst = []
    for w in string_list:
        w = w.strip()
        if re.search('((http|https)\:\/\/)www.\S+',w):
            temp = re.findall('((?:shttp|https)\:\/\/www.\S+)',w)
            lst.append(temp)
    # prin/t(lst)

def find_valid_release_dates(string_list):
    """
    This function returns a list of valid release dates.
    Sample format:
        mm/dd/yyyy
        mm/dd/yy
        mm-dd-yyyy
        mm-dd-yy
    Please refer to the instructions and be careful about invalid dates!
    """
    lst = []
    for w in string_list:
        w = w.strip()
        if re.search('(?:[0][1-9]|[1][0-2])(\/|\-)(?:((?:[0]|[1]|[2])[0-9])|[3][0-1])(\/|\-)(?:(19[0-9][0-9]|20[01][0-9]|2021)|[0-2][0-1])',w):
            temp = re.findall('?:[0][1-9]|[1][0-2]\/|\-?:?:[0]|[1]|[2][0-9]|[3][0-1]\/|\-?:19[0-9][0-9]|20[01][0-9]|2021|[0-2][0-1]',w)
            lst.append(temp)
    print(lst)

## Extra credit
def count_mid_str(string_list, string):
    """
    This function returns a count of the number of times a specified string appears
    in the text. The matched string should be in the middle of a word (ie: Not at 
    the start of end of a word).
    """
    pass

#Implement your own tests
class TestAllMethod(unittest.TestCase):

    def test_find_movie_titles(self):
        pass

    def test_find_valid_release_dates(self):
        pass

    def test_find_and_phrases(self):
        pass

    def test_find_urls(self):
        pass

    #Uncomment if working on Extra Credit
    #def test_count_mid_str(self):
    #    pass


def main():
    #Feel free run your functions here as well!
    file = read_file("/mnt/c/Users/loria/OneDrive/Desktop/SI206/hw5_win22-Loriasun/best_picture.txt")
    find_movie_titles(file)
    find_and_phrases(file)
    find_urls(file)
    find_valid_release_dates(file)
    # pass

if __name__ == '__main__':
    main()
    print()
    unittest.main(verbosity=2)