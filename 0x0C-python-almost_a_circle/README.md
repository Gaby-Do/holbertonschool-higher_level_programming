0x0C. Python - Almost a circle

Learning Objectives

- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

Tasks
- All your files, classes and methods must be unit tested and be PEP 8 validated.
- 1. Base class - first class Base
- 2. First Rectangle - class Rectangle that inherits from Base
- 3. Validate attributes - Update Rectangle by adding validation of all
\t setter methods and instantiation (id excluded)
- 4. Area first - Update Rectangle by adding the public method def area(self)
- 5. Display #0 - Update Rectangle by adding a public method that prints Rectangle instance with char #
- 6. __str__ - Update the class Rectangle by overriding the __str__ method
- 7. Display #1 - print Rectangle with character # by taking care of x and y
- 8. Update #0 - assigns an argument to each attribute
- 9. Update #1 - Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes
- 10. And now, the Square! - Write the class Square that inherits from Rectangle
- 11. Square size - Update the class Square by adding the public getter and setter size
- 12. Square update - Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes
- 13. Rectangle instance to dictionary representation - Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle
- 14. Square instance to dictionary representation - Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square
- 15. Dictionary to JSON string - Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries
- 16. JSON string to file - Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file
- 17. JSON string to dictionary - Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string
- 18. Dictionary to Instance - Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set
- 19. File to instances - Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances
