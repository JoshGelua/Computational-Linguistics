from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.cluster import hierarchy
from sklearn.decomposition import PCA



PERCEPTUAL_MATRIX_FILE = 'data/perceptual_color_mat.tsv'


def write_matrix(output_file, matrix, column_labels):
    """
    output_file: str
    matrix: np.array
    column_labels: list of str
    
    Each line is tab-separated. The first item is the column_label identifier.
    The remaining items are features for the 330 Munsell color chips in order.
    """
    with open(output_file, 'w') as f:
        for i, col in enumerate(matrix.T):
            f.write(column_labels[i] + '\t' + '\t'.join([str(item) for item in col.tolist()]) + '\n')
    

def load_matrix(matrix_file):
    """
    matrix_file: str -- path to load matrix from
    
    Return a tuple of (matrix, column_labels) where matrix is an np.array
    and column_labels is a list of str containing the names of the features
    for each column. The file matrix_file should have the same format as
    the output of write_matrix.
    """
    column_labels = []
    column_label_to_column = {}
    with open(matrix_file, 'r') as f:
        for line in f:
            line = line.strip().split('\t')
            column_labels.append(line[0])
            column_label_to_column[line[0]] = np.array([float(item) for item in line[1:]])
    result = np.zeros((len(column_label_to_column[column_labels[0]]), len(column_labels)))
    for i, column_label in enumerate(column_labels):
        result[:, i] = column_label_to_column[column_label]
    return result, column_labels
  
  
def get_perceptual_matrix_rgb():
    """
    Load the L*a*b* matrix from PERCEPTUAL_MATRIX_FILE, and convert the data
    to RGB colors, (so that they can be used to color points in matplotlib).
    The resulting matrix should be of the shape (N_CHIPS, 3).
    """
    perceptual_mat, __ = load_matrix(PERCEPTUAL_MATRIX_FILE)
    perceptual_mat = perceptual_mat
    result_mat = np.zeros(perceptual_mat.shape)
    for i, row in enumerate(perceptual_mat):
        l, a, b = row
        lab = LabColor(l, a, b)
        rgb = convert_color(lab, sRGBColor)
        result_mat[i, :] = [min(val, 1.0) for val in rgb.get_value_tuple()]
    return result_mat
  
  
def create_pca_graph(chip_by_term_mat_pca, title=None):
    """
    chip_by_term_mat_pca: 2D np.array -- pca-ed chip_by_term matrix of shape
    	(N_CHIPS, n) where n is in {1, 2, 3}. The rows of chip_by_term_mat_pca
        should correspond to the chip id numbers (with chip 1 in index 0).
    title: str -- title for the graph plotted
    
    Generate a scatter plot of points in chip_by_term_mat_pca, with each point
    colored with the colors of the color chips.
    """
    perceptual_mat_rgb = get_perceptual_matrix_rgb()
    x_values = [item[0] for item in chip_by_term_mat_pca]
    color = [perceptual_mat_rgb[i] for i in range(len(x_values))]
    dim = chip_by_term_mat_pca.shape[1]
    assert dim in [1, 2, 3], \
        "Matrix must have dim in {1, 2, 3}, but instead found {}".format(dim)
    
    fig = plt.figure()
    if dim == 1:
        plt.scatter(x_values, np.zeros(len(x_values)), color=color)
    if dim == 2:
        y_values = [item[1] for item in chip_by_term_mat_pca]
        plt.scatter(x_values, y_values, color=color)
    elif dim == 3:
        y_values = [item[1] for item in chip_by_term_mat_pca]
        z_values = [item[2] for item in chip_by_term_mat_pca]
        ax = Axes3D(fig)
        ax.scatter(x_values, y_values, z_values, color=color)
        
    if title:
        plt.title(title)
    plt.show()
