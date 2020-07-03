"""
Author: Igor
Date: 2020.06.25
This library contains the set of functions that are suitable to object mapping.
"""


def map_object_to_object(source=None, destination=None, suffix_of_destination=None, suffix_of_source=None):
    """
    Maps a source object to a destination object. Both objects should have the same
    attributes. In case if no same attributes is defined then nothing will be mapped.
    """
    for key, value in source.__dict__.items():
        required_value = value
        # For example we want to get values from source:
        #   phone_form.phone.data
        # we define source = phone_form and suffix_of_source='data';
        # so we must follow to the attribute phone_form.phone and
        # then extract phone_form.phone.data
        if suffix_of_source is not None and hasattr(destination, key):
            required_value = getattr(getattr(source, key), suffix_of_source)
        if not str(key).startswith('_'):
            if hasattr(destination, key):
                if suffix_of_destination is None:
                    setattr(destination, key, required_value)
                else:
                    attribute = getattr(destination, key)
                    setattr(attribute, suffix_of_destination, required_value)


def map_object_to_dict(source=None, destination=None, suffix_of_source=None, keys_to_map=None):
    """
    Maps an object with some attributes to a destination dictionary.
    Will only take into account the attributes which names are containing in
    the set, tuple or list of keys_to_map.
    """
    if type(destination) is not dict:
        raise ValueError('Destination should be a dictionary to map object to dict')
    if keys_to_map is None or type(keys_to_map) not in (tuple, list, set):
        raise ValueError('Parameter keys_to_map has to be defined for mapping object to dict '
                         'and has to be list, set or tuple')

    for key, value in source.__dict__.items():
        required_value = value
        if suffix_of_source is not None and key in keys_to_map:
            required_value = getattr(getattr(source, key), suffix_of_source)
        if not str(key).startswith('_'):
            if key in keys_to_map:
                destination[key] = required_value


def map_objects(source=None, destination=None, suffix_of_destination=None, suffix_of_source=None, keys_to_map=None):
    """
    Maps an object to its destination. According to destination type it can do
    a mapping to object with attributes or to a dictionary with keys.
    """
    if source is None:
        raise ValueError('Source object has to be set for mapping')
    if destination is None:
        raise ValueError('Destination object has to be set for mapping')

    if type(destination) is dict and type(source) is not dict:
        map_object_to_dict(source=source,
                           destination=destination,
                           suffix_of_source=suffix_of_source,
                           keys_to_map=keys_to_map)
    elif type(source) is not dict:
        map_object_to_object(source=source,
                             destination=destination,
                             suffix_of_destination=suffix_of_destination,
                             suffix_of_source=suffix_of_source)
    else:
        raise ValueError('Unknown type of source or destination: source - {0}, destination - {1}'.format(str(type(source)), str(type(destination))))
