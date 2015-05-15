
def nodes(groups):
    nodes = []
    result = []
    for i in groups:
        nodes.append(i)
        result = ' '.join(nodes)
    return result


class FilterModule(object):
    ''' A filter to skip first host in group '''
    def filters(self):
        return {
            'nodes': nodes,
        }
