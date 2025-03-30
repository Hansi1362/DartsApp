import re
from gtts import gTTS
from tkinter import messagebox
import two_player, one_player, gui

#Fonts für alle Seiten
font = 'Bahnschrift', 70
font2 = 'Bahnschrift', 30
font3 = 'Bahnschrift', 10
background = 'lightgrey'

font_two = 'Bahnschrift', 50
font2_two = 'Bahnschrift', 30
font3_two = 'Bahnschrift', 10

game_start = []

next_player = 0

dart_checkouts = {
    170: ["T20, T20, D25"],
    167: ["T20, T19, D25"],
    164: ["T20, T18, D25"],
    161: ["T20, T17, D25"],
    160: ["T20, T20, D20"],
    158: ["T20, T20, D19"],
    157: ["T20, T19, D20"],
    156: ["T20, T20, D18"],
    155: ["T20, T19, D19"],
    154: ["T20, T18, D20"],
    153: ["T20, T19, D18"],
    152: ["T20, T20, D16"],
    151: ["T20, T17, D20"],
    150: ["T20, T18, D18"],
    149: ["T20, T19, D16"],
    148: ["T20, T16, D20"],
    147: ["T20, T17, D18"],
    146: ["T20, T18, D16"],
    145: ["T20, T15, D20"],
    144: ["T20, T20, D12"],
    143: ["T20, T17, D16"],
    142: ["T20, T14, D20"],
    141: ["T20, T19, D12"],
    140: ["T20, T20, D10"],
    139: ["T20, T13, D20"],
    138: ["T20, T18, D12"],
    137: ["T20, T19, D10"],
    136: ["T20, T20, D8"],
    135: ["T20, T13, D18"],
    134: ["T20, T14, D16"],
    133: ["T20, T19, D8"],
    132: ["T20, T16, D12"],
    131: ["T20, T13, D16"],
    130: ["T20, T20, D5"],
    129: ["T19, T16, D12"],
    128: ["T18, T14, D16"],
    127: ["T20, T17, D8"],
    126: ["T19, T19, D6"],
    125: ["25, T20, D20"],
    124: ["T20, T14, D11"],
    123: ["T19, T16, D9"],
    122: ["T18, T18, D7"],
    121: ["T20, T11, D14"],
    120: ["T20, 20, D20"],
    119: ["T19, T10, D16"],
    118: ["T20, 18, D20"],
    117: ["T20, 17, D20"],
    116: ["T20, 16, D20"],
    115: ["T20, 15, D20"],
    114: ["T20, 14, D20"],
    113: ["T20, 13, D20"],
    112: ["T20, 12, D20"],
    111: ["T20, 11, D20"],
    110: ["T20, 10, D20"],
    109: ["T20, 9, D20"],
    108: ["T20, 8, D20"],
    107: ["T19, 10, D20"],
    106: ["T20, 6, D20"],
    105: ["T19, 8, D20"],
    104: ["T18, 10, D20"],
    103: ["T17, 12, D20"],
    102: ["T20, 2, D20"],
    101: ["T17, 10, D20"],
    100: ["T20, D20"],
    99: ["T19, 10, D16"],
    98: ["T20, D19"],
    97: ["T19, D20"],
    96: ["T20, D18"],
    95: ["T19, D19"],
    94: ["T18, D20"],
    93: ["T19, D18"],
    92: ["T20, D16"],
    91: ["T17, D20"],
    90: ["T18, D18"],
    89: ["T19, D16"],
    88: ["T16, D20"],
    87: ["T17, D18"],
    86: ["T18, D16"],
    85: ["T15, D20"],
    84: ["T20, D12"],
    83: ["T17, D16"],
    82: ["T14, D20"],
    81: ["T19, D12"],
    80: ["T20, D10"],
    79: ["T19, D11"],
    78: ["T18, D12"],
    77: ["T15, D16"],
    76: ["T20, D8"],
    75: ["T17, D12"],
    74: ["T14, D16"],
    73: ["T19, D8"],
    72: ["T16, D12"],
    71: ["T13, D16"],
    70: ["T18, D8"],
    69: ["T19, D6"],
    68: ["T20, D4"],
    67: ["T17, D8"],
    66: ["T10, D18"],
    65: ["T19, D4"],
    64: ["T16, D8"],
    63: ["T13, D12"],
    62: ["T10, D16"],
    61: ["T15, D8"],
    60: ["20, D20"],
    59: ["19, D20"],
    58: ["18, D20"],
    57: ["17, D20"],
    56: ["16, D20"],
    55: ["15, D20"],
    54: ["14, D20"],
    53: ["13, D20"],
    52: ["12, D20"],
    51: ["19, D16"],
    50: ["10, D20"],
    49: ["9, D20"],
    48: ["16, D16"],
    47: ["7, D20"],
    46: ["6, D20"],
    45: ["13, D16"],
    44: ["4, D20"],
    43: ["3, D20"],
    42: ["10, D16"],
    41: ["9, D16"],
    40: ["D20"],
    }


def split_darts_input(s):
    match = re.match(r"([dtDT])?(\d+)", s) 
    if match:
        letter = match.group(1) 
        number = int(match.group(2))
        
        if letter:
            letter = letter.lower()  
            if letter == "d":
                number *= 2
            elif letter == "t":
                number *= 3
        
        return number  

    return 0
    
last_points_p1 = []
last_points_p2 = []

last_avg_p1 = []
last_avg_p2 = []

def calc(n1, n2, n3, points, p):
    t1 = split_darts_input(n1)
    t2 = split_darts_input(n2)
    t3 = split_darts_input(n3)

    throw = t1 + t2 + t3
    if p == 1:
        last_points_p1.append(throw)
    else:
        last_points_p2.append(throw)

    p = t1 + t2 + t3
    max = points - p

    if max < 0 or max == 1 or p == 0:
        return points, False, 'No Score'
    elif max == 0:
        return max, True, ''
    else:
        return max, False, p

def get_average(p):
    if p == 1:
        avg = sum(last_points_p1)/len(last_points_p1)
        throws = len(last_points_p1)
        last_avg_p1.append(avg)
    else:
        avg = sum(last_points_p2)/len(last_points_p2)
        throws = len(last_points_p2)
        last_avg_p2.append(avg)
    return round(avg), throws * 3
    
def reset(points, p):
    if p == 1:
        last_points = points + last_points_p1[-1]
        last_points_p1.pop()
        last_avg = last_avg_p1[-1]
        last_avg_p1.pop()
    else:
        last_points = points + last_points_p2[-1]
        last_points_p2.pop()
        last_avg = last_avg_p2[-1]
        last_avg_p2.pop()
    
    return last_points, round(last_avg)

def on_closing():
        if messagebox.askokcancel("Schließen", "Wollen Sie das Spiel wirklich beenden?"):
            try:
                two_player.two_player_root.destroy()
            except AttributeError:
                pass
            try:
                one_player.one_player_root.destroy()
            except AttributeError:
                pass
            gui.select.destroy()
        else:
            return