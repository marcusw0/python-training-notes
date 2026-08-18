# Advanced Functions and Python Classes

This course section builds on the novice function and class material with
object-oriented features and reusable function patterns. The notebooks show
state changes and method behavior directly below each example.

## Recommended Order

1. `custom_iterators.ipynb`
2. `decorators.ipynb`
3. `abstract_base_class.ipynb`
4. `class_methods_static_methods.ipynb`
5. `getters_setters_deleters.ipynb`

## Topic Map

| Topic | Files | Main ideas |
| --- | --- | --- |
| Custom iteration | `custom_iterators.ipynb` | Iterator protocol, `__iter__`, `__next__`, stopping |
| Decorators | `decorators.ipynb` | Wrapping functions, preserving behavior, validation |
| Abstract classes | `abstract_base_class.ipynb` | Interfaces, required methods, subclass contracts |
| Class and static methods | `class_methods_static_methods.ipynb` | `@classmethod`, `@staticmethod`, alternate constructors |
| Properties | `getters_setters_deleters.ipynb` | `@property`, setters, deleters, controlled access |

## Practice Labs

1. Add a custom iterator that counts down instead of up.
2. Write a decorator that prints before and after a function call.
3. Create an abstract base class for a payment method with a required `pay()`
   method.
4. Add a class method that creates an object from a comma-separated string.
5. Add validation in a property setter so invalid values are rejected.

## Quick Reference

| Feature | Syntax |
| --- | --- |
| Iterator object | `iter(obj)` |
| Next value | `next(iterator)` |
| Decorator | `@decorator_name` |
| Abstract method | `@abc.abstractmethod` |
| Class method | `@classmethod` |
| Static method | `@staticmethod` |
| Property getter | `@property` |

