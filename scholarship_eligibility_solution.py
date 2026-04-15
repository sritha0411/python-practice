def is_eligible(GPA, extracurricular_activities, community_service_hours, financial_need):
    if GPA >= 3.5 and extracurricular_activities >= 2 and community_service_hours >= 50 and financial_need >= 10000:
        return True
    elif GPA >= 4.0 and extracurricular_activities == 1 and community_service_hours >= 100:
        return True
    elif GPA >= 3.0 and extracurricular_activities >= 3 and community_service_hours >= 200 and financial_need >= 5000:
        return True
    return False
print(is_eligible(float(input()), int(input()), int(input()), float(input())))