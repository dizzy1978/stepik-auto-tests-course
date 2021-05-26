def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"


test_substring('full_string', 'string')







#s = 'My Name is Julia'

#if 'Name' in s:
#    print('Substring found')