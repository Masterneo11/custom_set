

class CustomSet():


    def __init__(self):
        self.a = []


    def add(self, item : str):
       if item not in self.a:
           self.a.append(item)
        
    

    def remove(self, item :str):
        if item not in self.a:
            raise KeyError(f"{item} not removed, try again")
        self.a.remove(item)


    def as_list(self) -> list:
        return self.a

    def clear(self):
        self.a = []


def main():
    
    my_set = CustomSet()
    my_set.add("item 1")
    my_set.add("item 2")
    my_set.add("item 1")

    print(my_set.as_list()) # ["item 1", "item 2"]

    my_set.remove("item 2")
    print(my_set.as_list()) # ["item 1"]

    try:
        my_set.remove("item 3")
    except KeyError:
        print("Item not removed, moving forward")

    my_set.clear()
    print(my_set.as_list()) # []



if __name__ == "__main__":
    main()
