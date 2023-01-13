class MyEnumerate():
    def __init__(self, data, label):
        self.data = data
        self.label = label
        self.index = -1

    def __iter__(self):
         return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.data):
            return self.index, self.data[self.index], self.label[self.index]
        else:
            raise StopIteration

def main():

    data = [[174, 63], [165, 45], [168, 61], [180, 85], [163, 52]]
    label = ['male', 'female', 'male', 'male', 'female']

    for index, info, target in MyEnumerate(data, label):
        print(f"id:{index} | height:{info[0]} weight:{info[1]} -> {target}")
    
    # the output should look like the following:
    # id:0 | height:174 weight:63 -> male
    # id:1 | height:165 weight:45 -> female
    # id:2 | height:168 weight:61 -> male
    # id:3 | height:180 weight:85 -> male
    # id:4 | height:163 weight:52 -> female


if __name__ == "__main__":
    main()


