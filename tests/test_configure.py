import muuusiiik.util as msk
from   pytest import raises

def test_save_and_load_configure_by_dict():
    conf = {'module': 'configure',
            'checklist': ['save', 'load']
           }
    path = 'tests/_config/demo.conf'
    msk.configure.save(conf, path)
    # the conf fire exist
    result = msk.data.exist(path)
    assert result == True
    # assertation
    loaded_conf = msk.configure.load(path)
    assert loaded_conf == conf
    # remove the demo folder
    fd, fn = msk.data.path_split(path)
    msk.data.rm(fd)
    result = msk.data.exist(path)
    assert result == False


def test_save_and_load_configure_by_plain_text():
    conf = """
    module: configure
    checklist:
    - save
    - load
    """
    path = 'tests/_config/demo.conf'
    msk.data.save(conf, path)
    # the conf fire exist
    result = msk.data.exist(path)
    assert result == True
    # assertation
    loaded_conf = msk.configure.load(path)
    assert loaded_conf['module'   ] == 'configure'
    assert loaded_conf['checklist'] == ['save', 'load']
    # remove the demo folder
    fd, fn = msk.data.path_split(path)
    msk.data.rm(fd)
    result = msk.data.exist(path)
    assert result == False


def test_load_non_existing_configure_file():
    path = 'tests/_config/non_existing.conf'
    with raises(FileNotFoundError):
        loaded_conf = msk.configure.load(path)


def test_load_none_configure_file():
    path = None
    with raises(TypeError):
        loaded_conf = msk.configure.load(path)
