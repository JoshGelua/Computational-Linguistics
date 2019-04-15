from collections import Counter
import csv
import string


### Functions for Part 2: Surprisal and Reading Times ###


def read_sentences_and_reading_times(path_to_corpus):
    """
    path_to_corpus: str -- path to where the corpus is.
    
    Read in each sentence and each word in the corpus. Return sentences, reading_times, where sentences is a 
    list of list of str and reading_times is a list of list of reading times. Each item in reading_times
    should correspond to the item at the same index in sentences.
    
    Note: make sure to convert each word to lowercase, and strip each word of punctuation.
    """
    sentences = []
    curr_sentence = []
    reading_times = []
    curr_reading_times = []
    with open(path_to_corpus, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        headers = next(csv_reader)  # skip headers
        for row in csv_reader:
            word = row[1].lower()
            reading_time = row[-1]
            curr_sentence.append(word.strip(string.punctuation))
            curr_reading_times.append(float(reading_time))
            if word[-1] == '.':
                sentences.append(curr_sentence)
                reading_times.append(curr_reading_times)
                curr_sentence = []
                curr_reading_times = []
    return sentences, reading_times


### Functions for Part 3: Surprisal and Concreteness ###


def get_bigram_counts(path_to_file):
    """
    path_to_file: str -- path to corpus file
    
    Return a Counter mapping bigram tuples to their frequency in the corpus at path_to_file.
    """
    result = Counter()
    with open(path_to_file, 'r') as f:
        for line in f:
            line = line.lower().split()
            for i in range(len(line) - 1):
                result.update([tuple(line[i: i + 2])])
    return result


def read_concreteness(path_to_file):
    """
    path_to_file: str -- path to Calgary Concreteness data set csv.
    
    Return a list of concreteness scores and a list of words. The concreteness scores
    correspond to the words at the same index in the list of words.
    """
    concreteness = []
    words = []
    with open(path_to_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        headers = next(csv_reader)  # skip headers
        for row in csv_reader:
            concreteness.append(float(row[1]))
            words.append(row[0])
    return concreteness, words


def load_words(path_to_file):
    """
    path_to_file: str -- path to one of the noun list files (e.g. 'data/all_nouns.txt')
    
    Return a list of all the words in the file at path_to_file.
    """
    with open(path_to_file, 'r') as f:
        words = f.readlines()
    return [item.strip() for item in words]