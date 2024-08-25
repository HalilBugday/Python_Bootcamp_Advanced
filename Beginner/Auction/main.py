from art import logo

def find_highest_bidder(bidding_dic):
    winner = ""
    highest_bid = 0
    #max(bidding_dic)
    for bidder in bidding_dic:
        bid_amount = bidding_dic[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}!")


bids = {} #dictionary -> {name: price}
cont_bidding = True
while cont_bidding:
    print(logo)
    name = input("What is your name?: ")
    prince = int(input("What is your bid?: $"))
    bids[name] = prince #dictionary append
    should_cont = input("Are there any other bidders? Type 'yes' or 'no'.\n " ).lower()
    if should_cont == "no":
        cont_bidding = False
        find_highest_bidder(bids)
    elif should_cont == "yes":
        print("\n" * 5)
