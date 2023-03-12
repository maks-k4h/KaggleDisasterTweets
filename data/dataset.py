import torch.utils.data as data
import pandas as pd


class DisasterData(data.Dataset):
    def __init__(self, split='all', train_fraction=.9, path=''):
        """

        :param split:
            all — load all labeled data
            train — load train split
            valid — load validation split
            test — load test data
        :return:
        """

        self._split = split.strip().lower()

        if split == 'all':
            self._data = pd.read_csv(path + 'train.csv')
        elif split == 'train':
            data = pd.read_csv(path + 'train.csv')
            N = int(data.shape[0] * train_fraction)
            self._data = data[:N]
        elif split == 'valid':
            data = pd.read_csv(path + 'train.csv')
            N = int(data.shape[0] * train_fraction)
            self._data = data[N:]
        elif split == 'test':
            self._data = pd.read_csv(path + 'test.csv')
        else:
            raise Exception("Unknown data split requested")

    def __len__(self):
        return self._data.shape[0]

    def __getitem__(self, item):
        """

        :param item:
        :return: (id, text, location, keyword)
        """
        entry = self._data.iloc[item]
        return (entry.id, entry.text, entry.location, entry.keyword), entry.get('target')
