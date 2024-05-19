class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"Invalid pet type: {pet_type}. Your pet mu be one of {Pet.PET_TYPES}.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name
        
        
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet.")
        pet.owner = self
    def pets(self):
        return [pet for pet in Pet.all if isinstance(pet.owner, Owner) and pet.owner == self]


    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
