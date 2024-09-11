import collections
Event = collections.namedtuple('Event', ('start', 'finish'))

events = [
    Event(1, 1.8), Event(1, 1.9), Event(1.85, 2)
]

def find_max_simultaneous_events(events):
    all_times = set([event.start for event in events])

    max_simultaneous_events = 0
    for time in all_times:
        simultaneous_events = len([event for event in events if event.start <= time <= event.finish])
        if simultaneous_events > max_simultaneous_events: 
            max_simultaneous_events = simultaneous_events

    return max_simultaneous_events

print(find_max_simultaneous_events(events))