class Randomness:
    def __init__(self, data=''):
        self.min_len = 100
        self.data = data

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
        print(f'\nFinal data string:\n{self.data}')


def main():
    rand = Randomness()
    rand.get_data()


if __name__ == '__main__':
    main()
