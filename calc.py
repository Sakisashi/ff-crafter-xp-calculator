# Function to calculate the number of items needed to reach the desired level
def calculate_items(desired_level, current_level, current_xp, xp_per_item):
    # Experience points required for each level (example values, please adjust as needed)
    xp_chart = {
    1: 300,
    2: 750,
    3: 1380,
    4: 2350,
    5: 3790,
    6: 5730,
    7: 8730,
    8: 12650,
    9: 17620,
    10: 23520,
    11: 30950,
    12: 39570,
    13: 49770,
    14: 61070,
    15: 74170,
    16: 89370,
    17: 106770,
    18: 126370,
    19: 148270,
    20: 172570,
    21: 199970,
    22: 230570,
    23: 264470,
    24: 301770,
    25: 342570,
    26: 391770,
    27: 446370,
    28: 508270,
    29: 573870,
    30: 642270,
    31: 716270,
    32: 798970,
    33: 887670,
    34: 982670,
    35: 1084670,
    36: 1197670,
    37: 1318670,
    38: 1451670,
    39: 1593670,
    40: 1748670,
    41: 1898670,
    42: 2082670,
    43: 2261670,
    44: 2448670,
    45: 2643670,
    46: 2857670,
    47: 3086670,
    48: 3330670,
    49: 3589670,
    50: 4010670,
    51: 4510670,
    52: 5090670,
    53: 5750670,
    54: 6630670,
    55: 7490670,
    56: 8370670,
    57: 9270670,
    58: 10190670,
    59: 11339670,
    60: 12610670,
    61: 12997670,
    62: 14453670,
    63: 15987670,
    64: 17608670,
    65: 19328670,
    66: 21162670,
    67: 25256670,
    68: 27573670,
    69: 30123670,
    70: 33046670,
    71: 36064670,
    72: 39121670,
    73: 42321670,
    74: 45621670,
    75: 49846770,
    76: 53306770,
    77: 57806770,
    78: 62306770,
    79: 67806770,
    80: 73306770,
    81: 79306770,
    82: 85506770,
    83: 91906770,
    84: 98606770,
    85: 105706770,
    86: 113586770,
    87: 121706770,
    88: 130086770,
    89: 138706770,
    90: 152086770,
    91: 165706770,
    92: 179586770,
    93: 193206770,
    94: 208119270,
    95: 226653270,
    96: 244916270,
    97: 265238270,
    98: 286195270,
    99: 309174270,
    100: 332963270,
}
    # Calculate total XP needed to reach the desired level
    total_xp_needed = xp_chart[desired_level] - (xp_chart[current_level] + current_xp)

    # Calculate the number of items needed
    if total_xp_needed <= 0:
        return 0  # Already at or above desired level
    else:
        items_needed = total_xp_needed / xp_per_item
        return int(items_needed) + (1 if total_xp_needed % xp_per_item > 0 else 0)  # Round up if needed


# Example usage
desired_level = int(input("Enter desired level: "))
current_level = int(input("Enter current level: "))
current_xp = int(input("Enter current XP to next level: "))
xp_per_item = int(input("Enter XP per item: "))

items_needed = calculate_items(desired_level, current_level, current_xp, xp_per_item)
print(f"You need to give {items_needed} items to reach level {desired_level}.")