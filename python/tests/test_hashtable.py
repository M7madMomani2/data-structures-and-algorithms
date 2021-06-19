from data_structures.hashtable.hashtable import Hashtable,LinkedList

def test_hashtable():
    hash_op = Hashtable()
    hash_op.add('test',30)
    actual = hash_op.get('test')
    assert actual== 30

def test_hashtable_not_exist():
    hash_op = Hashtable()
    actual2 = hash_op.get('test2')
    assert actual2 =='key not exist'

def test_hashtable_contains():
    hash_op = Hashtable()
    hash_op.add('test',30)
    actual = hash_op.contains('test')
    assert actual== True

def test_hashtable_hash():
    hash_op = Hashtable()
    hash_op.add('test',30)
    actual = hash_op.hash('test')
    assert actual== 320
