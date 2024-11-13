from auction_art import gavel
from replit import clear
auction_book = {}

print(gavel)
print("Welcom to the secret auction program.")


status = "yes"
while status == "yes":
    name_input = input("What is your name? ")
    bid_input = int(input("Whats your bid? $"))
    auction_book[name_input] = bid_input
    status = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    clear()

auction_book_sorted = sorted(auction_book.items(), key=lambda x:x[1], reverse=True)
print(f"The winner is {auction_book_sorted[0][0]} with a bid of ${auction_book_sorted[0][1]}.")
