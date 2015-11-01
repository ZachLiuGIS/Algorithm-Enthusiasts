# This is the simple and naive solution, which does not pass all tests.
# The problem here is combination of 5 and 3 different books is more expensive.
# than a combination of two 4 different books, given the same shopping cart.


def simple_price(book_list):

    # store how much discount you get for 1, 2, 3, 4, or 5 different books (package)
    discount_dict = {
        5: .25,
        4: .2,
        3: .1,
        2: .05,
        1: 0
    }

    # get which books are in the shopping cart
    books = set(book_list)

    # get count of each books in the cart
    book_count = {}
    for book in books:
        book_count[book] = book_list.count(book)

    # take the maximum different books each time from the cart and calculate the price for selected books
    total = 0
    while len(book_count) > 0:
        max_com = len(book_count)
        total += max_com * 8 * (1 - discount_dict[max_com])

        # you can not delete a key when iterating a dict, so have to use list(dict) to loop through keys
        for key in list(book_count):
            book_count[key] -= 1
            if book_count[key] == 0:
                del book_count[key]
    return total


# This is the correct solution which passes all tests
# The implementation is similar to the first one, but goes one step further
# Instead of calculating price directly, it finds a max combination of books from the cart first and then
# store it in a cum_list list. So the list should something like [5, 5, 4, 4, 3, 2, 2, 1]
# then replace a 5 and 3 with two 4s, so make it [5, 4, 4, 4, 4, 2, 2, 1]
# After reshuffle the combinations, the correct total price can be calculated.
def price(book_list):
    discount_dict = {
        5: .25,
        4: .2,
        3: .1,
        2: .05,
        1: 0
    }

    books = set(book_list)
    book_count = {}
    for book in books:
        book_count[book] = book_list.count(book)

    cum_list = []

    while len(book_count) > 0:
        max_com = len(book_count)
        cum_list.append(max_com)

        for key in list(book_count):
            book_count[key] -= 1
            if book_count[key] == 0:
                del book_count[key]

    while 5 in cum_list and 3 in cum_list:
        cum_list[cum_list.index(5)] = 4
        cum_list[cum_list.index(3)] = 4

    total = 0
    for num in cum_list:
        total += 8 * num * (1 - discount_dict[num])
    return total


def main():
    books = [0, 0, 1, 1, 2, 2, 3, 4]
    total = price(books)
    print(total)


if __name__ == "__main__":
    main()
