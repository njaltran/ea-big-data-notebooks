Same inference but different behavior, 

Duck typing: 
- if it walks like a duck, it quacks like a duck then it must be a duck
- Dynamic type checking


If two objects have the same methods, you can pool them together and call the method of the shared function

## Visual

```mermaid
flowchart TD
    F["make_sound(animal)"]
    F -->|animal is Dog| D["dog.bark() → woof"]
    F -->|animal is Cat| C["cat.meow() → meow"]
    F -->|animal is Cow| CW["cow.moo() → moo"]
```
Same function call. Different behavior depending on the object.

## Visual - mixed list

```mermaid
flowchart LR
    L["[dog, cat, cow]"] --> LOOP[for animal in list]
    LOOP --> CALL["animal.sound()"]
    CALL --> O1["woof"]
    CALL --> O2["meow"]
    CALL --> O3["moo"]
```

## Learn more
- Wikipedia: [Polymorphism (computer science)](https://en.wikipedia.org/wiki/Polymorphism_(computer_science))
- See [[Object-Oriented Programming]], [[Duck Typing]]



