import sys,os
sys.path.append('/home/rohytg/Software/PyHTMLWriter/src');
from Element import Element
from TableRow import TableRow
from Table import Table
from TableWriter import TableWriter

corpus = '../../../dataset/PALn1KHayesDistractors/corpus/'

def formElt(match):
  temp = match.split(':')
  e = Element()
  box = [float(el) for el in temp[1].split(',')]
  e.addImg(os.path.join('..', corpus, temp[0]), bboxes=[box])
  e.addTxt(temp[2])
  return e

t = Table()
r = TableRow(isHeader = True)
r.addElement(Element('Sno'))
r.addElement(Element('Top Patch'))
r.addElement(Element('Retrieval Score'))
r.addElement(Element('Distinct Retrievals...'))
t.addRow(r)
for i in range(1, 120):
  with open('top_patches_text/' + str(i) + '.txt') as f:
    lines = f.read().splitlines()
  for j in range(len(lines)):
    line = lines[j]
    r = TableRow(rno=i + 0.1 * j)
    temp = line.split(';')
    qbox = [float(el) for el in temp[1].split(',')]
    e = Element()
    e.addImg(os.path.join('..', corpus, temp[0]), bboxes=[qbox])
    r.addElement(e)
    r.addElement(Element(temp[2]))
    matches_elts = [formElt(el) for el in temp[3].strip().split(' ')]
    for mel in matches_elts:
      r.addElement(mel)
    t.addRow(r)
tw = TableWriter(t, 'out')
tw.write()

