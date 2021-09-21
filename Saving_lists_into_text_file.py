# If you wanna save list into txt file and load it as list in python
# IF you wanna save list into file as retrieve it back as list
# with out using pickle or numpy in python
# here is a trick

import json
data = [1, 2, 3, 4, 5]
print(data[4]+data[2])

with open('bin.data', "wb") as file:
     file.write(json.dumps(data).encode())
     # Encoding is necessary because we are saving
     # it in binary format# Run it now


# Reading list back

with open("bin.data", "rb") as file:
    data = file.read()
    data = json.loads(data)
    # Reading from file as list

    print(data)
    print(data[4] + data[2])
        # Boom
