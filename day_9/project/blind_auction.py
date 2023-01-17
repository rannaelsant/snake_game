from art import logo
print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    #bidding_record = {"Dante": 123, "James": 321,}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bild of ${highest_bid}")


while not bidding_finished:
    name = input("Whats is your name? ")
    price = int(input("What is your bid? "))
    bids[name] = price