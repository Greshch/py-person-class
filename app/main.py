class Person:
    people = {}
    # people = []

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # Person.people.append({"name": name, "age": age})
        Person.people[name] = self

def create_person_list(people: list) -> list:
    persons = []
    for person in people:
        obj = Person(person["name"], person["age"])
        partner = "wife" if "wife" in person else "husband"
        obj.__setattr__(partner, person[partner])
        persons.append(obj)

    for person in persons:
        partner = "wife" if hasattr(person, "wife") else "husband"
        key = person.__getattribute__(partner)
        if key is None:
            person.__delattr__(partner)
        else:
            obj = Person.people[key]
            person.__setattr__(partner, obj)
    return persons
