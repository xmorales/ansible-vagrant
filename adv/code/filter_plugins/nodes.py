
def nodes(groups):
    nodes = []
    result = []
    for i in groups:
        nodes.append(i)
        result = ' '.join(nodes)
    return result


class FilterModule(object):
    ''' A filter to get hosts by space sepparated '''
    def filters(self):
        return {
            'nodes': nodes,
        }
