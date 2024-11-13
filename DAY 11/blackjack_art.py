
def cards_art(symbol, num, current_cards = '''


'''):
    if (num == "10"):
        new_card = f''' ___ 
|{num} |
| {symbol} |
|_{num}|'''
    else:
        new_card = f''' ___ 
|{num}  |
| {symbol} |
|__{num}|'''
    return '\n'.join(map(' '.join, zip(*map(str.split, (current_cards, new_card), ('\n', '\n')))))

title = ''' _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/                 '''