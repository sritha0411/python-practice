def smart_home(door_open, window_open, motion_detected, alaram_deactivated):
    if (door_open and not alaram_deactivated) or (window_open and not alaram_deactivated) or (motion_detected and not alaram_deactivated):
        return True
    return False

print(smart_home(bool(input()), bool(input()), bool(input()), bool(input())))