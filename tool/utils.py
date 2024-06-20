import logging


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


def generate_rental_listings_message(user, apartments):
    message = f"Instarent nieuwe huurwoning\n\nHoi {user['username']},\n\nWe hebben meerdere nieuwe huurwoningen gevonden die passen bij je zoekfilters:\n\n"
    try:
        for apartment in apartments:
            message += (
                f"{apartment['location']}\n"
                f"{apartment['address']}\n"
                f"€{apartment['price']}\n"
                f"{apartment['bedrooms']}\n"
                f"{apartment['square_meters']} m2\n\n"
                f"{apartment['link']}\n\n"
            )
    except Exception as e:
        logging.error(e)

    return message, user['phone_number']
