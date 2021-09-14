import random
import sys

# AR Raffle Picker program
# ------------------------
# authors: KingCobra and moomin_junkie

def create_colour_set(ticket_colour: str, last_ticket_number: int):
    ticket_numbers = set()
    for i in range(1, last_ticket_number+1):
        ticket_numbers.add((ticket_colour, i))
    return ticket_numbers


def remove_random_ticket(tickets):
    if len(tickets) > 0:
        total_number_of_tickets = len(tickets)
        index = random.randint(0, total_number_of_tickets-1)
        selected_ticket = tickets.pop(index)
        return selected_ticket
    
# user picks last ticket number sold for each colour    
last_pink_ticket_number_text = input("Enter last Pink ticket number:")
last_green_ticket_number_text = input("Enter last Green ticket number:")
last_yellow_ticket_number_text = input("Enter last Yellow ticket number:")
last_white_ticket_number_text = input("Enter last White ticket number:")
print()

# computer figures out all tickets sold and stores them in one big data collection
pink_tickets = create_colour_set('PINK', int(last_pink_ticket_number_text))
green_tickets = create_colour_set('GREEN', int(last_green_ticket_number_text))
yellow_tickets = create_colour_set('YELLOW', int(last_yellow_ticket_number_text))
white_tickets = create_colour_set('WHITE', int(last_white_ticket_number_text))

all_tickets = list(set.union(pink_tickets, green_tickets, yellow_tickets, white_tickets))

# user repeatedly picks out (winning) tickets from the big data collection 
while True:
    remaining_tickets = len(all_tickets)
    if (remaining_tickets):
        stop = input(f'Press Enter key to pick a ticket ({remaining_tickets} remaining)...')
        colour, ticket_number = remove_random_ticket(all_tickets)
        print(f'Winning ticket: {colour} {ticket_number}')
    else:
        print('No tickets left to pick from.')
        sys.exit()
