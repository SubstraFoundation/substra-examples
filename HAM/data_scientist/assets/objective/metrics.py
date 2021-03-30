from sklearn.metrics import accuracy_score

import substratools as tools


class HAM10000Metrics(tools.Metrics):
    def score(self, y_true, y_pred):
        """Returns the macro-average recall

        :param y_true: actual values from test data
        :type y_true: pd.DataFrame
        :param y_true: predicted values from test data
        :type y_pred: pd.DataFrame
        :rtype: float
        """

        y_true = y_true[0].numpy()
        y_pred = y_pred[0].numpy()
        return accuracy_score(y_true, y_pred)


if __name__ == '__main__':
    tools.metrics.execute(HAM10000Metrics())