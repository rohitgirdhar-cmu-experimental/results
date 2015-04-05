import sys
sys.path.append('/home/rohytg/Software/PyHTMLWriter/src');
from Element import Element
from TableRow import TableRow
from Table import Table
from TableWriter import TableWriter
import os
import numpy as np

def readRetrievals(fpath, DIV = 1):
  f = open(fpath, 'r')
  lines = f.read().splitlines()
  f.close()
  imids = []
  allmatches = []
  for line in lines:
    imgid = int(line.split(';')[0])
    imids.append(imgid)
    matches = line.split(';')[1].strip()
    matches = [(int(m.split(':')[0])/DIV, float(m.split(':')[1]), [int(el) for el in m.split(':')[2].split(',')]) for m in matches.split()]
    allmatches.append(matches)
  return (imids, allmatches)

t = Table()
methods = ['gt.txt', 'full.txt', 'svr_rbf_10000.txt', 'svr_linear_FullData_liblinear_pool5.txt']
imgspath = '../../../dataset/PALn1KHayesDistractors/corpus/'
imgslistpath = '../../../dataset/ImgsList.txt'
selboxpath = 'selsearch_boxes/'

selbox_cache = {}
def readBbox(featid):
  im = featid / 10000 + 1
  if im not in selbox_cache.keys():
    boxes = np.loadtxt(os.path.join(selboxpath, str(im) + '.txt'), delimiter=',')
    selbox_cache[im] = boxes
  else:
    boxes = selbox_cache[im]
  res = boxes[(featid % 10000) - 1]
  return [res[1], res[0], res[3] - res[1], res[2] - res[0]]

f = open(imgslistpath)
imgslist = f.read().splitlines()
f.close()

methodout = []
for method in methods:
  imids, matches = readRetrievals(os.path.join('retrievals', method))
  methodout.append((imids, matches))

for i in range(117):
  print i
  j = 0
  for method in methods:
    imids = methodout[j][0]
    matches = methodout[j][1]
    r = TableRow(rno = i + 0.01 * j)
    e = Element()
    bbox = readBbox(imids[i])
    bboxes = [bbox]
    imname = imgslist[imids[i]/10000]
    if method == 'full.txt':
      bboxes = None
    e.addImg(os.path.join('..', imgspath, imname), bboxes=bboxes)
    parentclass = os.path.dirname(imname)
    r.addElement(e)
    e = Element(method[:-4])
    r.addElement(e)
    for k in range(len(matches[i])):
      e = Element()
      bboxes = []
      for m in matches[i][k][2]:
        bboxes.append(readBbox(m))
      match_imname = imgslist[matches[i][k][0]]
      matchclass = os.path.dirname(match_imname)
      if matchclass == parentclass:
        e.setDrawCheck()
      else:
        e.setDrawUnCheck()
      if method == 'full.txt':
        bboxes = None
      e.addImg(os.path.join('..', imgspath, match_imname), bboxes=bboxes)
      r.addElement(e)
    j += 1
    t.addRow(r)

tw = TableWriter(t, 'out')
tw.write()


