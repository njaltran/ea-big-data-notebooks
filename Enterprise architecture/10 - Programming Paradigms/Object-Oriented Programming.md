Separate data and procedures.
-state is part of the object

Objects--> have methods


Class is a template --> instantiate --> object(S)

```
class something():
	def __init__(self, assign):
		self.attribute= assign
	def method(self):
		DO SOMETHING 
		
x = something(data)
x.method()
```


[[Polymorphism]]

## Visual - class to object

```mermaid
flowchart LR
    C["class Dog<br/>name<br/>bark()"] -->|instantiate| O1["dog1<br/>name='Rex'"]
    C --> O2["dog2<br/>name='Buddy'"]
    C --> O3["dog3<br/>name='Lola'"]
```

## Visual - the four pillars

```mermaid
mindmap
  root((OOP))
    Encapsulation
      hide internal state
      expose via methods
    Inheritance
      child gets parent's stuff
      override what differs
    Polymorphism
      same call
      many behaviors
    Abstraction
      ignore details
      think in interfaces
```

## Learn more
- Wikipedia: [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [Real Python: OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- See [[Polymorphism]], [[Duck Typing]]
