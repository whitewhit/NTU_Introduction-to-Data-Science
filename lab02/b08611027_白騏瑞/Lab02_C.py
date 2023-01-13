class Array:
    """A Array is a self-defined sequential data type which contains a name."""
    
    def __init__(self, name, contents = None):
        """Initialize the contents.
        name: string
        contents: initial contents.
        """
        if contents == None:
            contents = []
        self.name = name
        self.contents = contents

    # def __init__(self, name, contents = []):
    #     """Initialize the contents.
    #     name: string
    #     contents: initial contents.
    #     """
    #     self.name = name
    #     self.contents = contents

    def __str__(self):
        """Return a string representaion of this Array.
        """
        t = [ self.name + ' has contents:' ]
        for obj in self.contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    # Hint: two special functions here
    def __getitem__(self, key):
        item = self.contents[key]
        return item
    
    def __setitem__(self, key, value):
        self.contents[key] = value

    def add_item(self, item):
        """Adds a new item to the contents.
        item: any object to be added
        """
        self.contents.append(item)

def main():

    arr1 = Array('MyFirstArray')

    arr1.add_item('wallet')
    arr1.add_item('car keys')

    print(arr1) 
    # you should see the output: 
    # MyFirstArray has contents:
    #   'wallet'
    #   'car keys'

    # The following 3 statements should work
    # after you finish TODO_C1
    print(arr1[0]) # 'wallet'
    arr1[0] = 'toys'
    print(arr1[0]) # 'toys'

    arr2 = Array('MySecondArray')
    arr1.add_item(arr2)
    print(arr1)

    # If you run this program as is, it seems to work.
    # To see the problem, trying printing arr2.


if __name__ == "__main__":
    main()

