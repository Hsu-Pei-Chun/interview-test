from timer import measure_time

def find_digit_at_position(position: int) -> int:
    digit_length = 1 # 當前數字的位數 (1 位數, 2 位數, 3 位數, ...)
    start_number = 1 # 當前位數範圍的起始數字 (1, 10, 100, 1000, ...)

    while True:
        # 當前區間內數字的總數
        count_of_numbers = 9 * digit_length * start_number

        # 當前當前區間總共佔據的位數
        total_digits_in_range = count_of_numbers * digit_length

        if position <= total_digits_in_range:
            break
        
        # 進入下一個位數的區間
        position -= total_digits_in_range
        digit_length += 1
        start_number *= 10

    # 確定目標數字所在區間的索引
    number_index = (position - 1) // digit_length
    digit_in_number = (position - 1) % digit_length

    # 確定實際數字
    actual_number = start_number + number_index

    # 取得目標數字的指定位數
    return int(str(actual_number)[digit_in_number])

print(find_digit_at_position(9))
measure_time(find_digit_at_position, 9)

print(find_digit_at_position(200)) 
measure_time(find_digit_at_position, 200)

print(find_digit_at_position(10_000))
measure_time(find_digit_at_position, 10_000) 
