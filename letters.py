def main():
    names = [" MARIO" , "Luigi", "Daisy", "Yoshu", "Ramo"]
    for name in names:
   #you could use that to 
   #  for i in range(len(name)):
        print(write_letter(name,"Princes Peach"))


def write_letter(reciver,sender):
    return f"""
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
```````````````````````````````````````````
Dear {reciver}

You Are Cordially invited to a ball at 
peach's castle this evening, 7:00 PM.

Sincerely,
{sender}


```````````````````````````````````````````
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
```````````````````````````````````````````
"""

main()