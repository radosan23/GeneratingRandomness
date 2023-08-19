class Predictor:
    def __init__(self, data=''):
        self.min_len = 100
        self.data = data
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
        for i in range(0, len(self.data) - 3):
            self.profile[self.data[i:i+3]][int(self.data[i+3])] += 1

    def print_info(self):
        print(f'\nFinal data string:\n{self.data}\n')
        for triad, values in self.profile.items():
            print(f'{triad}: {values[0]},{values[1]}')


def main():
    predict = Predictor()
    predict.get_data()
    predict.make_profile()
    predict.print_info()


if __name__ == '__main__':
    main()
