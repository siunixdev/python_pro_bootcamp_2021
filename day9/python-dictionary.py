sulawesi_dictionary = {
  "Sulawesi Barat": "Mamuju",
  "Sulawesi Selatan": "Makassar",
  "Sulawesi Tenggara": "Kendari",
  "Sulawesi Tangah": "Palu",
  "Sulawesi Utara": "Manado"
}

print(sulawesi_dictionary)
print(f"ibukota Sulawesi barat adalah {sulawesi_dictionary['Sulawesi Barat']}")

sulawesi_dictionary["Gorontalo"] = "Gorontalo"
print(sulawesi_dictionary)

for ibukota in sulawesi_dictionary:
  print(sulawesi_dictionary[ibukota])