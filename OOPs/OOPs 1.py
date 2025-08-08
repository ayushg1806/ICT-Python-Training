#Create a Class and Display Its Namespace
class MyClass:
    def __init__(self):
        self.attribute1 = 'Hello'
        self.attribute2 = 'World'
    def method1(self):
        return 'This is method1'
print(MyClass.__dict__)
for name in MyClass.__dict__:
    print(name)
