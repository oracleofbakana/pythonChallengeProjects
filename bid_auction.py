from bid_art import logo
print(logo)
bidder = {}
bidder_name = str(input("Enter the name of the bidder:\n"))
bidder_price = int(input("Enter the amount you wish to pay for the item: \n"))
bidding_finished = False

def add_bidder_info(name, price, direction):
    bidder_info = {}
    bidder_info["name"] = name
    bidder_info["price"] = price
    bidder.append(bidder_info)




