import json

from cached_property import cached_property
from dateutil.parser import parse


class Event(object):
    def __init__(self, raw):
        self.raw = raw

    def __iter__(self):
        return iter(self.raw['entries'])

    @cached_property
    def ctime(self):
        """
        Get event's creating time.

        :rtype: datetime.datetime
        """
        return parse(self.raw['dateCreated'])

    @cached_property
    def headers(self):
        """
        Get event's HTTP headers.

        :rtype: dict
        """
        for entry in self:
            if entry['type'] == 'request':
                return dict(entry['data']['headers'])

        return {}

    @cached_property
    def params(self):
        """
        Get event message's parameters.

        :rtype: dict
        """
        for entry in self:
            if entry['type'] == 'message':
                return entry['data']

        return {}

    @cached_property
    def context(self):
        """
        Get event's context.

        :rtype: dict
        """
        context = self.raw['context'].copy()
        context.update(self.raw.get('user', {}))
        return context

    @cached_property
    def frames(self):
        """
        Get event's stack frames.

        :rtype: list
        """
        for entry in self:
            if entry['type'] == 'exception':
                # TODO does `entry['data']['values']` have always 1 element?
                return entry['data']['values'][0]['stacktrace']['frames']

        return []

    @cached_property
    def vars(self):
        """
        Get event's variables from all its stack frames.

        :rtype: set
        """
        values = set()

        for frame in self.frames:
            values |= set(frame.get('vars', []))

        return values

    @cached_property
    def tags(self):
        """
        Get event's tags.

        :rtype: dict
        """
        return {tag['key']: tag['value'] for tag in self.raw['tags']}

    @cached_property
    def breadcrumbs(self):
        """
        Get event's breadcrumbs.

        :rtype: list
        """
        breadcrumbs = []

        for entry in self:
            if entry['type'] == 'breadcrumbs':
                breadcrumbs.extend(entry['data'].get('values', []))

        return breadcrumbs

    def is_breadcrumbs_order_preserved(self, order):
        """
        Check if given breadcrumbs order is preserved.
        :param order: order of categories which should be preserved
        between ones specified in order.
        :type: re.SRE_Pattern
        :rtype: bool
        """
        categories = (breadcrumb['category'] for breadcrumb in self.breadcrumbs)
        categories_str = ' '.join(categories)
        return bool(order.search(categories_str))


def load_from_file(pathname):
    """
    Load events from file.
    :param pathname: path to the file containing events.
    :type: str
    :rtype: list<Event>
    """
    with open(pathname) as f:
        events = json.load(f)

    return [Event(event) for event in events]
