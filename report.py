
"""
def main():
   spacecraft = {"name" : " Voyager 1", "Distance" : "153"}
   print(create_report(spacecraft))


def create_report(spacecraft):
   return f
   ___________________
    ===================
    ====== Report =====
   ___________________

   Name     : TO
   Distance : TOdo
    
     this will not pass the values
    ___________________
    ===================
    ___________________
    

    
 main()
"""

"""

def main():
    spacecraft = {"name" : " Voyager 1", "Distance" : "153"}
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f
    ___________________
    ===================
    ====== Report =====
    ___________________

    Name     : {spacecraft["name"]}
    Distance : {spacecraft["Distance"]} AU
    
    
    ___________________
    ===================
    ___________________
    

    
main()

"""

def main():
    spacecraft = {"name" : " James Web Space Telescope"}
    spacecraft.update({"Distance" : 123.2, "Orbit" : "Sun"})
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ___________________
    ===================
    ====== Report =====
    ___________________

    Name     : {spacecraft.get("name", "Unknown")}
    Distance : {spacecraft.get("Distance", "Unknown")} AU
    Orbit    : {spacecraft.get("Orbit", "Unknown")}

    
    
    ___________________
    ===================
    ___________________
    

    """
main()