import numpy as np

def write_vectors(output_file, word_vector_dict):
    """
    output_file: str -- path to file to write vectors to
    word_vector_dict: dict of str to list of float -- dictionary mapping words to vectors.
    
    Writes all vectors in word_vector_dict to output_file. There is one vector per line.
    Each line starts with the word for the vector, which is followed by a tab and then the
    vector values. The vector values are also separated by tabs.
    """
    with open(output_file, 'w') as f:
        for word, vector in word_vector_dict.items():
            output = [str(item) for item in vector.tolist()]
            output = [word] + output
            f.write('\t'.join(output) + '\n')


def load_vectors(path_to_file):
    """
    path_to_file: str -- path to file to read vectors from
    
    Returns a dict of str to list of float, which maps words to their vectors. The
    words and vectors are loaded from path_to_file.
    """
    word_vector_dict = {}
    with open(path_to_file) as f:
        for line in f:
            line = line.split('\t')
            word = line[0]
            vector = np.array(line[1:])
            word_vector_dict[word] = vector
    return word_vector_dict


def get_vocab(vocab_file):
    """
    vocab_file: str -- path to vocabulary file
    
    Returns a list of str, where each str in the list is a line in vocab_file.
    """
    with open(vocab_file) as f:
        vocab = f.readlines()
    vocab = [item.strip('\n').lower() for item in vocab]
    return vocab