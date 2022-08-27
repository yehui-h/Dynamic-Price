from datetime import timedelta


class Supermarket:
    original_price = 7
    discount_price = 4
    discount_time = timedelta(hours=22)

    def __init__(self):
        self.stock = 1000

    def sale(self, num) -> int:
        if num > self.stock:
            self.stock = 0
            return self.stock

        self.stock -= num
        return num

    def is_left(self) -> bool:
        return self.stock >= 0

    def __str__(self):
        return "supermarket stock: {0}".format(self.stock)
