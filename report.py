def main():
    spacecraft = {"name": "Voyager 1"}
    spacecraft.update({"distance": 163, "orbit": "Sun"})
    print(report(spacecraft))

def report(spacecraft):
    return f"""

    ========== REPORT ==========

    Name: = {spacecraft.get("name", "Unknown")}
    Distance: = {spacecraft.get("distance", "Unknown")} AU
    Orbit: = {spacecraft.get("orbit", "Unknown")}

    ============================
    """

main()