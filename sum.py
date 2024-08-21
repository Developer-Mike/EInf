nums = [4, 5, 3, 2]
goal = 6

def get_sum_sublist(current_numbers, available_numbers, goal):
    for new_number in available_numbers:
        new_current_numbers = current_numbers + [new_number]

        if sum(new_current_numbers) == goal: return new_current_numbers

        updated_available_numbers = [o for o in available_numbers if o != new_number]
        result = get_sum_sublist(new_current_numbers, updated_available_numbers, goal)

        # Possible result found
        if result != None: return result
    
    return None

def get_sum_list(nums, goal):
    filtered_nums = [num for num in nums if num <= goal]
    return get_sum_sublist([], filtered_nums, goal)
        
print(get_sum_list(nums, goal))