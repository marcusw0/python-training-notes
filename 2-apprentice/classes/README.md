# Classes in Python

This course section introduces classes, objects, instance state, inheritance,
encapsulation, and polymorphism. The notebooks are split into short cells so
object state and method output stay close to the code that produced them.

## Recommended Order

1. `classes_and_instances.ipynb`
2. `class_initialization.ipynb`
3. `instance_variables.ipynb`
4. `class_variables.ipynb`
5. `private_variables.ipynb`
6. `superclass_and_subclass.ipynb`
7. `classes_and_inheritance.ipynb`
8. `class_inheritance_exercise.ipynb`
9. `multilevel_inheritance.ipynb`
10. `multiple_inheritance.ipynb`
11. `polymorphism.ipynb`
12. `programming_problems_using_classes.ipynb`

## Topic Map

| Topic | Files | Main ideas |
| --- | --- | --- |
| Objects and attributes | `classes_and_instances.ipynb` | Class definitions, instances, dynamic attributes |
| Initialization | `class_initialization.ipynb` | `__init__`, `self`, methods, deleting attributes |
| Instance variables | `instance_variables.ipynb` | Per-object state and dictionaries |
| Class variables | `class_variables.ipynb` | Shared class state, instance overrides |
| Private variables | `private_variables.ipynb` | Name mangling, getters, setters, internal state |
| Inheritance | `superclass_and_subclass.ipynb`, `classes_and_inheritance.ipynb` | Parent classes, subclasses, `super()` |
| Inheritance exercises | `class_inheritance_exercise.ipynb`, `multilevel_inheritance.ipynb`, `multiple_inheritance.ipynb` | Payroll, family hierarchy, multiple parents |
| Polymorphism and problems | `polymorphism.ipynb`, `programming_problems_using_classes.ipynb` | Method overrides, reusable class designs |

## Quick Reference

| Concept | Example |
| --- | --- |
| Class definition | `class Student:` |
| Constructor | `def __init__(self, name):` |
| Instance attribute | `self.name = name` |
| Class variable | `raise_amount = 1.04` |
| Inheritance | `class Sprint(Competition):` |
| Parent call | `super().__init__(...)` |
| Private-style name | `self.__name` |

