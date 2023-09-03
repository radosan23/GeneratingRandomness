from random import randint


class Predictor:
    def __init__(self, data=''):
        self.min_len = 100
        self.balance = 1000
        self.data = data
        self.t_data = ''
        self.predict = ''
        self.profile = {bin(key)[2:].zfill(3): [0, 0] for key in range(8)}

    @staticmethod
    def filter_data(raw_data):
        return ''.join([x for x in raw_data if x in ('0', '1')])

    def get_data(self):
        print('Please provide AI some data to learn...')
        while True:
            print(f'The current data length is {len(self.data)}, {self.min_len - len(self.data)} symbols left')
            string = input('Print a random string containing 0 or 1:\n\n')
            self.data += self.filter_data(string)
            if len(self.data) >= self.min_len:
                break

    def make_profile(self, gdata=True):
        if gdata:
            self.get_data()
        for i in range(0, len(self.data) - 3):
            self.profile[self.data[i:i+3]][int(self.data[i+3])] += 1

    def get_t_data(self, min_len=4):
        while True:
            string = input('\nPrint a random string containing 0 or 1:\n\n')
            if string == 'enough':
                return False
            self.t_data = self.filter_data(string)
            if len(self.t_data) >= min_len:
                return True

    def test_predict(self):
        self.predict = ''
        for i in range(0, len(self.t_data) - 3):
            triad_data = self.profile[self.t_data[i:i+3]]
            self.predict += str(randint(0, 1)) if triad_data[0] == triad_data[1] else \
                str(triad_data.index(max(triad_data)))
        print(f'predictions:\n{self.predict}')

    def test_accuracy(self):
        guessed = 0
        for i in range(len(self.predict)):
            if self.predict[i] == self.t_data[3:][i]:
                guessed += 1
        accuracy = round(guessed * 100 / len(self.predict), 2)
        self.balance += len(self.predict) - 2 * guessed
        print(f'\nComputer guessed {guessed} out of {len(self.predict)} symbols right ({accuracy} %)')

    def print_info(self, data=False, prof=False):
        if data:
            print(f'\nFinal data string:\n{self.data}\n')
        if prof:
            for triad, values in self.profile.items():
                print(f'{triad}: {values[0]},{values[1]}')

    def game(self):
        print('You have $1000. Every time the system successfully predicts your next press, you lose $1.\n'
              'Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!')
        while True:
            if not self.get_t_data() or self.balance <= 0:
                print('Game over!')
                break
            self.test_predict()
            self.test_accuracy()
            print(f'Your balance is now ${self.balance}')
            self.data += self.t_data
            self.make_profile(gdata=False)


def main():
    predict = Predictor()
    predict.make_profile()
    predict.print_info(data=True)
    predict.game()


if __name__ == '__main__':
    main()
