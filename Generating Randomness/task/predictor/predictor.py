from random import randint


class Predictor:
    def __init__(self, data=''):
        self.min_len = 100
        self.data = data
        self.t_data = ''
        self.predict = ''
        self.profile = {bin(key)[2:].zfill(3): [0, 0] for key in range(8)}

    @staticmethod
    def filter_data(raw_data):
        return ''.join([x for x in raw_data if x in ('0', '1')])

    def get_data(self):
        while True:
            string = input('Print a random string containing 0 or 1:\n\n')
            self.data += self.filter_data(string)
            if len(self.data) >= self.min_len:
                break
            print(f'Current data length is {len(self.data)}, {self.min_len - len(self.data)} symbols left')

    def make_profile(self):
        self.get_data()
        for i in range(0, len(self.data) - 3):
            self.profile[self.data[i:i+3]][int(self.data[i+3])] += 1

    def get_t_data(self, min_len=4):
        while True:
            string = input('\nPlease enter a test string containing 0 or 1:\n\n')
            self.t_data = self.filter_data(string)
            if len(self.t_data) >= min_len:
                break

    def test_predict(self):
        for i in range(0, len(self.t_data) - 3):
            triad_data = self.profile[self.t_data[i:i+3]]
            self.predict += randint(0, 1) if triad_data[0] == triad_data[1] else str(triad_data.index(max(triad_data)))
        print(f'predictions:\n{self.predict}')

    def test_accuracy(self):
        self.get_t_data()
        self.test_predict()
        guessed = 0
        for i in range(len(self.predict)):
            if self.predict[i] == self.t_data[3:][i]:
                guessed += 1
        accuracy = round(guessed * 100 / len(self.predict), 2)
        print(f'\nComputer guessed {guessed} out of {len(self.predict)} symbols right ({accuracy} %)')

    def print_info(self, prof=False):
        print(f'\nFinal data string:\n{self.data}\n')
        if prof:
            for triad, values in self.profile.items():
                print(f'{triad}: {values[0]},{values[1]}')


def main():
    predict = Predictor()
    predict.make_profile()
    predict.print_info()
    predict.test_accuracy()


if __name__ == '__main__':
    main()
