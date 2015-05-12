
def get_slaves(groups):
    slaves = []
    for i in groups:
        slaves.append(i)
    return slaves[1:]


class FilterModule(object):
    ''' A filter to skip first host in group '''
    def filters(self):
        return {
            'get_slaves': get_slaves,
        }
