print("Welcome to LITTLECART")


# ====================================================================================================================================================

import random

num4 = random.randrange(0, 50)
num3 = random.randrange(0, 50)
num2 = random.randrange(0, 50)
num1 = random.randrange(0, 50)
num_ = random.randrange(1, 9999)

coupon = f"DIWALI{num_}"  # ye coupon previous,  real order ke pamplate me rahega !


inventory = {
    "shirt": {
        "types": {
            "red shirt": {"prize": 1500, "stock": num4},
            "white shirt": {"prize": 1500, "stock": num3},
            "blue shirt": {"prize": 1500, "stock": num2},
            "yellow shirt": {"prize": 1500, "stock": num1},
        }
    },
    "jeans": {
        "types": {
            "black jeans": {"prize": 2000, "stock": num1},
            "blue jeans": {"prize": 2000, "stock": num2},
            "brown jeans": {"prize": 2000, "stock": num3},
            "white jeans": {"prize": 2000, "stock": num4},
        }
    },
    "shoes": {
        "types": {
            "nike": {"prize": 2500, "stock": num2},
            "redtape": {"prize": 2300, "stock": num4},
            "bluetape": {"prize": 2100, "stock": num3},
            "blacktape": {"prize": 2000, "stock": num1},
        }
    },
    "watches": {
        "types": {
            "patek": {"prize": 200000000, "stock": num2},
            "jacob&co": {"prize": 20000000, "stock": num3},
            "rolex": {"prize": 30000000, "stock": num4},
        }
    },
}


# ====================================================================================================================================================


def shirt_menu():
    print(20 * "~")
    print(
        f"Shirts Types\n{22 * '-'}\n[1] red shirt - ₹1500 , stock - {num4}\n[2] white shirt - ₹1500 , stock - {num3}\n[3] blue shirt - ₹1500 , stock - {num2}\n[4] yellow shirt - ₹1500 , stock - {num1}"
    )
    print(20 * "~")


def jeans_menu():
    print(20 * "~")
    print(
        f"Jeans Types\n{22 * '-'}\n[1] black jeans - ₹2000 , stock - {num1}\n[2] white jeans - ₹2000 , stock - {num4}\n[3] blue jeans - ₹2000 , stock - {num2}\n[4] brown jeans - ₹2000 , stock - {num3}"
    )
    print(20 * "~")


def shoes_menu():
    print(20 * "~")
    print(
        f"Shoes Types\n{22 * '-'}\n[1] nike - ₹2500, stock - {num2}\n[2] redtape - ₹2300 , stock - {num4}\n[3] bluetape - ₹2100 , stock - {num3}\n[4] blacktape - ₹2000 , stock - {num1}"
    )
    print(20 * "~")


def watch_menu():
    print(20 * "~")
    print(
        f"Watch Types\n{22 * '-'}\n[1] patek - ₹200000000 , stock - {num2}\n[2] jacob&co - ₹20000000 , stock - {num3}\n[3] rolex - ₹30000000 , stock - {num4}"
    )
    print(20 * "~")


def main_menu():
    print(20 * "~")
    print(
        f"Product Available\n{29 * '-'}\n[1] Shirts\n[2] Jeans\n[3] Shoes\n[4] Watches\n[5] Exit\n[6] Basket"
    )
    print(20 * "~")


bill = []
cart = []
stock_list = []


# ========================================================================================================================================================================


print(coupon)


def order_cart():
    while True:
        try:
            main_menu()
            x = input("Select option  :  ")

            # -------------------------------------------------------------------------------------------------

            if x == "shirt" or x == "1":
                shirt_menu()

                shirt_input = input("Enter ur shirt :  ")
                stock_shirt = int(
                    inventory["shirt"]["types"][shirt_input.lower()]["stock"]
                )
                prize_shirt = int(
                    inventory["shirt"]["types"][shirt_input.lower()]["prize"]
                )
                qty1 = int(input("Enter quantity : "))

                if stock_shirt >= 1 and qty1 <= stock_shirt:
                    cart.append(shirt_input)
                    for e in range(1, qty1 + 1):
                        stock_list.append(1)
                    for z in range(1, qty1 + 1):
                        bill.append(prize_shirt)

                    print("Order placed ✓ check Basket !")
                elif stock_shirt == 0:
                    print("Out of stock ! ")
                else:
                    print("Plz Enter valid quantity")

            # -------------------------------------------------------------------------------------------------

            elif x == "jeans" or x == "2":
                jeans_menu()

                jeans_input = input("Enter ur jeans : ")
                stock_jeans = int(
                    inventory["jeans"]["types"][jeans_input.lower()]["stock"]
                )
                prize_jeans = int(
                    inventory["jeans"]["types"][jeans_input.lower()]["prize"]
                )
                qty2 = int(input("Enter quantity : "))

                if stock_jeans >= 1 and qty2 <= stock_jeans:
                    cart.append(jeans_input)
                    for l in range(1, qty2 + 1):
                        stock_list.append(1)
                    for a in range(1, qty2 + 1):
                        bill.append(prize_jeans)
                    print("Order placed ✓ check Basket !")
                elif stock_jeans == 0:
                    print("Out of stock ! ")
                else:
                    print("Plz Enter valid quantity")

            # -------------------------------------------------------------------------------------------------

            elif x == "shoes" or x == "3":
                shoes_menu()

                shoes_input = input("Enter ur shoes : ")
                stock_shoes = int(
                    inventory["shoes"]["types"][shoes_input.lower()]["stock"]
                )
                prize_shoes = int(
                    inventory["shoes"]["types"][shoes_input.lower()]["prize"]
                )
                qty3 = int(input("Enter quantity : "))

                if stock_shoes >= 1 and qty3 <= stock_shoes:
                    cart.append(shoes_input)
                    for b in range(1, qty3 + 1):
                        stock_list.append(1)
                    for c in range(1, qty3 + 1):
                        bill.append(prize_shoes)
                    print("Order placed ✓ check Basket !")
                elif stock_shoes == 0:
                    print("Out of stock ! ")
                else:
                    print("Plz Enter valid quantity")

            # -------------------------------------------------------------------------------------------------

            elif x == "watches" or x == "4":
                watch_menu()

                watch_input = input("Enter ur watch : ")
                stock_watch = inventory["watches"]["types"][watch_input.lower()][
                    "stock"
                ]
                prize_watch = int(
                    inventory["watches"]["types"][watch_input.lower()]["prize"]
                )
                qty4 = int(input("Enter quantity : "))

                if stock_watch >= 1 and qty4 <= stock_watch:
                    cart.append(watch_input)
                    for d in range(1, qty4 + 1):
                        stock_list.append(1)
                    for f in range(1, qty4 + 1):
                        bill.append(prize_watch)
                    print("Order placed ✓ check Basket !")

                elif stock_watch == 0:
                    print("Out of stock ! ")
                else:
                    print("Plz Enter valid quantity")

            # -------------------------------------------------------------------------------------------------

            elif x == "exit":
                break

            # -------------------------------------------------------------------------------------------------

            elif x == "basket":

                def show_order():
                    m = 0

                    for j in cart:
                        print(f" Product : {j}")
                    for k in stock_list:
                        k += 1
                    print(f" Quantity {k} : {k}")
                    for i in bill:
                        m += i

                    accept_coupon = input(" Enter your coupon If you have :  ")

                    discount = (20 / 100) * m

                    if accept_coupon == coupon:
                        final_bill = m - discount
                        print(f" Bill : {final_bill}")
                        return final_bill, accept_coupon, discount

                    else:
                        print(f"Bill : {m}")
                        return m, accept_coupon, discount

                store1, store2, discount1 = show_order()

                # -------------------------------------------------------------------------------------------------

                can_order = input("Want to cancel order ? [yes/no]:  ")
                print(store2)

                if can_order == "yes":
                    print(cart)
                    print(bill)
                    print(stock_list)

                    cancel_order_input = input("Enter product name :  ")
                    can_or_type = input("Enter product's type name :  ")
                    qty = int(input("Enter quantity : "))
                    cancel_order_price = int(
                        inventory[cancel_order_input.lower()]["types"][
                            can_or_type.lower()
                        ]["prize"]
                    )

                    # cart.remove(can_or_type)
                    for g in range(1, qty + 1):
                        stock_list.remove(1)
                    for h in range(0, qty):
                        bill.remove(cancel_order_price)

                    m = 0

                    for j in cart:
                        print(f" Product : {j}")
                    for k in stock_list:
                        k += 1
                    print(f" Quantity {j} : {k}")
                    for i in bill:
                        m += i

                    if store2 == coupon:
                        final_bill = m - discount1
                        print(f" Bill : {final_bill}")

                    else:
                        print(f"Bill : {m}")

                    print("Have a great day !!")

                elif can_order == "no":
                    print(" Ok ! Have a great day")
                    break
                else:
                    print(" Plz Enter correct Option !")

            else:
                print("Enter valid Product ! ")
        except KeyError:
            print("Enter valid Input !! ")
        except:
            print("Hey user something went wrong !!")


order_cart()


# ====================================================================================================================================================
