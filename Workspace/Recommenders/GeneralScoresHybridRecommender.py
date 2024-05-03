from Recommenders.BaseRecommender import BaseRecommender
import scipy.sparse as sps

class GeneralScoresHybridRecommender(BaseRecommender):
    """ ScoresHybridRecommender3
    Hybrid of tot prediction scores

    """

    RECOMMENDER_NAME = "GeneralScoresHybridRecommender"

    def __init__(self, URM_train, recommender_array):
        super(GeneralScoresHybridRecommender, self).__init__(URM_train)

        self.URM_train = URM_train
        self.recommender_array = recommender_array


    def fit(self, parameter_array):
        self.parameter_array = parameter_array

    def _compute_item_score(self, user_id_array, items_to_compute):

        # In a simple extension this could be a loop over a list of pretrained recommender objects
        item_weights_array = []

        for recommender in self.recommender_array:
            item_weights_array.append(recommender._compute_item_score(user_id_array, items_to_compute=items_to_compute))

        item_weights = 0

        for i in range(len(item_weights_array)):
            item_weights += item_weights_array[i] * self.parameter_array[i]

        return item_weights
