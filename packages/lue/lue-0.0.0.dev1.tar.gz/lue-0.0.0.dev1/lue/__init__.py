"""
LUE Python package

Among other things, LUE is the name of an API for performing I/O to the
LUE scientific database. LUE can be used for storing information that
is related to agents (AKA objects, individuals, items), e.g.:

- the location of houses
- GPS tracks of birds
- elevation of a mountain range

The number of agents for which information is stored is at least 1 (e.g.:
a single research area, country, economy, planet) and is at most limited
by the available computing resources.

LUE information is stored in a dataset (see lue.Dataset). Each dataset
contains a collection of universes (lue.Universe) and a collection of
phenomena (lue.Phenomenon). Each universe contains a collection of
phenomena (lue.Phenomenon). Each phenomenon contains a collection of
property sets (lue.PropertySet). Each property set is connected to
a single domain (lue.Domain) and contains a collection of properties
(lue.Property).

For more information about the API, see the help pages of the imported
modules and the various classes, e.g.: help(lue._lue), help(lue.Dataset).
Note that although the documentation mentions the subpackage name
`lue._lue` in various places, the `lue._lue` module should not be used
in code. All high-level symbols are imported in the main `lue` module.
So, use `lue.Dataset` instead of `lue._lue.Dataset`, for example.

For more information about LUE, see the LUE project page:
https://github.com/pcraster/lue
"""
from _lue import *
from describe import describe_dataset


__version__ = "0.0.0.dev1"


def _api(property_set):

    # TODO
    return property_set

    # result = O_O_PropertySet(property_set)

    # return result


def _decorated_add_property_set(
        function):
    def add_property_set(*args, **kwargs):
        return _api(function(*args, **kwargs))

    return add_property_set

Phenomenon.add_property_set = _decorated_add_property_set(
    Phenomenon.add_property_set)


def _decorated__getitem__(
        function):
    def __getitem__(*args, **kwargs):
        return _api(function(*args, **kwargs))

    return __getitem__


PropertySets.__getitem__ = _decorated__getitem__(PropertySets.__getitem__)

Chunks = Shape
