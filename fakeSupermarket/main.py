# organized = 0  # buy exactly 1, 10%
# bare_minimum = 1  # buy [1-3] when money is right, none when price is high, 15%
# hoarder = 2  # buy [1-3] no matter what price, 15%
# improviser = 3  # buy 1 with possibility 5%, 60%
import datetime

from customer import create_customer, get_customer_time, Customer, print_customers
from supermarket import Supermarket
import random
import csv


def get_customer_type_str(customer: Customer):
    customer_type = customer.type
    if customer_type == 0:
        return "organized"
    elif customer_type == 1:
        return "bare_minimum"
    elif customer_type == 2:
        return "hoarder"
    elif customer_type == 3:
        return "improviser"
    else:
        return "Unknown"


def get_bought_amount(customer: Customer):
    if customer.is_buying:
        return customer.buy_amount
    else:
        return 0


def get_bought_price(customer: Customer):
    if not customer.is_buying:
        return 0
    elif customer.time > datetime.timedelta(hours=22):
        return 4
    else:
        return 7


def is_affordable(market: Supermarket, single_customer: Customer):
    price = market.original_price
    if single_customer.time > market.discount_time:
        price = market.discount_price
    return single_customer.ideal_price > price


def buy(market, single_customer):
    if market.is_left():
        buy_amount = market.sale(single_customer.buy_amount)
        single_customer.buy_amount = buy_amount
        single_customer.is_buying = True
        return True
    else:
        print("Transaction failed")
        print(market)
        print(single_customer)
        return False


def build_dataset(num):
    for i in range(num):
        print("-------- Build dataset{0} --------".format(i))
        customer_list = create_customer(2000)
        supermarket_instance = Supermarket()
        for customer in customer_list:
            if customer.type == 3:
                is_buy = random.choices([True, False], weights=(.05, .95), k=1)
                if is_buy[0]:
                    buy(supermarket_instance, customer)
            elif customer.type == 0:
                buy(supermarket_instance, customer)
            else:
                if is_affordable(supermarket_instance, customer):
                    buy(supermarket_instance, customer)
        print_customers(customer_list)
        print(supermarket_instance)
        filename = "dataset/data{0}.csv".format(i)
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["index", "sales_time", "each_bread_price",
                             "customer_type", "amount",
                             "production_date", "expired_date"])
            for j in range(len(customer_list)):
                customer = customer_list[j]
                writer.writerow([j, customer.time,
                                 get_bought_price(customer),
                                 get_customer_type_str(customer),
                                 get_bought_amount(customer),
                                 datetime.timedelta(hours=6),
                                 datetime.timedelta(hours=23, minutes=59, seconds=59)])


if __name__ == '__main__':
    build_dataset(20)
