def is_watered(soil_dry, raining, day_time, temperature):
    if soil_dry:
        return True
    elif raining==False:
        return True
    elif day_time:
        return True
    elif temperature>10:
        return True
    return False
print(is_watered(bool(input()), bool(input()), bool(input()), int(input())))