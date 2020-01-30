

@dataclass
class Sighting:
    spotter: int
    animal: str
    count: int
    area: int
    period: int


class SightingReader:

    def get_sightings(filename):
        import csv
        sightings = []
        # Parse CSV
        # for row in csv:
        #    s = Sighting(...)
        # return sightings
        pass


class AnimalMonitor:

    def __init__(self):
        self.sightings = []

    def add_sightings(filename):
        # vul self.sightings
        pass

    def get_count(animal):
        pass

    def print_list():
        pass

    def print_sightings_by(spotter):
        pass

    def print_sightings_of(animal):
        pass


if __name__ == "__main__":
    animalMo1 = AnimalMonitor()

    animalMo1.add_sightings("sightings.csv")
    print(animalMo1.get_count("Elephant"))
    print(animalMo1.print_sightings_by(2)) # spotter nr 2?
    print(animalMo1.print_sightings_of("Elephant")) 

