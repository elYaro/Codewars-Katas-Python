'''
We want to generate all the numbers of three digits that:

* the value of adding their corresponding ones(digits) is equal to 10.
* their digits are in increasing order (the numbers may have two or more equal contiguous digits)

The numbers that fulfill the two above constraints are: 118, 127, 136, 145, 226, 235, 244, 334

Make a function that receives two arguments:
* the sum of digits value
* the amount of desired digits for the numbers

The function should output an array with three values: [1,2,3]
1 - the total amount of all these possible numbers
2 - the minimum number
3 - the maximum numberwith

The example given above should be:
HowManyNumbers.findAll(10, 3) == [8, 118, 334]   // as List<Integer>

If we have only one possible number as a solution, it should output a result like the one below:
HowManyNumbers.findAll(27, 3) == [1, 999, 999]

If there are no possible numbers, the function should output the empty array.
HowManyNumbers.findAll(84, 4) == []

The number of solutions climbs up when the number of digits increases.
HowManyNumbers.findAll(35, 6) == [123, 116999, 566666]

Features of the random tests:
Numbers of tests: 111
Sum of digits value between 20 and 65
Amount of digits between 2 and 15
'''

def find_all(sum_dig, digs):
    potential_min = int("1" * digs)
    potential_max = int("9" * digs)
    result_list = []
    next_number = potential_min
    
    while next_number <= potential_max:
        if sum([int(digit) for digit in list(str(next_number))]) == sum_dig:
            result_list.append(next_number)
        next_number += 1
        draft_list = list(str(next_number))
        if "0" in draft_list:
            for i in range(len(draft_list)):
                if draft_list[i] < draft_list[i - 1]:
                    draft_list[i] = draft_list[i - 1]
            next_number = int("".join(draft_list))
    return [] if len(result_list) == 0 else [len(result_list), result_list[0], result_list[-1]]