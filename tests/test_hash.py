from   pytest import raises
import muuusiiik.util as msk


def test_hash_string():
    obj    = 'demo text'
    result = msk.hasher.hash(obj)
    assert type(obj) == str
    assert result    == '5c40f9622c9489a25dd71a15374a04fe'


def test_hash_dict():
    obj    = {'type': 'dict', 'value': 'some value'}
    result = msk.hasher.hash(obj)
    assert type(obj) == dict
    assert result    == '2f7a3110878f1c45dcafa9f62b428171'


def test_hash_dict_with_array():
    ...


def test_hash_for_4_digit():
    ...


def test_hash_for_n_digits():
    ...


def test_exception_type_error_when_obj_is_int():
    ...




