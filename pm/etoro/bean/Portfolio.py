from datetime import datetime


class Portfolio(object):
    __slots__ = ('_ticker_symbol', '_open_date', '_close_date', '_open', '_close', '_units')

    def __init__(self, ticker_symbol='AAA', open_date='2000-01-01', close_date='2000-01-01', open=0, close=0, units=0):
        self._ticker_symbol = ticker_symbol
        self._open_date = open_date
        self._close_date = close_date
        self._open = open
        self._close = close
        self._units = units

    def __eq__(self, that: object) -> bool:
        if not isinstance(that, Portfolio):
            return False
        return self.__hash__() == that.__hash__()

    def __hash__(self) -> int:
        return int(41 * (41 + datetime.fromisoformat(self._close_date).timestamp()
                         + datetime.fromisoformat(self._open_date).timestamp()
                         + self._open
                         + self._close
                         + self._units))

    @property
    def ticker_symbol(self):
        return self._ticker_symbol

    @ticker_symbol.setter
    def ticker_symbol(self, ticker_symbol):
        self._ticker_symbol = ticker_symbol

    @property
    def open_date(self):
        return self._open_date

    @open_date.setter
    def open_date(self, open_date):
        self._open_date = open_date

    @property
    def close_date(self):
        return self._close_date

    @close_date.setter
    def close_date(self, close_date):
        self._close_date = close_date

    @property
    def open(self):
        return self._open

    @open.setter
    def open(self, open):
        self._open = open

    @property
    def close(self):
        return self._close

    @close.setter
    def close(self, close):
        self._close = close

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, units):
        self._units = units

    def convert(self, ticker_symbol=0, open_date=0, close_date=0, open=0, close=0, units=0):
        self._ticker_symbol = ticker_symbol
        self._open_date = open_date
        self._close_date = close_date
        self._open = open
        self._close = close
        self._units = units


def main():
    f1 = Portfolio(ticker_symbol='ZZZ', open_date='2000-01-01', close_date='2000-01-01', open=1, close=2, units=0)
    f2 = Portfolio(ticker_symbol='ZZZ', open_date='2000-01-01', close_date='2000-01-01', open=1, close=2, units=0)
    print(f1.__hash__())
    print(f2.__hash__())
    print(f1.__eq__(f2))


if __name__ == '__main__':
    main()
