class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.owner = owner
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        else:
            self.pet_type = pet_type
        
        Pet.all.append(self)

class Owner:

    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Enter valid pet")
    
    def get_sorted_pets(self):
        def pet_name(pet):
            return pet.name
        
        sorted_pets = sorted(self.pets(), key=pet_name)
        return sorted_pets
