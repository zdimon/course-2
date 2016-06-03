from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed

class MinerClass(object):
    def __init__(self, filename, password=''):
        self.fp = open(filename,'rb')
        self.parser = PDFParser(self.fp)
        self.doc = PDFDocument(self.parser)
        # Check if the document allows text extraction. If not, abort.
        if not self.doc.is_extractable:
            raise PDFTextExtractionNotAllowed

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.doc = None
        self.parser = None
        self.fp.close()
        print 'tear things down'

if __name__=='__main__':

    with MinerClass('1.pdf') as m:
        outlines = m.doc.get_outlines()
        import pdb; pdb.set_trace()
        toc = [(level,title) for (level,title,dest,a,s) in outlines]
        print toc


