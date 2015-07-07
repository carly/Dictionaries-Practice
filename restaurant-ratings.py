# your code goes here
def restaurant_ratings(filename):
    """Tells you the restaurant ratings in alphabetical order"""

    file_object = open(filename)
    restaurant_ratings = {}

    for line in file_object:
        each_line = line.rstrip().split(":")
        restaurant_name = each_line[0]
        rating = each_line[1]
        restaurant_ratings[restaurant_name] = rating

    for restaurant_name, rating in restaurant_ratings.items():
            print "%s is rated at %s" % (restaurant_name, rating)


restaurant_ratings("scores.txt")