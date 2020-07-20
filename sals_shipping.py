def cost_of_ground_shipping(weight):
    cost = 20
    if(weight <= 2):
        cost += (weight * 1.50)
    elif((weight > 2) and weight <= 6):
        cost += (weight * 3.00)
    elif((weight > 6 and weight <= 10)):
        cost += (weight * 4.00)
    else:
        cost += weight * 4.75
    return cost


def cost_of_drone_shipping(weight):
    cost = 0
    if(weight <= 2):
        cost += (weight * 4.50)
    elif((weight > 2) and weight <= 6):
        cost += (weight * 9.00)
    elif((weight > 6 and weight <= 10)):
        cost += (weight * 12.00)
    else:
        cost += weight * 14.75
    return cost


def cheapest_shipping_method(weight):
    ground_shipping = cost_of_ground_shipping(weight)
    drone_shipping = cost_of_drone_shipping(weight)
    cost_of_premium_ground_shipping = 125.00

    if(ground_shipping < drone_shipping and ground_shipping < cost_of_premium_ground_shipping):
        print("Ground shipping is the cheapest and it costs: $ " +
              str(ground_shipping))
    elif(drone_shipping < ground_shipping and drone_shipping < cost_of_premium_ground_shipping):
        print("Drone shipping is the cheapest and it cost: $" + str(drone_shipping))
    else:
        print("Premium ground shipping is the cheapest and it cost: $125")


print("$" + str(cost_of_ground_shipping(8.4)))

print("$" + str(cost_of_drone_shipping(1.5)))

cheapest_shipping_method(4.8)
cheapest_shipping_method(41.5)
