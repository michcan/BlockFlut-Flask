# -*- coding: utf-8 -*-
from pyo import *
import random

s = Server(duplex=0,audio="jack").boot()
s.setJackAuto(False, False)
s.start()
s.amp=1

silenceTable = LinTable([(0,0),(8191,0)])
presquareTable = SquareTable(15).normalize()
presawTable = SawTable(15).normalize()
sawTable = DataTable(size=8191)
squareTable = DataTable(size=8191)
scale1 = TableScale(presawTable, sawTable, mul=0.08)
scale2 = TableScale(presquareTable, squareTable, mul=0.08)
sinTable = HarmTable([0.08])

try:
  step.destroy()#libère les ressources
  del step#détruit l'instance
except:
  pass

code1="""
class Steps():
  def __init__(self):
    self.seqTable=[]
    self.oscTable=[None]*10 #tableau initialisé avec 10 emplacements vides
    self.seqTable.append(TrigFunc(Seq(time=0.001,seq=[500,500]).play(),self.loop0))
    #self.seqTable.append(TrigFunc(Seq(time=0.001,seq=[200,200,300]).play(),self.loop1))

  def destroy(self):
    #on vide les tableaux
    del self.seqTable[:]
    del self.oscTable[:]

  def loop0(self):
    if self.oscTable[1]==None:
      self.oscTable[1]=Osc(sinTable).out()
    self.oscTable[1].freq=random.randint(400,800)
    
  def __del__(self):
    print "poubelle"
"""

#step=Steps()#instance de l'objet

"""
step=Steps()#instance de l'objet
step.destroy()#libère les ressources
del step#détruit l'instance
"""
