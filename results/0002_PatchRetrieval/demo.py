import sys
sys.path.append('/home/rohytg/Software/PyHTMLWriter/src');
from Element import Element
from TableRow import TableRow
from Table import Table
from TableWriter import TableWriter

t = Table()
for i in range(121, 125):
  r = TableRow(rno = i + 0.1)
  e = Element()
  e.addImg('../retrievals_vis/rbf_10K/' + str(i) + '/q.jpg')
  r.addElement(e)
  r.addElement(Element('RBF 10K iter'))
  for j in range(1,20):
    e = Element()
    e.addImg('../retrievals_vis/rbf_10K/' + str(i) + '/' + str(j) + '.jpg')
    r.addElement(e)
  t.addRow(r)

tw = TableWriter(t, 'out')
tw.write()

