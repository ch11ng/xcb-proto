#!/usr/bin/python

from xml.sax.saxutils import XMLFilterBase, XMLGenerator
from xml.sax.xmlreader import AttributesImpl
from xml.sax import make_parser
import sys

class AttributesUnion(AttributesImpl):
	def __init__(self, base, **values):
		baseitems = dict(base)
		baseitems.update(values)
		AttributesImpl.__init__(self, baseitems)

class AnnotateSize(XMLFilterBase):
	types = {
		'BYTE': 1,
		'BOOL': 1,
		'CARD8': 1,
		'CARD16': 2,
		'CARD32': 4,
		'INT8': 1,
		'INT16': 2,
		'INT32': 4,
		'float': 4,
		'double': 8,
	}
	header = None
	def setTypeSize(self, name, size):
		self.types[name] = size
		self.types[self.header + ':' + name] = size

	struct = None
	union = None
	def startElement(self, name, attrs):
		if name == 'xcb':
			self.header = attrs['header']
		elif name == 'field':
			size = self.types.get(attrs['type'], 0)
			if self.struct is not None:
				self.totalsize += size
			elif self.union is not None:
				self.totalsize = max(self.totalsize, size)
			attrs = AttributesUnion(attrs, bytes=str(size))
		elif name == 'xidtype':
			self.setTypeSize(attrs['name'], 4)
		elif name == 'typedef':
			self.setTypeSize(attrs['newname'], self.types[attrs['oldname']])
		elif name == 'struct' or name == 'union':
			assert self.struct is None and self.union is None
			setattr(self, name, attrs['name'])
			self.totalsize = 0
		XMLFilterBase.startElement(self, name, attrs)

	def endElement(self, name):
		if name == 'struct' or name == 'union':
			assert getattr(self, name) is not None
			self.setTypeSize(getattr(self, name), self.totalsize)
			setattr(self, name, None)
			del self.totalsize
		XMLFilterBase.endElement(self, name)

annotator = AnnotateSize(make_parser())
annotator.setContentHandler(XMLGenerator())
for f in sys.argv[1:]:
	annotator.parse(f)
