CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    index_channel = 0
    def __init__(self, channels):
        self.channels = channels

    def first_channel(self):            #turns on the first channel from the list.
        self.index_channel = 0
        return self.channels[self.index_channel]

    def last_channel(self):             #turns on the last channel from the list.
        self.index_channel = len(self.channels) - 1
        return self.channels[self.index_channel]

    def turn_channel(self, N):            #turns on the N channel.
        self.index_channel = N - 1
        return self.channels[self.index_channel]           #Pay attention that the channel numbers start from 1, not from 0.

    def next_channel(self):         #turns on the next channel. If the current channel is the last one, turns on the first channel.
        self.index_channel += 1
        if self.index_channel == len(self.channels):
            index_channel = 0
        return self.channels[self.index_channel]

    def previous_channel(self):         #turns on the previous channel. If the current channel is the first one, turns on the last channel.
        self.index_channel -= 1
        if self.index_channel < 0:
            self.index_channel = len(self.channels) - 1
        return self.channels[self.index_channel]

    def current_channel(self):          #returns the name of the current channel.
        return self.channels[self.index_channel]

    def exists(self, name):           #gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
        try:
            if isinstance(name, int):
                if len(self.channels) <= int(name) or int(name) < 0:
                    return "No"
                else:
                    return "Yes"
            else:
                if name in self.channels:
                    return "Yes"
                else:
                    return "No"
        except ValueError:
            print('Was entered an invalid character')

controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"

assert controller.last_channel() == "TV1000"

assert controller.turn_channel(1) == "BBC"

assert controller.next_channel() == "Discovery"

assert controller.previous_channel() == "BBC"

assert controller.current_channel() == "BBC"

assert controller.exists(4) == "No"

assert controller.exists("BBC") == "Yes"
