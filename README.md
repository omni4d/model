# Model
An omni4d model contains signs which refer to objects in the real world. There are 4 basic types of sign:

1. Individual - Refers to an object which has constant identity over time

1. Class - Refers to a set of objects

1. Event - Refers to an object with extension across space at a point in time

1. Tuple - Refers to a relationship between multiple objects

Class and Tuple have further subtypes. All Class and Tuple signs must be one of these subtypes rather than the basic type:

1. Class of Individuals
2. Class of Classes
2. Class of Events
3. Class of Tuples
4. Whole-Part Tuple - Indicating that the second item is part of the first
5. Class-Member Tuple - Indicating that the second item is a member of the first
6. Ordinary Tuple

# Work
The intention of this repository is to produce a set of YAML (https://en.wikipedia.org/wiki/YAML) files which are omni4d models. These can then be used as the basis for further implementations probably involving various database systems and programming languages.

# Acknowledgments
This work is based upon the ideas described by Chris Partridge in his book "Business Objects: Re-Engineering for Re-Use" (https://books.google.co.uk/books?id=BIFFAAAAYAAJ).

Those ideas are, in turn, based upon the work of [Aristotle](https://en.wikipedia.org/wiki/Aristotle), [Georg Cantor](https://en.wikipedia.org/wiki/Georg_Cantor), [Gottlob Frege](https://en.wikipedia.org/wiki/Gottlob_Frege), [Albert Einstein](https://en.wikipedia.org/wiki/Albert_Einstein), [Willard van Orman Quine](https://en.wikipedia.org/wiki/Willard_Van_Orman_Quine) and countless others.
]
