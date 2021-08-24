# List data structure
west_sulawesi = ["Polewali Mandar", "Majene", "Mamuju", "Mamuju Utara", "Mamasa", "Pasangkayu"]

print(west_sulawesi)
print(west_sulawesi[0])

# You can get the last item of west sulawesi
print(west_sulawesi[-1])
print(west_sulawesi[-2])

# You can change the item
west_sulawesi[0] = "Polman"
print(west_sulawesi)

# To add new item of the list
west_sulawesi.append("Darma city")
print(west_sulawesi)

# Extend the list by appending all the items from the iterable.
west_sulawesi.extend(["Pekkabata", "Banggae", "Bangae Timur"])
print(west_sulawesi)

# More : https://docs.python.org/3/tutorial/datastructures.html