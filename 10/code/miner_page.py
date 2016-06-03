from miner import MinerClass
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from cStringIO import StringIO
import sys

class Miner_Page(MinerClass):

    def __init__(self,filename,password='',**kw):
        super(Miner_Page,self).__init__(filename,password)
        self.retstr = StringIO()
        self.resources = PDFResourceManager()
        self.device = self.init_device(self.resources,**kw)
        self.interpreter = PDFPageInterpreter(self.resources,self.device)
        

    def init_device(self,resource_manager,**kw):
        codec = 'utf-8'
        laparams = LAParams()
        return TextConverter(resource_manager, self.retstr, codec=codec, laparams=laparams)


    def init_device_agregator(self,resource_manager,**kw):
        laparams = LAParams()
        return PDFPageAggregator(resource_manager, laparams=laparams)


    def page_iter(self):
        for page in PDFPage.get_pages(self.fp, check_extractable=True):
            self.interpreter.process_page(page)
            yield page

if __name__=='__main__':

    with Miner_Page('2.pdf') as miner:
        count = 0
        for page in miner.page_iter():
            count += 1
            print count
            #layout = miner.device.get_result()
            #import pdb; pdb.set_trace()
        str = miner.retstr.getvalue()
        miner.retstr.close()
        f = open('1.txt','w')
        f.write(str)
        f.close()
        print 'Done!'
