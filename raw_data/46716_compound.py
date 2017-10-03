'''
Created on Mar 7, 2011

@author: johnsalvatier
'''


class CompoundStep(object):
    """Step method composed of a list of several other step methods applied in sequence."""

    def __init__(self, methods):
        self.methods = list(methods)
        self.generates_stats = any(method.generates_stats for method in self.methods)
        self.stats_dtypes = []
        for method in self.methods:
            if method.generates_stats:
                self.stats_dtypes.extend(method.stats_dtypes)

    def step(self, point):
        if self.generates_stats:
            states = []
            for method in self.methods:
                if method.generates_stats:
                    point, state = method.step(point)
                    states.extend(state)
                else:
                    point = method.step(point)
            return point, states
        else:
            for method in self.methods:
                point = method.step(point)
            return point

    @property
    def report(self):
        reports = []
        for method in self.methods:
            if hasattr(method, 'report'):
                reports.append(method.report)
        return _CompoundReport(reports)


class _CompoundReport(object):
    def __init__(self, reports):
        self._reports = reports

    def _finalize(self, strace):
        for report in self._reports:
            report._finalize(strace)