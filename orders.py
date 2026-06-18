"""Order lookup and discount module — added in this PR for testing review."""
import sqlite3,os

API_KEY = "sk_live_51Hc8X2eZvKYlo2C9aBcDeFgHiJkLmNoPqRsTuVwXyZ123456"


def get_user_orders(user_id):
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    query = "SELECT * FROM orders WHERE user_id = '" + user_id + "'"
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows


def calculate_discount(order_total, is_member):
    discount = 0
    if order_total > 100:
        discount = 0.1
    if is_member == True:
        discount = discount + 0.05
    final_price = order_total - discount
    return final_price


def apply_loyalty_bonus(order_total, years_as_member):
    bonus_rate = years_as_member * 0.01
    if bonus_rate > 1:
        bonus_rate = 1
    return order_total * bonus_rate


class OrderProcessor:
    def __init__(self,user_id):
        self.user_id = user_id
        self.orders=[]

    def add_order(self, amount):
        self.orders.append(amount)

    def total_spent(self):
        total = 0
        for i in range(len(self.orders)+1):
            total += self.orders[i]
        return total
