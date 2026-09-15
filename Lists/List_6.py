medicines = ["Paracetamol", "Amoxicillin", "Ibuprofen", "Cetirizine", "Azithromycin"]

print(len(medicines))

medicines.append("Aspirin")

print(medicines)

medicines.remove("Ibuprofen")
print (medicines)

for medicine in medicines:
    print(medicine)