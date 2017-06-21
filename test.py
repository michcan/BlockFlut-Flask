# -*- coding: utf-8 -*-
from pyo import *
import time
import signal
import sys
s = Server(duplex=0,audio="jack").boot()
s.setJackAuto(False, False)
s.start()
s.amp=0
time.sleep(0.2)
s.amp=1
def signal_term_handler(signal, frame):
  s.amp=0
  time.sleep(0.1)
  s.shutdown()
  sys.exit(0)
signal.signal(signal.SIGTERM, signal_term_handler)


silenceTable = LinTable([(0,0),(8191,0)])
presquareTable = SquareTable(15).normalize()
presawTable = SawTable(15).normalize()
sawTable = DataTable(size=8191)
squareTable = DataTable(size=8191)
scale1 = TableScale(presawTable, sawTable, mul=0.08)
scale2 = TableScale(presquareTable, squareTable, mul=0.08)
sinTable = HarmTable([0.08])
oscilloList=[None]*10
sampleList=[None]*10
seqList=[]
count=0

class Steps():
  def __init__(self):
    self.seq0=(Seq(time=0.001,seq=[500,500]).play(),0)
    self.tf0=TrigFunc(self.seq0[0],self.loop0)
    self.count0=0

  def loop0(self):
    self.id=0
    if self.count0==0:
      try :
        if oscilloList[1]==None:
          oscilloList.insert(1,Osc(sinTable).out())
          oscilloList[1].ramp=SigTo(value=0.5,time=0.1)
          oscilloList[1].mul=oscilloList[1].ramp
        oscilloList[1].freq=440
      except :
        pass
    if self.count0==1:
      try :
        if oscilloList[1]==None:
          oscilloList.insert(1,Osc(sinTable).out())
          oscilloList[1].ramp=SigTo(value=0.5,time=0.1)
          oscilloList[1].mul=oscilloList[1].ramp
        oscilloList[1].freq=800
      except :
        pass
    self.count0+=1
    if self.count0>=len(self.seq0.seq):
      self.count0=0

step=Steps()
