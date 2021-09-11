sulawesi_dictionary = {
  "Sulawesi Barat": "Mamuju",
  "Sulawesi Selatan": "Makassar",
  "Sulawesi Tenggara": "Kendari",
  "Sulawesi Tangah": "Palu",
  "Sulawesi Utara": "Manado",
  "Gorontalo": "Gorontalo",
}

# Nesting a list in a dictionary
sulawesi_dictionary = {
  "Sulawesi Barat": {"cities": ["Polewali Mandar", "Majene", "Mamuju", "Mamasa", "Mamuju Utara"], "total": 6},
  "Sulawesi Selatan": {"cities" : ["Makassar", "Pare-pare", "Pinrang", "Barru", "Pangkep", "Maros"], "total": 6},
  "Sulawesi Tenggara": {"cities" : ["Kendari"], "total" : 1},
  "Sulawesi Tangah": {"cities" : ["Palu"], "total" : 1},
  "Sulawesi Utara": {"cities":["Manado", "Tomohon"], "total":2},
  "Gorontalo": {"cities":["Gorontalo"], "total":1},
}

# Nesting a dictioanry in a list
sulawesi_dictionary = [
  {
    "country":"Sulawesi Barat",
    "cities": ["Polewali Mandar", "Majene", "Mamuju", "Mamasa", "Mamuju Utara"],
    "total": 6
  },
  {
    "country":"Sulawesi Selatan",
    "cities" : ["Makassar", "Pare-pare", "Pinrang", "Barru", "Pangkep", "Maros"],
    "total": 6
  },
]