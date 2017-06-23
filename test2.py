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

from numbers import Number

try:
  step.destroy()
  del step
except:
  pass

class Steps():
  def __init__(self):
    self.oscTable=[None]*10
    self.seqTable=[]
    self._C3_A9l_C3_A9ment = 0
    self._C3_A9l_C3_A9ment = 40
    self._C3_A9l_C3_A9ment = (self._C3_A9l_C3_A9ment if isinstance(self._C3_A9l_C3_A9ment, Number) else 0) + 1
    self.count0=0
    self.seqTable.append(TrigFunc(Seq(time=0.001,seq=[500]).play(),self.loop0))

  def destroy(self):
    del self.seqTable[:]
    del self.oscTable[:]

  def loop0(self):
    self.id=0
    if self.count0==0:
      if self.oscTable[1]==None:
        self.oscTable[1]=Osc(sinTable).out()
        self.oscTable[1].ramp=SigTo(value=0.5,time=0.1)
        self.oscTable[1].mul=self.oscTable[1].ramp
      self.oscTable[1].freq=((2**(((self._C3_A9l_C3_A9ment*1.0)-69)/12))*440)
    self.count0+=1
    if self.count0>=len(self.seqTable[0].input.seq):
      self.count0=0

step=Steps()
