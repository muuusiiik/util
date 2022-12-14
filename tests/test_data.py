import muuusiiik.util as msk
import os

from   pytest import raises


# -----------------------------
# FILE PATH SPLIT 
# -----------------------------
def test_path_split_on_folder_path():
    filename = '/some/folder_path/'
    p, f     = msk.data.path_split(filename)
    assert p == '/some/folder_path'
    assert f == ''
    

def test_path_split_on_file_path():
    filename = '/some/folder_path/file_name.txt'
    p, f     = msk.data.path_split(filename)
    assert p == '/some/folder_path'
    assert f == 'file_name.txt'
    

def test_path_split_on_current_folder():
    filename = 'file_name.txt'
    p, f     = msk.data.path_split(filename)
    assert p == '.'
    assert f == 'file_name.txt'


def test_path_split_raise_attribute_error():
    with raises(AttributeError):
        filename = 1
        p, f     = msk.data.path_split(filename)


# -----------------------------
# CHECK IF FILE & FOLDER EXIST
# -----------------------------
def test_there_is_existing_file():
    file_name = 'tests/test_data.py'
    result    = msk.data.exist(file_name)
    assert result == True


def test_there_is_not_existing_file():
    file_name = 'tests/non_existing_file.py'
    result    = msk.data.exist(file_name)
    assert result == False


def test_there_is_existing_folder():
    folder_name = 'tests'
    result      = msk.data.exist(folder_name)
    assert result == True


def test_there_is_existing_folder_with_slash():
    folder_name = 'tests/'
    result      = msk.data.exist(folder_name)
    assert result == True


def test_there_is_not_exising_folder():
    folder_name = 'not_existing_tests/'
    result      = msk.data.exist(folder_name)
    assert result == False


def test_raise_type_error_for_incorrect_path_type():
    with raises(TypeError):
        folder_name = 'not_existing_tests/'
        result      = msk.data.exist(folder_name, pathtype='document')


# -----------------------------
# MAKE PATH
# -----------------------------



# -----------------------------
# LS
# -----------------------------
def ttest_ls_given_folder():
    path      = 'tests'
    this_file = 'test_data.py'
    elements = msk.data.ls(path)
    assert (f'{path}/{this_file}' in elements ) == True


def ttest_ls_given_folder_make_sure_robust_with_slash():
    path      = 'tests/'
    this_file = 'test_data.py'
    elements  = msk.data.ls(path)
    p, f      = msk.data.path_split(path)
    assert (f'{path}/{this_file}' in elements ) == True


def ttest_ls_some_existing_folder():
    ...


def ttest_ls_non_existing_folder():
    ...


# -----------------------------
# MAKE 
# -----------------------------
def ttest_make_path_from_not_existing_folder():
    ...


def ttest_there_is_no_existing_folder():
    ...




