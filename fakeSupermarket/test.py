from supermarket import *
from customer import *
from main import is_affordable

if __name__ == "__main__":
    sm_object = Supermarket()
    customer_1 = Customer(0.1, 1)
    customer_2 = Customer(0.9, 2)
    rc1 = is_affordable(sm_object, customer_1)
    print("Should fail: {0}".format(rc1))
    print("Should buy: {0}".format(is_affordable(sm_object, customer_2)))