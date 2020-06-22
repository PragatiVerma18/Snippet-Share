from django.test import TestCase
from .EncodeDecodeURL import EncodeDecodeURL
# Create your tests here.
class EncodeDecodeTest(TestCase):
    
    def pass_encode_function(self):
        data = EncodeDecodeURL("hello_world").encode()
        self.assertEqual(data,"aGVsbG9fd29ybGQ=/19a3e3fca4a7")
    
    def pass_decode_function(self):
        data = EncodeDecodeURL("aGVsbG9fd29ybGQ=/19a3e3fca4a7").decode()
        self.assertEqual(data,"hello_world")

    def fail_encode_function(self):
        data = EncodeDecodeURL("hello_world").encode()
        self.assertEqual(data,"aGVsbG9ybGQ=/19a3e3fca4a7")
    
    def fail_decode_function (self):
        data = EncodeDecodeURL("aGVsbG9fd29ybGQ=/19a3e3fca4a7").decode()
        self.assertEqual(data,"hel_world")