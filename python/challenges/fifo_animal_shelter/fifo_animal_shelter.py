class Dog:
    def __init__(self,name) :
        self.name =name
        self.next=None
        self.kind='dog'
class Cat:
    def __init__(self,name) :
        self.name =name
        self.next=None
        self.kind='cat'
class Any:
    def __init__(self,name) :
        self.name =name
        self.next=None
        self.kind='Any'



class AnimalShelter :
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,animal):
        new_node = animal

        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.rear=new_node
            self.front=new_node


    def dequeue(self,pref="None"):
        if not ((pref.lower()== 'cat' or pref.lower()=='dog') and self.front):
            return "NULL"
        else:
            current = self.front
            if self.front.kind == pref:
                target = self.front
                self.front = self.front.next
                return target.name
            else:
                while current.next:
                    if current.next.kind == pref:
                        target = current.next
                        current.next = current.next.next
                        if target.name:
                            return target.name
                    if current.kind != pref:
                        current = current.next
                return 'NULL'

    def to_string(self):
        result= ''
        current = self.front
        while current:
            result += f'{{{current.name}}}->'
            current = current.next
            if current == None:
                result += 'NULL'

        return result


animal_shelter_o=AnimalShelter()
animal_shelter_o.enqueue(Dog('Dog1'))
animal_shelter_o.enqueue(Dog('Dog2'))
animal_shelter_o.enqueue(Dog('Dog3'))
animal_shelter_o.enqueue(Cat('Cat1'))
animal_shelter_o.enqueue(Cat('Cat2'))
animal_shelter_o.enqueue(Cat('Cat3'))

print(animal_shelter_o.to_string())


animal_shelter_o.dequeue("dog")
animal_shelter_o.dequeue("dog")
animal_shelter_o.dequeue("dog")
print(animal_shelter_o.to_string())








# class AnimalShelter :
#     def __init__(self):
#         self.animal_dec={'cat':[],'dog':[],'other':[] }

#     def enqueue(animal):
#         pass
#     def dequeue(pref):
#         pass
