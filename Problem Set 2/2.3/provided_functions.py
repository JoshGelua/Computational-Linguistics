import matplotlib.pyplot as plt
import numpy as np
from data import BEG_PHON_TAGS, SEMANTIC_TAGS, kid_answers, features_by_trial


def get_trials(semantic_filter=[], beg_phonological_filter=[]):
    """
    semantic_filter: list of int -- list of features. Each trial index returned must correspond
    	to a trial with a semantic feature in semantic_filter.
    beg_phonological_feature: list of int -- list of features. Each trial index returned must correspond
    	to a trial with a initial phonological feature in beg_phonological_filter.
        
    Return a list of trial indices where the semantic feature is in semantic_filter and the phonological
    feature is in beg_phonological_filter.
    """
    assert semantic_filter == [] or all([item in SEMANTIC_TAGS for item in semantic_filter]), \
        'invalid semantic filter'
    assert beg_phonological_filter == [] or all([item in BEG_PHON_TAGS for item in beg_phonological_filter]), \
        'invalid beg_phonological_filter'

    selected_trials = []
    n_trials = len(kid_answers)
    for i in range(n_trials):
        if ((beg_phonological_filter == [] or features_by_trial['beg_phonological'][i] in beg_phonological_filter) and
                (semantic_filter == [] or features_by_trial['semantic'][i] in semantic_filter)):
            selected_trials.append(i)
    return selected_trials


def bar_graph(class_probabilties, title=None):
    """
    class_probablities: 1-dimensional np.array of length 4.
    title: str -- title for the bar graph
    
	Generate a bar graph of class_probabilities.
    """
    fig, ax = plt.subplots()
    ind = np.arange(1, 5)
    class1, class2, class3, class4 = plt.bar(ind, class_probabilties)
    ax.set_xticks(ind)
    ax.set_xticklabels(['c1', 'c2', 'c3', 'c4'])
    ax.set_ylim([0, 1])
    ax.set_ylabel('Class Probability')
    ax.set_xlabel('Noun Class')
    if title:
      ax.set_title(title)
    plt.show()


def visualise_results(results, semantic_filter=[], beg_phonological_filter=[], title=None):
    """
    results: 
    semantic_filter: list of int corresponding to semantic features (see semantic
    	feature values in data.py)
    beg_phonological_filter: list of int corresponding to phonological features
    	(see phonological feature values in data.py)
    title: str -- title for the bar graph
    
    Generate a bar graph of a subset of the trials in results. Select the trials
    to include based on semantic_filter and beg_phonological filter.
    """
    selected_trials = get_trials(
        semantic_filter=semantic_filter, beg_phonological_filter=beg_phonological_filter)
    selected_results = np.array([results[trial_id] for trial_id in selected_trials])
    # normalise results
    selected_results = [np.array([float(x) for x in item]) / float(np.sum(item)) for item in selected_results]
    result = np.sum(selected_results, axis=0)
    result = result / np.sum(result)
    bar_graph(result, title=title)
    
    
def sum_squared_error(model_results, gold_standard):
    """
    model_results: np.array of shape (n_trials, n_classes) representing the output of one
        of the models
    gold_standard: np.array of shape (n_trials, n_classes) representing the trial answers
        from humans (this could be kid_answers, adult_answers, etc).
        
    Return the sum squared error of model_results relative to gold_standard. Do this by
    computing the error for each trial. For a given trial, you should first normalise the
    gold_standard results to sum to one. For example, for a particular trial, if the
    gold_standard results are [0, 0, 20, 5], it would normalise to [0, 0, 0.8, 0.2].
    Then you can compute the per-item squared error for this trial.
    
    Note: this only considers trials in gold_standard that have a sum greater than 0.
    This is important because, for some trials, we do not have the results for certain groups.
    """
    error = 0
    for curr_model_results, curr_gold_standard in zip(model_results, gold_standard):
        if np.sum(curr_gold_standard) == 0:
            continue
        gold_standard_normalised = curr_gold_standard / np.sum(curr_gold_standard)
        error += np.sum(np.square(gold_standard_normalised - curr_model_results))
    return error