#!/usr/bin/env python3

#chmod +x play_with_arrays.py

original_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = [num + 2 for num in original_array if num > 5]

set_list = set(new_array)


print(original_array)
print(set_list)