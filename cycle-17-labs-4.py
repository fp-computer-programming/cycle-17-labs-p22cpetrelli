#author CJP 4/12/2022
class tv_remote:

    #all values for remote 
    def __init__(self, channel=0, volume_level=0, on=False):
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
    #tells user what channel tv is on    
    def __str__(self):
        if self.on == True:
            return "You are watching channel {0} at {1} volume.".format(self.channel, self.volume_level)
        else:
            return "The TV is off."

    def turn_on(self):
        self.on = True
    
    def turn_off(self):
        self.on = False
    
    def volume_up(self, value):
        self.volume_level += value
    
    def volume_down(self, value):
        self.volume_level -= value
    
    def channel_up(self, value):
        self.channel += value
    
    def channel_down(self, value):
        self.channel -= value
    
my_remote = tv_remote()
my_remote.on = True
my_remote.turn_on()
my_remote.turn_off()
my_remote.turn_on()
my_remote.volume_up(16)
my_remote.volume_up(28)
my_remote.channel_up(38)
my_remote.volume_down(23)
my_remote.channel_down(5)
my_remote.turn_off()
print(my_remote)