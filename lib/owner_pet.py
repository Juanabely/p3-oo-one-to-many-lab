class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    _instances = []

    def __init__(self, name, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception('Invalid pet type')
        self.name = name
        self.pet_type = pet_type
        self.owner = None
        self._instances.append(self)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_pet_type(self):
        return self.pet_type

    def set_pet_type(self, pet_type):
        self.pet_type = pet_type

    @classmethod
    def all(cls):
        return cls._instances


class Owner:
    def __init__(self, name):
        self._name = name
        self._pets = []

    @property
    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            self._pets.append(pet)
            pet.owner = self
        else:
            raise TypeError("Input object is not of type Pet")

    def remove_pet(self, pet):
        if isinstance(pet, Pet):
            if pet in self._pets:
                self._pets.remove(pet)
                pet.owner = None
            else:
                raise ValueError("Pet not found in the list")
        else:
            raise TypeError("Input object is not of type Pet")

    @property
    def pets(self):
        return self._pets

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.get_name())
