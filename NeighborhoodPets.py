#Author: Ashley Johnson
#Date: 4/26/2021
#Description: Program loads data from a json file, adds a pet, deletes a pet, searches for the owner
#of the pet, saves data to a json file, and returns a set of all pet species.

import json


class NeighborhoodPets():
    """class initializes pet dictionary, adds pets, gets the dictionary of pets, deletes pets, reads
       a json, saves file to json, and gets a set of all pet species."""

    def __init__(self):
        """initializes pet dictionary"""

        self._pets_dict = {}

    def get_pets(self):
        """returns pet dictionary"""
        return self._pets_dict

    #def add_pet(self, name, species, owner):
        #if name not in self._pets_dict.keys():
            #self._pets_dict[name] = {
                #name : "name",
                #species : "species",
                #owner : "owner"
            #}
            #return self._pets_dict

    def add_pet(self, name, species, owner):
        try:
            self._pets_dict[name]
        except KeyError:
            new_pet = {
                "name": name,
                "owner": owner,
                "species": species
            }
            self._pets_dict[name] = new_pet
        else:
            print("this pet already exists {}".format(name))

    def delete_pet(self, pet_name):
        """deletes pet from pet dictionary"""
        try:
            pet = self._pets_dict[pet_name]
        except KeyError:
            print("pet name not found")
        del self._pets_dict[pet_name]


    def save_as_json(self, json_file):
        """saves file as json file."""
        data = self.get_pets()
        with open(json_file,'w') as outfile:
            json.dump(data, outfile)

    def read_json(self, file_name):
        """reads json file"""
        with open(file_name) as json_file:
            self._pets_dict = json.load(json_file)

    def get_owner(self,pet_name):
        """gets owner of pet"""
        data = self.get_pets()
        print(data)
        owner = None
        try:
            this_pet = data[pet_name]
        except KeyError:
            print("pet name not found")
        return this_pet["owner"]

    def get_all_species(self):
        """returns a set of all species in pet dictionary"""
        pets = self.get_pets()
        species_list = {}
        for entry in pets:
            species = entry["species"]
            species_list[species] = "found"
        return set(species_list.keys())


class Pet():
    """class initializes name, owner, and species"""
    def __init__(self,name,owner,species):
        self._name = name
        self._owner = owner
        self._species = species

    def get_name(self):
        return self._name

    def get_owner(self):
        return self._owner

    def get_species(self):
        return self._species

def main(argv=None):
    """
    Entry Point
    """

    nbhood = NeighborhoodPets()


    nbhood.add_pet('Parika', 'dog', 'Ashley')
    nbhood.add_pet('Dobby', 'cat', 'Nikkie')
    nbhood.save_as_json("NeighboorhoodPets.json")
    pets = nbhood.get_pets()
    pet_owner = nbhood.get_owner("Parika")
    print(pet_owner)
    print(pets)


if __name__ == "__main__":


    main()
