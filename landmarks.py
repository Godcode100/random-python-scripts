cities = {
    "SEATTLE": "WASHINGTON USA",
    "PORTLAND":"OREGON USA",
    "BOSTON":"MASSACHUSETS USA"
    }
landmarks ={
    "LIBERY SHIP MEMORIAL":"PORTLAND",
    "ALAMO":"SAN ANTONIO",
    "SPACE NEEDLE":"SEATTLE"
    }

def lookup_landmark(landmark):
    landmark = landmark.upper()
    try:
        city = landmarks[landmark]
        state = cities[city]
    except KeyError as e:
        raise KeyError("Landmark not found") from e
    print(f"{landmark} is in {city} {state}")

lookup_landmark("space needle")
#lookup_landmark("alamo")
lookup_landmark("golden gate bridge")
        
