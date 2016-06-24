[![Join the chat at https://gitter.im/omni4d/model](https://badges.gitter.im/omni4d/model.svg)](https://gitter.im/omni4d/model?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# Model

An omni4d model contains signs which refer to objects in the real world. There are 4 basic types of sign:

* Individual - Refers to an object which has constant identity over time

* Class - Refers to a set of objects

* Event - Refers to an object with extension across space at a point in time

* Tuple - Refers to a relationship between multiple objects

Tuple has further subtypes. All Tuple signs must be one of these subtypes rather than the basic type:

* Whole-Part Tuple - Indicating that the second object is part of the first
* Class-Member Tuple - Indicating that the second object is a member of the first
* Ordinary Tuple

Every sign must have a namespaced, unique id and tuples must contain a list of objects to which they refer.

# Work
The intention of this repository is to produce a set of [YAML](https://en.wikipedia.org/wiki/YAML) files which are omni4d models. These can then be used as the basis for further implementations probably involving various database systems and programming languages.

[org.omni4d.core.yaml](https://github.com/omni4d/model/blob/master/fragments/org.omni4d.core.yaml) contains the core model fragment and [org.omni4d.identification.yaml](https://github.com/omni4d/model/blob/master/fragments/org.omni4d.identification.yaml) the fragment describing the identification of individuals.

These two fragments are then used within [org.omni4d.example.yaml](https://github.com/omni4d/model/blob/master/fragments/org.omni4d.example.yaml) to represent the author of this repository.

# Acknowledgments
This work was inspired by the idea of a 4D spatio-temporal object paradigm described by Chris Partridge in his book [Business Objects: Re-Engineering for Re-Use](https://books.google.co.uk/books?id=BIFFAAAAYAAJ).

Those ideas are, in turn, based upon the work of:
* [Aristotle](https://en.wikipedia.org/wiki/Aristotle), the founding father of human attempt to model the world who gave us the 'Substance Paradigm'
* [Georg Cantor](https://en.wikipedia.org/wiki/Georg_Cantor), who gave us Set Thoery
* [Gottlob Frege](https://en.wikipedia.org/wiki/Gottlob_Frege), who used Set Theory to expand Aristotle's work and gave us the 'Logic Paradigm' with its notion of strong reference between signs within a model and real-world objects
* [Albert Einstein](https://en.wikipedia.org/wiki/Albert_Einstein), who realised that time is relative and gave us the 4D notion of spacetime
* [Willard van Orman Quine](https://en.wikipedia.org/wiki/Willard_Van_Orman_Quine), who realised that Einstein's ideas could be used to expand Frege's work and give us the '4D Spatio-Temporal Object Paradigm'

and countless others.
