class Logger:

    def __init__(self):
        self.logger=dict()
        
        
        

    def shouldPrintMessage(self, timestamp, message):
        if (message not in self.logger):
            self.logger.update({message:timestamp})
            return True
            print(self.logger)
        if (timestamp-self.logger[message]>=10):
            self.logger.update({message:timestamp})
            return True
        else:
            return False
                  
            
            
        
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)