"""
Sal's Shipping
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers.
Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping
their packages.
In this project, you’ll build a program that will take the weight of a package and determine the cheapest
way to ship that package using Sal’s Shippers.

Sal’s Shippers has several options for a customer to ship their package. They have ground shipping, which is a small
flat charge plus a rate based on the weight of your package.
Premium ground shipping, which is a much higher flat charge, but you aren’t charged for weight.
They recently also implemented drone shipping, which has no flat charge, but the rate based on weight is
triple the rate of ground shipping.

Here are the prices:

Ground Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$1.50	$20.00
Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
Over 10 lb	$4.75	$20.00

Drone Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$4.50	$0.00
Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
Over 10 lb	$14.25	$0.00

Premium Ground Shipping

Flat charge: $125.00

Write a program that asks the user for the weight of their package and then tells them which method of shipping is
cheapest and how much it will cost to ship their package using Sal’s Shippers.
"""


def ground_shipping_cost(w):
    w = float(w)
    flat_charge = 20
    g_cost = 0.0
    if w <= 2:
        g_cost = w * 1.5 + flat_charge
    elif 2 < w <= 6:
        g_cost = w * 3 + flat_charge
    elif 6 < w <= 10:
        g_cost = w * 4 + flat_charge
    elif w > 10:
        g_cost = w * 4.75 + flat_charge

    return str(g_cost)


def drone_shipping_cost(w):
    w = float(w)
    flat_charge = 0.0
    d_cost = 0.0
    if w <= 2:
        d_cost = w * 4.5 + flat_charge
    elif 2 < w <= 6:
        d_cost = w * 9 + flat_charge
    elif 6 < w <= 10:
        d_cost = w * 12 + flat_charge
    elif w > 10:
        d_cost = w * 14.25 + flat_charge

    return str(d_cost)


def premium_ground_shipping_cost():
    pg_cost = 0.0
    flat_charge = 125.0
    pg_cost = flat_charge

    return str(pg_cost)


def cheapest_shipping_cost(w):
    ground_cost = ground_shipping_cost(w)
    drone_cost = drone_shipping_cost(w)
    premium_ground_cost = premium_ground_shipping_cost()

    print("ground cost is " + ground_cost)
    print("drone cost is " + drone_cost)
    print("premium ground shipping cost is " + premium_ground_cost)

    if ground_cost > premium_ground_cost and drone_cost > premium_ground_cost:
        print("premium ground cost is cheapest")
        print("Cost of shipping is $" + str(premium_ground_cost))

    elif ground_cost == drone_cost:
        print("drone cost and ground cost are equal")
        print("Cost of shipping is $" + str(drone_cost))

    elif ground_cost < drone_cost:
        print("ground cost is cheapest")
        print("Cost of shipping is $" + str(ground_cost))
    elif ground_cost > drone_cost:
        print("drone cost is cheapest")
        print("Cost of shipping is $" + str(ground_cost))


print("Welcome to Sal's shipping")
weight = input("Enter weight of package in Pound ->  ")
cheapest_shipping_cost(weight)
