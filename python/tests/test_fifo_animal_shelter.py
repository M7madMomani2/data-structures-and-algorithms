import pytest
from challenges.fifo_animal_shelter.fifo_animal_shelter import *

def test_enqueue(animal_shelter):
    assert animal_shelter.to_string()== "{Dog1}->{Dog2}->{Dog3}->{Cat1}->{Cat2}->{Cat3}->NULL"

def test_dequeue(animal_shelter):
    animal_shelter.dequeue("dog")
    animal_shelter.dequeue("dog")
    animal_shelter.dequeue("dog")
    actual=animal_shelter.dequeue("xlion")
    assert animal_shelter.to_string()== "{Cat1}->{Cat2}->{Cat3}->NULL"
    assert animal_shelter.to_string()== "{Cat1}->{Cat2}->{Cat3}->NULL"
    assert actual== "NULL"





@pytest.fixture
def animal_shelter():
    animal_shelter_o=AnimalShelter()
    animal_shelter_o.enqueue(Dog('Dog1'))
    animal_shelter_o.enqueue(Dog('Dog2'))
    animal_shelter_o.enqueue(Dog('Dog3'))
    animal_shelter_o.enqueue(Cat('Cat1'))
    animal_shelter_o.enqueue(Cat('Cat2'))
    animal_shelter_o.enqueue(Cat('Cat3'))
    return animal_shelter_o
