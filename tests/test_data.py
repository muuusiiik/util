import muuusiiik.util as msk
import os

from   pytest import raises


# -----------------------------
# MOCK :: CREATE & REMOVE FILE
# -----------------------------
class Mock:
    def make_sure_there_is_a_file(file_name:str):
        fd, fn = msk.data.path_split(file_name)
        msk.data.make_path(fd)
        msk.data.save('', file_name)

    def make_sure_the_folder_removed(path:str):
        msk.data.rm(path)

    def make_a_new_folder_with_3_files_1_folder_inside(folder, fname):
        # mock a new folder with 3 files and 1 folder inside
        file_name = f'{folder}/{fname}'
        for i in range(3): Mock.make_sure_there_is_a_file(f'{file_name}_{i:02}.txt')
        msk.data.make_path(f'{folder}/not_exist_folder', pathtype='folder')



# -----------------------------
# FILE PATH SPLIT 
# -----------------------------
def test_path_split_on_folder_path():
    file_name = '/some/folder_path/'
    fd, fn    = msk.data.path_split(file_name)
    assert (fd, fn) == ('/some/folder_path', '')
    

def test_path_split_on_file_path():
    file_name = '/some/folder_path/file_name.txt'
    fd, fn    = msk.data.path_split(file_name)
    assert (fd, fn) == ('/some/folder_path', 'file_name.txt')
    

def test_path_split_on_current_folder():
    # current path with filename
    file_name = 'file_name.txt'
    fd, fn    = msk.data.path_split(file_name)
    assert (fd, fn) == ('.', 'file_name.txt')

    # nothing in the path
    file_name = ''
    fd, fn    = msk.data.path_split(file_name)
    assert (fd, fn) == ('.', '')

    # current path is .
    file_name = '.'
    fd, fn    = msk.data.path_split(file_name)
    assert (fd, fn) == ('.', '')

    # file_name is single letter
    file_name = 'x'
    fd, fn    = msk.data.path_split(file_name)
    assert (fd, fn) == ('.', 'x')


def test_path_split_raise_attribute_error():
    with raises(AttributeError):
        filename = 1
        p, f     = msk.data.path_split(filename)


# -----------------------------
# CHECK TYPE OF FILE & FOLDER 
# -----------------------------
def test_path_type_is_file_when_give_file_path():
    path   = 'tests/test_data.py'
    result = msk.data.path_type(path)
    assert result == 'file'


def test_path_type_is_folder_when_give_folder_path():
    # with out slash
    path   = 'tests'
    result = msk.data.path_type(path)
    assert result == 'folder'

    # with slash
    path   = 'tests/'
    result = msk.data.path_type(path)
    assert result == 'folder'


def test_path_type_is_current_dir_represented_with_special_char():
    # path is dot
    path   = '.'
    result = msk.data.path_type(path)
    assert result == 'folder'

    # path is empty string
    path   = ''
    result = msk.data.path_type(path)
    assert result == 'folder'


def test_path_type_is_none_when_give_non_existing_path():
    path   = 'tests/non_existing_file.txt'
    result = msk.data.path_type(path)
    assert result == None


# -----------------------------
# CHECK IF FILE & FOLDER EXIST
# -----------------------------
def test_there_is_existing_file():
    file_name = 'tests/test_data.py'
    result    = msk.data.exist(file_name)
    assert result == True


def test_there_is_existing_file_without_folder_path():
    file_name = 'README.md'
    result    = msk.data.exist(file_name)
    assert result == True


def test_there_is_not_existing_file():
    file_name = 'tests/non_existing_file.py'
    result    = msk.data.exist(file_name)
    assert result == False


def test_there_is_existing_folder():
    # without slash
    folder_name = 'tests'
    result      = msk.data.exist(folder_name)
    assert result == True

    # with slash
    folder_name = 'tests/'
    result      = msk.data.exist(folder_name)
    assert result == True


def test_exist_current_folder_with_special_char():
    # current folder is dot
    folder_name = '.'
    result      = msk.data.exist(folder_name)
    assert result == True

    # current folder is empty string
    folder_name = ''
    result      = msk.data.exist(folder_name)
    assert result == True


def test_there_is_no_exising_folder():
    folder_name = 'not_existing_tests/'
    result      = msk.data.exist(folder_name)
    assert result == False


def test_raise_type_error_for_incorrect_path_type():
    with raises(TypeError):
        folder_name = 'not_existing_tests/'
        result      = msk.data.exist(folder_name, pathtype='document')


# -----------------------------
# LS A SPECIFIC PATH
# -----------------------------
def test_list_contents_in_a_given_folder_in_list_format():
    # mock a new folder with 3 files and 1 folder inside
    file_name = 'tests/_data/some_file'
    fd, fn    = msk.data.path_split(file_name)
    Mock.make_a_new_folder_with_3_files_1_folder_inside(fd, fn)

    # check ontents in given folder
    result    = msk.data.ls(fd)
    assert len(result) == 4
    assert ('not_exist_folder/' in result) == True
    assert ('some_file_00.txt'  in result) == True
    assert ('some_file_01.txt'  in result) == True
    assert ('some_file_02.txt'  in result) == True
    assert ('some_file_03.txt'  in result) == False

    # remove the folder
    Mock.make_sure_the_folder_removed(fd)
    assert msk.data.exist(fd) == False


def test_list_contents_in_a_given_folder_in_dict_format():
    # mock a new folder with 3 files and 1 folder inside
    file_name = 'tests/_data/some_file'
    fd, fn    = msk.data.path_split(file_name)
    Mock.make_a_new_folder_with_3_files_1_folder_inside(fd, fn)

    # check ontents in given folder
    result    = msk.data.ls(fd, fmt='dict')
    assert len(result) == 2
    assert len(result['folder']) == 1
    assert len(result['file'  ]) == 3
    assert ('not_exist_folder' in result['folder']) == True
    assert ('some_file_00.txt' in result['file'  ]) == True
    assert ('some_file_01.txt' in result['file'  ]) == True
    assert ('some_file_02.txt' in result['file'  ]) == True
    assert ('some_file_03.txt' in result['file'  ]) == False

    # remove the folder
    Mock.make_sure_the_folder_removed(fd)
    assert msk.data.exist(fd) == False


def test_list_contents_in_current_folder_with_special_char():
    path   = '.'
    result = msk.data.ls(path)
    assert ('README.md' in result)         == True
    assert ('not_existing_file' in result) == False

    path   = ''
    result = msk.data.ls(path)
    assert ('README.md' in result)         == True
    assert ('not_existing_file' in result) == False


def test_list_contents_in_a_non_existing_folder():
    path   = 'non_existing_path'
    with raises(FileNotFoundError):
        result = msk.data.ls(path)


def test_list_conents_in_a_path_the_same_as_file_name():
    path   = 'tests/test_data.py'
    with raises(NotADirectoryError):
        result = msk.data.ls(path)


# -----------------------------
# REMOVE FILE & FOLDER
# -----------------------------
def test_remove_a_file():
    # mock content 
    file_name = 'tests/_data/some_file'
    fd, fn    = msk.data.path_split(file_name)
    Mock.make_a_new_folder_with_3_files_1_folder_inside(fd, fn)

    # the mocked contents have 3 files and 1 folder
    ls_list   = msk.data.ls(fd)
    assert len(ls_list) == 4

    # remove file 01
    f         = f'{file_name}_01.txt'
    result    = msk.data.rm(f)
    ls_list   = msk.data.ls(fd)
    assert result         == True
    assert len(ls_list)   == 3
    assert (f in ls_list) == False

    # reset to zero
    Mock.make_sure_the_folder_removed(fd)
    assert msk.data.exist(fd) == False


def test_remove_a_folder():
    # mock content 
    file_name = 'tests/_data/some_file'
    fd, fn    = msk.data.path_split(file_name)
    Mock.make_a_new_folder_with_3_files_1_folder_inside(fd, fn)

    # remove tests/_data/
    result    = msk.data.rm(fd)
    assert result == True

    # folder tests/_data/ does not exist anymore in tests/
    ls_list   = msk.data.ls('tests')
    assert (fd in ls_list) == False


def test_remove_a_non_existing_file():
    file_name = 'tests/non_existing_file.txt'
    result    = msk.data.rm(file_name)
    assert result == False


def test_remove_a_non_existing_folder():
    folder_path = 'tests/non_existing_folder/'
    result      = msk.data.rm(folder_path)
    assert result == False


# -----------------------------
# MAKE PATH
# -----------------------------
def _make_sure_remove_temp_folder_and_its_files(file_name:str) -> None:
    folder, fname = msk.data.path_split(file_name)



def _test_make_path_of_non_existing_folder():
    file_name     = 'tests/_data/candel.txt'

    _make_sure_remove_temp_folder_and_its_files(file_name)
    msk.data.make_path(file_name)
    assert msk.data.exist(file_name) == False


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




