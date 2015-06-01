
def split_string(string, separator=None):
    if separator is None:
        separator = '/'
    return string.split(separator)


class FilterModule(object):
    ''' A filter to split a string into a list. '''
    def filters(self):
        return {
            'split': split_string,
        }
