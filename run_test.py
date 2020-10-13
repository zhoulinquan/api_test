import time,sys
from HTMLTestRunner import HTMLTestRunner
import unittest

test_dir = 'F:\\test\\test2'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test2_*.py')

if __name__ == "__main__":
     now = time.strftime("%Y-%m-%d %H-%M-%S")
     filename = "F:\\test\\test2" + now +'_result.html'
     fp = open(filename,'wb')
     runner = HTMLTestRunner(
         stream=fp,
         title='Guest manage',
         description='Implementation Example with:'
     )
     runner.run(discover)
     fp.close()