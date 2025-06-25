
def kilometers_miles_converter(conversion_units,distance):
    units_selected = conversion_units
    if units_selected == "kms to miles":
        distance_in_miles = distance * 0.6
        return f"{distance} kms is equal to {distance_in_miles:.2f} miles"

    else:
        distance_in_kms = distance/0.6
        return f"{distance} miles is equal to {distance_in_kms:.2f} kms"


