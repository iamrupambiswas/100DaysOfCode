#Auction System to Determine the Highest Bidder

def find_highest_bidder(bidders_dict):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bidders_dict:
        bid_amount = bidders_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder
    print(f"{highest_bidder} is the highest bidder with {highest_bid} bids!")


continue_bidding = 'yes'
bids = {}
while continue_bidding == 'yes':
    name = input("What is your name: ")
    bid = int(input("What is your bid: "))
    bids[name] = bid
    continue_bidding = input("Are there other bidders? type 'yes' or 'no' :   ").lower()
    if continue_bidding == 'no':
        print("\n" * 100)
        find_highest_bidder(bids)
    elif continue_bidding == 'yes':
        print("\n" * 100)
        