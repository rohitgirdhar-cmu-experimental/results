import sys
sys.path.append('/home/rohytg/Software/PyHTMLWriter/src');
from Table import Table
from TableWriter import TableWriter

t = Table()
t.readFromCSV('table.csv', scale=1)
tw = TableWriter(t, 'out', makeChart = True, transposeTableForChart=True, rowsPerPage=50, desc='DCG/10 scores for each class')
tw.write()

