import hashlib
import zlib
import urllib
import pickle
import base64

class EncodeDecodeURL():
    def __init__(self,url):
        self.url = url
    
    def encode(self):
        my_url = base64.b64encode(self.url.encode('ascii')) # byte string
        my_hash = hashlib.md5(my_url).hexdigest()[:12] # string
        return str(my_url.decode("utf-8"))+'/'+str(my_hash)
    
    def decode(self):
        url = self.url[:len(self.url)-13].encode('ascii')
        hsh = self.url[len(self.url)-12:] 
        gen_hash =  hashlib.md5(url).hexdigest()[:12]
        if(gen_hash != hsh):
            return "Error"
        normal_url = base64.b64decode(url)

        return str(normal_url.decode('utf-8'))