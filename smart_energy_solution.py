def is_activated(house_occupied, high_energy_appliance_on, peak_hours, current_energy_usage):
    if (house_occupied==False):
        return True
    elif (high_energy_appliance_on and peak_hours):
        return True
    elif (current_energy_usage>50):
        return True
    else:
        return False

print(is_activated(bool(input()), bool(input()), bool(input()), int(input())))