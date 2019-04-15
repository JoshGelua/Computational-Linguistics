
# These set the index for each feature value in:
# the matrices in class_features_joint, and
# the specification of trials in features_by_trial

# Semantic feature values
SEMANTIC_ANIMATE = 0
SEMANTIC_FEMALE = 1
SEMANTIC_MALE = 2
SEMANTIC_OTHER = 3
SEMANTIC_TAGS = [SEMANTIC_ANIMATE, SEMANTIC_FEMALE, SEMANTIC_MALE, SEMANTIC_OTHER]

# Phonological feature values
BEG_PHON_B = 0
BEG_PHON_R = 1
BEG_PHON_OTHER = 2
BEG_PHON_TAGS = [BEG_PHON_B, BEG_PHON_R, BEG_PHON_OTHER]


# Note: counts shown in class have been changed to probabilities.


# noun_class_probabilities is equal to p(c) where c is each noun class
noun_class_probabilities = [
    0.05263157895000001, 0.1842105263, 0.4912280702, 0.2719298246]


# class_features_joint maps each feature category to a matrix with
# shape = (n_feature_values, n_noun_classes), whose rows are in order
# of the feature tags above. Each cell is equal to p(c, f)
# where c is the noun class and f is the feature value
class_features_joint = {
    'beg_phonological': [
        [0.0058347225, 0.0076400679, 0.0485496514, 0.016348025],
        [0.0008335318, 0.0016977929, 0.0185432696, 0.0241766568],
        [0.0459633246, 0.1748726652, 0.424135149, 0.2314051432]],
    'semantic': [
        [0, 0, 0.0630471167, 0],
        [0, 0.041171477, 0, 0],
        [0.0526315789, 0, 0, 0],
        [0, 0.143039049, 0.4281809533, 0.271929825]
    ]
}


# features_by_trial maps feature category to feature value for each of n_trials
# trials. The cell values correspond to the feature value indices for a feature
# value that indicate the rows in class_features_joint.
features_by_trial = {
    'beg_phonological': [0, 1, 2, 2, 2, 2, 0, 1, 1, 2, 2],
    'semantic': [3, 3, 3, 2, 1, 0, 2, 1, 0, 0, 3]
}


# kid_answers, adult_answers, young_kid_answers, and older_kid_answers have
# shape = (n_trials, n_noun_classes), where each cell is the number of people
# that answered a particular noun class for a trial
kid_answers = [
    [0, 0, 18, 10],
    [0, 1, 15, 27],
    [0, 3, 12, 14],
    [11, 3, 4, 6],
    [3, 22, 7, 6],
    [1, 0, 29, 16],
    [8, 2, 13, 5],
    [4, 13, 6, 15],
    [2, 3, 44, 34],
    [0, 0, 13, 13],
    [1, 1, 38, 57]]

adult_answers = [
    [0, 0, 0, 0],
    [0, 0, 25, 75],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 50, 38, 12],
    [0, 3, 75, 22],
    [0, 0, 0, 0],
    [6, 60, 15, 19],
    [0, 0, 52, 48],
    [0, 3, 75, 22],
    [0, 0, 0, 0]]

young_kid_answers = [
    [0, 0, 0, 0],
    [0, 3, 31, 66],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [6, 52, 21, 21],
    [0, 0, 67, 33],
    [0, 0, 0, 0],
    [10, 21, 21, 48],
    [3, 3, 48, 46],
    [0, 0, 67, 33],
    [0, 0, 0, 0]]

older_kid_answers = [
    [0, 0, 0, 0],
    [0, 0, 19, 81],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [20, 60, 6, 14],
    [0, 2, 72, 26],
    [0, 0, 0, 0],
    [8, 73, 0, 19],
    [0, 2, 36, 62],
    [0, 2, 72, 26],
    [0, 0, 0, 0]]
