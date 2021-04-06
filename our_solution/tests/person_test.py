import unittest
from src.person import Person
from src.bus import Bus

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("Guido van Rossum", 64, "Waverly Station")

    # @unittest.skip("Delete this line to run the test")
    def test_person_has_name(self):
        self.assertEqual("Guido van Rossum", self.person.name)

    # @unittest.skip("Delete this line to run the test")
    def test_person_has_age(self):
        self.assertEqual(64, self.person.age)

    def test_destination_of_bus(self):
        bus = Bus(22, "Waverly Station")
        self.assertEqual (True, self.person.check_destination_of_bus(bus))

    def test_get_on_bus(self):
        bus = Bus(22, "Waverly Station")
        self.assertEqual (1, len(bus.passengers))
