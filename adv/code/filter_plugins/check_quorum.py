
def check_quorum(groups):
    nodes = []
    quorum = False
    for i in groups:
        nodes.append(i)
        if len(nodes) >= 5:
            quorum = True

    return quorum


class FilterModule(object):
    ''' A filter to get minimum servers amount to have quorum '''
    def filters(self):
        return {
            'check_quorum': check_quorum,
        }
