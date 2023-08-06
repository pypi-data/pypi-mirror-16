from os import remove

import pytest
from markov.stores import Pickle, Redis


def clear_store(store):
    store.clear()
    return store


@pytest.mark.parametrize('store', [
    clear_store(Pickle('test.pickle')),
    clear_store(Redis(prefix='markovpytest'))
])
def test_stores(store):
    assert store.relation_count('test') == 0
    store.insert('test', 'test2')
    assert len(store) == 1
    assert store.relation_count('test') == 1
    assert 'test' in store
    assert store.next_words('test') == [('test2', 1)]
    store.insert('test', 'test2')
    assert store.next_words('test') == [('test2', 2)]
    store.insert('test', 'test3')
    assert sorted(store.next_words('test')) ==\
        sorted([('test2', 2), ('test3', 1)])


@pytest.fixture
def emptyfile(request):
    path = 'testempty.pickle'
    open(path, 'w')

    def fin():
        remove(path)
    request.addfinalizer(fin)
    return path


def test_pickle(emptyfile):
    Pickle(emptyfile)
