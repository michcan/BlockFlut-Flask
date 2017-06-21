from pyo import *

import time
import signal
import sys

s = Server(duplex=0,audio="jack").boot()
s.setJackAuto(False, False)
s.start()

silenceTable = LinTable([(0,0),(8191,0)])
presquareTable = SquareTable(15).normalize()
presawTable = SawTable(15).normalize()
sawTable = DataTable(size=8191)
squareTable = DataTable(size=8191)
scale1 = TableScale(presawTable, sawTable, mul=0.08)
scale2 = TableScale(presquareTable, squareTable, mul=0.08)
sinTable = HarmTable([0.08])

seqTable=[]
oscTable=[None]*10
oscTable[0]="gagag"

try:
  del seqTable[:]
  del oscTable[:]
  del step
except:
  pass

class Steps():
  def __init__(self):
    seqTable.append(TrigFunc(Seq(time=0.001,seq=[500]).play(),self.loop0))
    self.count0=0

  def loop0(self):
    self.id=0
    global oscTable
    if self.count0==0:
      print oscTable[0]
    self.count0+=1
    if self.count0>=len(seqTable[0].input.seq):
      self.count0=0

step=Steps()
