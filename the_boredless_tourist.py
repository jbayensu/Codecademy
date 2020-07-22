destinations = ['Paris, France', 'Shangai, China',
                'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination):

    # for i in range(len(destinations)):
    #   if destinations[i] == destination:
    #      return i

    # return "Destination not found"
    return destinations.index(destination)


print(get_destination_index("Los Angeles, USA"))
print(get_destination_index("Paris, France"))
print(get_destination_index("Hyderabad, India"))
