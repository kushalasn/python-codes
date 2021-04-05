import random
class Codec:
    def __init__(self):
        
       
        self.urls={}
        
    def encode(self,longUrl):
        print(longUrl)
        x=random.randint(0,1000000000)
        if x not in self.urls:
            self.urls[x]=longUrl
        else:
            x=random.randint(0,1000000000)
            self.urls[x]=longUrl
            
        code=''.join(str(x))
        short_url='http://tinyurl.com/'+code
        
            
        
        return short_url
        
        

    def decode(self,short_url):

        
        return self.urls[int(short_url[19:])]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))