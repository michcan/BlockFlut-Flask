# -*- coding: utf-8 -*-
import time
global start
start=time.time()

from pyo import *
print time.time()-start
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
count=0

class Steps():
  def __init__(self):

    self.seq0=Seq(time=0.001,seq=[500,500,500]).play()
    self.tf0=TrigFunc(self.seq0,self.loop0)
    self.count0=0

  def loop0(self):
    self.id=0
    if self.count0==0:
      try :
        if oscilloList[1]==None:
          print time.time()-start
          oscilloList.insert(1,Osc(sinTable).out())
          oscilloList[1].ramp=SigTo(value=0.5,time=0.1)
          oscilloList[1].mul=oscilloList[1].ramp
        oscilloList[1].freq=440
      except :
        pass
    if self.count0==1:
      try :
        if oscilloList[2]==None:
          oscilloList.insert(2,Osc(sinTable).out())
          oscilloList[2].ramp=SigTo(value=0.5,time=0.1)
          oscilloList[2].mul=oscilloList[2].ramp
        oscilloList[2].freq=880
      except :
        pass
    if self.count0==2:
      try :
        if oscilloList[3]==None:
          oscilloList.insert(3,Osc(sinTable).out())
          oscilloList[3].ramp=SigTo(value=0.5,time=0.1)
          oscilloList[3].mul=oscilloList[3].ramp
        oscilloList[3].freq=600
      except :
        pass
    self.count0+=1
    if self.count0>=len(self.seq0.seq):
      self.count0=0

step=Steps()
while True:
    time.sleep(0.1)
