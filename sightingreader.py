from dataclasses import dataclass

@dataclass
class Sighting:
    spotter: int
    animal: str
    count: int
    area: int
    period: int


class SightingReader:

    def get_sightings(self, filename):
        import csv
        sightings = []
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if len(row) != 5:
                    print("Rij gevonden die geen 5 velden heeft... Ignoring...")
                else:
                    print(row)
                    sightings.append(Sighting(row[0], row[1], row[2], row[3], row[4]))
        return sightings


class AnimalMonitor:

    def __init__(self):
        self.sightings = []

    def add_sightings(self, filename):
        sr = SightingReader()
        self.sightings = sr.get_sightings(filename)

    def get_count(self, animal):
        pass

    def print_list(self):
        for s in self.sightings:
            print(s)

    def print_sightings_by(self, spotter):
        pass

    def print_sightings_of(self, animal):
        pass


if __name__ == "__main__":
    s = Sighting(0, "Olifant", 0, 0, 0)
    print(s)

    sr = SightingReader()
    print(sr.get_sightings("sightings.csv"))

    animalMo1 = AnimalMonitor()
    animalMo1.add_sightings("sightings.csv")
    animalMo1.print_list()
    print(animalMo1.get_count("Elephant"))
    print(animalMo1.print_sightings_by(2)) # spotter nr 2?
    print(animalMo1.print_sightings_of("Elephant")) 

