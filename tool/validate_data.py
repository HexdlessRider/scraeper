# def compare_dicts_by_key_fast(array1, array2, key, update_key):
#     # Create a set of keys from array2 for fast lookup
#     keys_in_array2 = {d[key]: d for d in array2}
#     # Filter out dictionaries in array1 whose key value is not found in the keys_in_array2 set
#     unique_data = []
#     to_update_array = []
#     for item in array1:
#         if item[key] not in keys_in_array2:
#             unique_data.append(item)
#         elif item[update_key[0]] != keys_in_array2[item[key]][update_key[0]]:
#             to_update_array.append(item)
#     print(unique_data,
#           to_update_array)
#     return unique_data, to_update_array


def compare_dicts_by_key_fast(array1, array2, key, keys_to_check):
    keys_in_array2 = {d[key]: d for d in array2}
    # print("keys_in_array2", keys_in_array2)
    unique_data = []
    to_update_array = []
    for item in array1:

        if item[key] not in keys_in_array2.keys():
            unique_data.append(item)

        else:
            existing_item = keys_in_array2[item[key]]
            # Check if any of the specified keys have different values
            if any(item[k] != existing_item[k] for k in keys_to_check if k in item and k in existing_item):
                to_update_array.append(item)

    return unique_data, to_update_array
