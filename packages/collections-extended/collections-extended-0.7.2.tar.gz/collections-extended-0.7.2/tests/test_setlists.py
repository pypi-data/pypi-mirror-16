"""Test for setlist classes."""
import pytest

from collections_extended.setlists import setlist, frozensetlist


def test_count():
	"""Test count."""
	sl = setlist('abcdea')
	assert sl.count('a') == 1
	assert sl.count('f') == 0
	assert sl.count('e') == 1


def test_index():
	"""Test index."""
	sl = setlist('abcdef')
	assert sl.index('a') == 0
	assert sl.index('f') == 5
	with pytest.raises(ValueError):
		sl.index('g')
	with pytest.raises(ValueError):
		sl.index('a', start=1)
	with pytest.raises(ValueError):
		sl.index('f', end=5)
	with pytest.raises(ValueError):
		sl.index('f', end=-1)


def test_sub_index():
	"""Test sub_index."""
	sl = setlist('abcdef')
	assert sl.sub_index('ef') == 4
	with pytest.raises(ValueError):
		sl.sub_index('cb')
	with pytest.raises(ValueError):
		sl.sub_index('efg')
	with pytest.raises(TypeError):
		sl.sub_index(1)
	with pytest.raises(ValueError):
		sl.sub_index('ef', end=5)
	with pytest.raises(ValueError):
		sl.sub_index('ab', start=1)


def test_setlist():
	"""General setlist tests."""
	sl = setlist('abcde')
	sl[0] = 5
	assert sl == setlist((5, 'b', 'c', 'd', 'e'))
	sl[-1] = 0
	assert sl == setlist((5, 'b', 'c', 'd', 0))
	with pytest.raises(ValueError):
		sl[1] = 'c'
	assert sl == setlist((5, 'b', 'c', 'd', 0))
	with pytest.raises(ValueError):
		sl.append('c')
	assert sl == setlist((5, 'b', 'c', 'd', 0))
	sl[2] == 'c'
	assert sl == setlist((5, 'b', 'c', 'd', 0))
	assert sl == setlist((5, 'b', 'c', 'd', 0))
	del sl[0]
	assert sl == setlist(('b', 'c', 'd', 0))
	del sl[-1]
	assert sl == setlist(('b', 'c', 'd'))
	assert sl.pop() == 'd'
	assert sl.pop(0) == 'b'
	assert sl == setlist(('c',))
	sl.insert(0, 'a')
	assert sl == setlist(('a', 'c'))
	sl.insert(len(sl), 'e')
	assert sl == setlist(('a', 'c', 'e'))
	with pytest.raises(ValueError):
		sl.insert(1, 'e')
	sl.append('f')
	assert sl == setlist(('a', 'c', 'e', 'f'))
	sl += ('g', 'h')
	assert sl == setlist(('a', 'c', 'e', 'f', 'g', 'h'))


def test_removeall():
	"""Test remove_all & discard_all."""
	sl = setlist('abcdefgh')
	sl.remove_all(set('acdh'))
	assert sl == setlist(('befg'))
	with pytest.raises(ValueError):
		sl.remove('k')
	with pytest.raises(ValueError):
		sl.remove('bb')


def test_len():
	"""Test __len__."""
	assert len(setlist()) == 0
	assert len(setlist('a')) == 1
	assert len(setlist('ab')) == 2
	assert len(setlist('abc')) == 3


def test_shuffle():
	"""Test shuffle."""
	sl = setlist(range(100))
	sl.shuffle()
	assert sl != setlist(range(100))


def test_del():
	"""Test __delitem__."""
	sl = setlist('abcde')
	del sl[1]
	assert sl == setlist('acde')
	del sl[0]
	assert sl == setlist('cde')
	del sl[2]
	assert sl == setlist('cd')
	with pytest.raises(IndexError):
		del sl[2]
	with pytest.raises(IndexError):
		del sl[-3]


def test_getitem():
	"""Test __getitem__."""
	sl = setlist(range(10))
	assert sl[0] == 0
	assert sl[5] == 5
	assert sl[9] == 9
	with pytest.raises(IndexError):
		sl[10]
	assert sl[-1] == 9
	with pytest.raises(IndexError):
		sl[-11]
	assert sl[1:3] == setlist([1, 2])
	assert sl[1:6:2] == setlist([1, 3, 5])
	assert sl[6:1:-2] == setlist([6, 4, 2])


def test_setitem():
	"""Test __setitem__."""
	def compare_set_slice_to_list(slice_, replacement):
		sl = setlist(range(10))
		sl[slice_] = replacement
		l = list(range(10))
		l[slice_] = replacement
		assert sl == setlist(l)
	sl = setlist('abc')
	sl[0] = 'd'
	assert sl == setlist('dbc')
	sl[0] = 'd'
	assert sl == setlist('dbc')
	sl[1] = 'e'
	assert sl == setlist('dec')
	sl[2] = 'f'
	assert sl == setlist('def')
	with pytest.raises(IndexError):
		sl[3] = 'g'
	sl[0], sl[1] = 'h', 'i'
	assert sl == setlist('hif')
	sl = setlist(range(10))
	sl[0] = 'a'
	assert sl == setlist(['a'] + list(range(1, 10)))
	sl[9] = 'b'
	assert sl == setlist(['a'] + list(range(1, 9)) + ['b'])
	sl[-1] = 'c'
	assert sl == setlist(['a'] + list(range(1, 9)) + ['c'])
	with pytest.raises(IndexError):
		sl[-11] = 'd'
	assert sl == setlist(['a'] + list(range(1, 9)) + ['c'])
	with pytest.raises(IndexError):
		sl[10] = 'd'
	assert sl == setlist(['a'] + list(range(1, 9)) + ['c'])
	compare_set_slice_to_list(slice(0, 2), ['a', 'b'])
	compare_set_slice_to_list(slice(2, 4), ['a', 'b'])
	compare_set_slice_to_list(slice(7, 9), ['a', 'b'])
	compare_set_slice_to_list(slice(2, -2), ['a', 'b'])
	compare_set_slice_to_list(slice(2, 5, 2), ['a', 'b'])
	compare_set_slice_to_list(slice(-1, None, -1), list(range(10)))
	with pytest.raises(TypeError):
		sl[0:2] = 1
	sl = setlist(range(10))
	with pytest.raises(ValueError):
		sl[0:2] = [8, 9]
	with pytest.raises(ValueError):
		sl[-1:0:-2] = ['a', 'b']


def test_delitem():
	"""Test __delitem__."""
	sl = setlist(range(10))
	del sl[9]
	assert sl == setlist(range(9))
	del sl[-1]
	assert sl == setlist(range(8))
	del sl[0]
	assert sl == setlist(range(1, 8))
	with pytest.raises(IndexError):
		del sl[10]

	def compare_del_slice_to_list(slice_):
		sl = setlist(range(10))
		del sl[slice_]
		l = list(range(10))
		del l[slice_]
		assert sl == setlist(l)
	compare_del_slice_to_list(slice(0, 2))
	compare_del_slice_to_list(slice(6, 9))
	compare_del_slice_to_list(slice(3, 7))
	compare_del_slice_to_list(slice(7, 3, -1))
	compare_del_slice_to_list(slice(0, 7, 2))


def test_extend():
	"""Test extend."""
	sl = setlist(range(10))
	sl.extend([10, 11])
	assert sl == setlist(range(12))
	with pytest.raises(ValueError):
		sl.extend([1, 2])
	assert sl == setlist(range(12))
	with pytest.raises(ValueError):
		sl.extend([13, 2])
	assert sl == setlist(range(12))


def test_hash():
	"""Test __hash__."""
	assert hash(frozensetlist('abc')) == hash(frozensetlist('abc'))
	assert hash(frozensetlist()) == hash(frozensetlist())


def test_clear():
	"""Test clear."""
	sl = setlist(range(10))
	sl.clear()
	assert sl == setlist()


def test_discard():
	"""Test discard."""
	sl = setlist(range(10))
	sl.discard(9)
	assert sl == setlist(range(9))
	sl.discard(100)
	assert sl == setlist(range(9))


def test_add():
	"""Test add."""
	sl = setlist(range(10))
	sl.add(10)
	assert sl == setlist(range(11))
	sl.add(10)
	assert sl == setlist(range(11))


def test_remove():
	"""Test remove."""
	sl = setlist(range(10))
	sl.remove(9)
	assert sl == setlist(range(9))
	with pytest.raises(ValueError):
		sl.remove(100)


def test_eq():
	"""Test __eq__."""
	assert not setlist(range(10)) == list(range(10))
	assert not setlist(range(10)) == setlist(range(9))


def test_str():
	"""Test __str__."""
	assert str(setlist()) == str(list())
	assert str(setlist('abc')) == str(list('abc'))


def test_repr():
	"""Test __repr."""
	assert repr(setlist()) == 'setlist()'
	assert repr(setlist(range(4))) == 'setlist((0, 1, 2, 3))'


def test_copy():
	"""Test copy."""
	sl = setlist(range(10))
	copy = sl.copy()
	assert sl == copy
	assert sl is not copy
	sl = setlist(('1', (0, 1)))
	copy = sl.copy()
	assert sl == copy
	assert sl is not copy
	assert sl[1] is copy[1]
