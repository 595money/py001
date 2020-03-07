from datetime import datetime


class Fund(object):
    __slots__ = ('_deposit_date', '_total_pay_ntd', '_exchange_rate', '_total_pay_usd')

    def __init__(self, deposit_date='2000-01-01', total_pay_ntd=0, exchange_rate=0, total_pay_usd=0):
        self._deposit_date = deposit_date
        self._total_pay_ntd = total_pay_ntd
        self._exchange_rate = exchange_rate
        self._total_pay_usd = total_pay_usd

    def __eq__(self, that: object) -> bool:
        if not isinstance(that, Fund):
            return False
        return self.__hash__() == that.__hash__()

    def __hash__(self) -> int:
        return int(41 * (41 + datetime.fromisoformat(
            self._deposit_date).timestamp() + self._total_pay_ntd + self._total_pay_ntd + self._total_pay_usd))

    @property
    def deposit_date(self):
        return self._deposit_date

    @deposit_date.setter
    def deposit_date(self, deposit_date):
        self._deposit_date = deposit_date

    @property
    def total_pay_ntd(self):
        return self._total_pay_ntd

    @total_pay_ntd.setter
    def total_pay_ntd(self, total_pay_ntd):
        self._total_pay_ntd = total_pay_ntd

    @property
    def exchange_rate(self):
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        self._exchange_rate = exchange_rate

    @property
    def total_pay_usd(self):
        return self._total_pay_usd

    @total_pay_usd.setter
    def total_pay_usd(self, total_pay_usd):
        self._total_pay_usd = total_pay_usd

    def convert(self, deposit_date=0, total_pay_ntd=0, exchange_rate=0, total_pay_usd=0):
        self._deposit_date = deposit_date
        self._total_pay_ntd = total_pay_ntd
        self._exchange_rate = exchange_rate
        self._total_pay_usd = total_pay_usd


def main():
    f1 = Fund('2000-02-11', 2, 3, 4)
    f2 = Fund('2000-02-11', 2, 3, 4)
    print(f1.__eq__(f2))
    print(f2.__hash__())


if __name__ == '__main__':
    main()
