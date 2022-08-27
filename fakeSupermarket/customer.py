# organized = 0  # buy exactly 1, 10%
# bare_minimum = 1  # buy [2-4] when money is right, none when price is high, 15%
# hoarder = 2  # buy [1-3] no matter what price, 15%
# improviser = 3  # buy 1 with possibility 5%, 60%

import numpy as np
import random
import datetime
from matplotlib import pyplot as plt
import seaborn as sns
from math import ceil


class Customer:
    original_price, discount_price = 7, 4

    def __init__(self, time_percentage, type):
        self.time_percentage = time_percentage
        self.time = get_time(time_percentage)
        self.type = type
        self.is_buying = False
        if type == 0:
            self.buy_probability = 0.1
            self.buy_amount = 1
            self.ideal_price = self.original_price + 1
        elif type == 1:
            self.buy_probability = 1
            self.ideal_price = self.original_price - 1
            self.buy_amount = random.choice([2, 3, 4])
        elif type == 2:
            self.buy_probability = 1
            self.buy_amount = random.choice([1, 2, 3])
            self.ideal_price = self.original_price + 1
        elif type == 3:
            self.buy_probability = .05
            self.buy_amount = 1
            self.ideal_price = self.original_price + 1
        else:
            print("Wrong type, abort!")
            exit(1)

    def __str__(self):
        return "type: {0}, time: {1}, is_buying: {2}, ideal_price:{3},amount: {4}".format(
            self.type, self.time, self.is_buying,self.ideal_price, self.buy_amount)


def print_customers(customer_list):
    print("---------- Customers details -----------")
    type_count = [0, 0, 0, 0]
    people_buying = 0
    breads_sold = 0

    for customer in customer_list:
        type_count[customer.type] += 1
        if customer.is_buying:
            people_buying += 1
            breads_sold += customer.buy_amount

    print("--------Total Customers: {0}----------".format(len(customer_list)))
    print("Organizers: {0}, Bares: {1}, hoards: {2}, improvisers: {3}".format(
        type_count[0], type_count[1], type_count[2], type_count[3]))
    print("people buying: {0}".format(people_buying))
    print("bread sold:{0}".format(breads_sold))


def get_time(time_percentage):
    seconds = 6 * 3600 + round(18 * 3600 * time_percentage)

    return datetime.timedelta(seconds=seconds)


def create_customer(num):
    mu_time, mu_sigma, size = 75, 8.33, num
    customer_type_probability = np.array([0.1, 0.15, 0.15, 0.6])
    time_array = create_time_customers(mu_time, mu_sigma, size)
    customer_list = list()
    for i in range(size):
        customer_type = np.random.choice([0, 1, 2, 3], 1, True, customer_type_probability)
        customer = Customer(time_array[i], customer_type[0])
        customer_list.append(customer)
    return customer_list


def create_time_customers(mu, sigma, size):
    idle_size = ceil(size/100)
    time_array = np.random.normal(mu, sigma, [1, size + 2 * idle_size])
    time_array.sort()
    time_array = time_array[0, idle_size:size+idle_size]
    time_array = (time_array - np.min(time_array))/(np.max(time_array) - np.min(time_array) + 1)
    sns.displot(time_array)
    plt.show()
    return time_array


def get_customer_time(customer):
    return customer.time_percentage


if __name__ == "__main__":
    create_customer(200)