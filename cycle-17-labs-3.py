#author CJP 4/12/2022
class tv_remote:  
    # define class
    def __init__(self, channel=0, volume_level=0, on=False):  
        #base value for tv
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
    def __str__(self): 
        # tv on
        if self.on == True:
            return "You are watching channel {0} at volume {1}.".format(self.channel, self.volume_level) # str format for print
        else:   
            #tv off
            return "The TV is off."

my_remote = tv_remote()
my_remote.on = True
print(my_remote)