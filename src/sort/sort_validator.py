def check_order(list_to_check):
    for x in range(1, len(list_to_check)):
        previous_positon_value = list_to_check[x-1]
        current_position_value = list_to_check[x]
        if previous_positon_value > current_position_value:
            return False
    return True