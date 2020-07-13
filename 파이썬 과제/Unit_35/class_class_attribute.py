class Person:
    bag = []

    def put_bag(self, stuff):
        #self.bag.append(stuff)
        Person.bag.append(stuff)

james = Person()
james.put_bag('book')

maria = Person()
maria.put_bag('key')

print(james.bag)
print(maria.bag)
print(Person.bag)
