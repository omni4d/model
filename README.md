# Model
An omni4d model contains signs which refer to objects in the real world. There are 4 basic types of sign:

* Individual - Refers to an object which has constant identity over time

* Class - Refers to a set of objects

* Event - Refers to an object with extension across space at a point in time

* Tuple - Refers to a relationship between multiple objects

Class and Tuple have further subtypes. All Class and Tuple signs must be one of these subtypes rather than the basic type:

* Class of Individuals
* Class of Classes
* Class of Events
* Class of Tuples
* Whole-Part Tuple - Indicating that the second object is part of the first
* Class-Member Tuple - Indicating that the second object is a member of the first
* Ordinary Tuple

Every sign must have a unique id apnd tuples must contain a list of objects to which they refer.

# Work
The intention of this repository is to produce a set of [YAML](https://en.wikipedia.org/wiki/YAML) files which are omni4d models. These can then be used as the basis for further implementations probably involving various database systems and programming languages.

[core.yaml](https://github.com/omni4d/model/blob/master/core.yaml) contains the core model which is then used within [example.yaml](https://github.com/omni4d/model/blob/master/example.yaml) to represent the author of this repository.

# Acknowledgments
This work is based upon the idea of a 4D spatio-temporal object paradigm described by Chris Partridge in his book "Business Objects: Re-Engineering for Re-Use" (https://books.google.co.uk/books?id=BIFFAAAAYAAJ).

Those ideas are, in turn, based upon the work of [Aristotle](https://en.wikipedia.org/wiki/Aristotle), [Georg Cantor](https://en.wikipedia.org/wiki/Georg_Cantor), [Gottlob Frege](https://en.wikipedia.org/wiki/Gottlob_Frege), [Albert Einstein](https://en.wikipedia.org/wiki/Albert_Einstein), [Willard van Orman Quine](https://en.wikipedia.org/wiki/Willard_Van_Orman_Quine) and countless others.
