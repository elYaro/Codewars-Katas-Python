'''
How many bees are in the beehive?

bees can be facing UP, DOWN, LEFT, or RIGHT
bees can share parts of other bees
Examples

Ex1
bee.bee     
.e..e..
.b..eeb
Answer: 5

Ex2
bee.bee     
e.e.e.e
eeb.eeb
Answer: 8

Notes
The hive may be empty or null
Python: the hive is passed as a list of lists (not a list of strings)
'''

def how_many_bees(hive):
    if hive == None or len(hive) <3:
        return 0
    else:
        new_hive = []
        nomber_of_bees = 0
        
        for sublist in hive:
            new_hive.append(("".join(sublist)))
        
        for element in new_hive:
            nomber_of_bees += element.count("bee")
            nomber_of_bees += element.count("eeb")
        
        for nomber_of_positions_in_row in range(0, (len(new_hive[0]))):
            for nomber_of_rows in range(0, (len(new_hive))-2):
                if new_hive[nomber_of_rows][nomber_of_positions_in_row] == "b" and new_hive[nomber_of_rows + 1][nomber_of_positions_in_row] == "e" and new_hive[nomber_of_rows + 2][nomber_of_positions_in_row] == "e":
                    nomber_of_bees += 1
                    
                if new_hive[nomber_of_rows][nomber_of_positions_in_row] == "e" and new_hive[nomber_of_rows + 1][nomber_of_positions_in_row] == "e" and new_hive[nomber_of_rows + 2][nomber_of_positions_in_row] == "b": 
                    nomber_of_bees += 1
                  


    return nomber_of_bees