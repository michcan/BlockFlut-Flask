// If any new block imports any library, add that library name here.
Blockly.Python.addReservedWords('pyo');

Blockly.Python['moncustom'] = function(block) {
  var value_name = Blockly.Python.valueToCode(block, 'NAME', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var code = 'trala\n'+value_name;
  return code;
};

Blockly.Python['pitchtofrequ'] = function(block) {
  var value_name = Blockly.Python.valueToCode(block, 'NAME', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var code = "(2**((("+value_name+"*1.0)-69)/12))*440";
  //var code = (value_name-69);
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['attendre'] = function(block) {
  var value_duree = Blockly.Python.valueToCode(block, 'duree', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var code = 'pass \n';
  return code;
};

Blockly.Python['hz'] = function(block) {
  var value_synthid = Blockly.Python.valueToCode(block, 'synthID', Blockly.Python.ORDER_ATOMIC);
  var value_frequ = Blockly.Python.valueToCode(block, 'frequ', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var code = 
  'if self.oscTable['+value_synthid+']==None: \n'
  +'  self.oscTable['+value_synthid+']=Osc(sinTable).out() \n' 
  +'  self.oscTable['+value_synthid+'].ramp=SigTo(value=0.5,time=0.1) \n'
  +'  self.oscTable['+value_synthid+'].mul=self.oscTable['+value_synthid+'].ramp \n'
  +'self.oscTable['+value_synthid+'].freq='+value_frequ+" \n";
  return code;
};

Blockly.Python['vol'] = function(block) {
  var value_synthid = Blockly.Python.valueToCode(block, 'synthID', Blockly.Python.ORDER_ATOMIC);
  var value_vol = Blockly.Python.valueToCode(block, 'vol', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var code = 
  'if self.oscTable['+value_synthid+']==None: \n'
  +'  self.oscTable['+value_synthid+']=Osc(sinTable).out() \n' 
  +'  self.oscTable['+value_synthid+'].ramp=SigTo(value=0.5,time=0.1) \n'
  +'  self.oscTable['+value_synthid+'].mul=self.oscTable['+value_synthid+'].ramp \n'
  +'self.oscTable['+value_synthid+'].ramp.value='+value_vol+' \n';
  return code;
};

Blockly.Python['formeonde'] = function(block) {
  var value_synthid = Blockly.Python.valueToCode(block, 'synthID', Blockly.Python.ORDER_ATOMIC);
  var dropdown_forme = block.getFieldValue('forme');
  // TODO: Assemble Python into code variable.
  var code = 
  'if self.oscTable['+value_synthid+']==None: \n'
  +'  self.oscTable['+value_synthid+']=Osc(sinTable).out() \n'
  +'  self.oscTable['+value_synthid+'].ramp=SigTo(value=0.5,time=0.1) \n'
  +'  self.oscTable['+value_synthid+'].mul=self.oscTable['+value_synthid+'].ramp \n';
  if (dropdown_forme=="sin"){
	  code += 'self.oscTable['+value_synthid+'].setTable(sinTable) \n';
  }
  if (dropdown_forme=="square"){
	  code += 'self.oscTable['+value_synthid+'].setTable(squareTable) \n';
  }
  if (dropdown_forme=="scie"){
	  code += 'self.oscTable['+value_synthid+'].setTable(sawTable) \n';
  }
  return code;
};

Blockly.Python['boucle_inf'] = function(block) {
  var statements_sequence_boucle = Blockly.Python.statementToCode(block, 'sequence_boucle');
  // TODO: Assemble Python into code variable.
  statements_sequence_boucle = Blockly.Python.addLoopTrap(statements_sequence_boucle, block.id) || Blockly.Python.PASS;
  var code = statements_sequence_boucle;
  return code;
};
