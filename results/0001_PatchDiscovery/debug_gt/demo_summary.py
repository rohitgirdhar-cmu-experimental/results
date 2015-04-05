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
r.addElement(Element('Top 10 GT Patches (removing small)'))
r.addElement(Element('Top 10 GT Patches (before)'))
r.addElement(Element('Top 10 GT Patches (ratio)'))
t.addRow(r)
for i in range(1, 121):
  r = TableRow(rno=i)
  with open('2_top_patches_text_removedSmall/' + str(i) + '.txt') as f:
    lines = f.read().splitlines()
  boxes = []
  for j in range(min(len(lines), 10)):
    line = lines[j]
    temp = line.split(';')
    qbox = [float(el) for el in temp[1].split(',')]
    boxes.append(qbox)
  with open('top_patches_text/' + str(i) + '.txt') as f:
    lines = f.read().splitlines()
  boxes2 = []
  for j in range(min(len(lines), 10)):
    line = lines[j]
    temp = line.split(';')
    qbox = [float(el) for el in temp[1].split(',')]
    boxes2.append(qbox)
  with open('3_top_patches_text_removedSmallFixed/' + str(i) + '.txt') as f:
    lines = f.read().splitlines()
  boxes3 = []
  for j in range(min(len(lines), 10)):
    line = lines[j]
    temp = line.split(';')
    qbox = [float(el) for el in temp[1].split(',')]
    boxes3.append(qbox)


  e = Element()
  e.addImg(os.path.join('..', corpus, temp[0]), bboxes=boxes)
  r.addElement(e)
  e = Element()
  e.addImg(os.path.join('..', corpus, temp[0]), bboxes=boxes2)
  r.addElement(e)
  e = Element()
  e.addImg(os.path.join('..', corpus, temp[0]), bboxes=boxes3)
  r.addElement(e)

  t.addRow(r)
tw = TableWriter(t, 'out_summary')
tw.write()

