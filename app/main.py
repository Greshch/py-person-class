class Person:
    people = []

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.append({"name": name, "age": age})


def create_person_list(people: list) -> list:
    persons = []
    for obj in people:
        person = Person(obj["name"], obj["age"])
        attribute = "wife" if "wife" in obj else "husband"
        value = obj[attribute]
        person.__setattr__(attribute, value)
        persons.append(person)
    return persons
