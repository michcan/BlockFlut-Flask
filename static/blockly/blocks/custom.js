Blockly.Blocks['moncustom'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField("valeur");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(290);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['hz'] = {
  init: function() {
    this.appendValueInput("synthID")
        .setCheck("Number")
        .appendField("Mettre le synth n°");
    this.appendValueInput("frequ")
        .setCheck("Number")
        .appendField("à");
    this.appendDummyInput()
        .appendField("Hz");
    this.appendValueInput("durée")
        .setCheck("Number")
        .appendField("pendant");
    this.appendDummyInput()
        .appendField("ms");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(330);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['vol'] = {
  init: function() {
    this.appendValueInput("synthID")
        .setCheck("Number")
        .appendField("Mettre le synth n°");
    this.appendValueInput("vol")
        .setCheck("Number")
        .appendField("à");
    this.appendDummyInput()
        .appendField("dB");
    this.appendValueInput("durée")
        .setCheck("Number")
        .appendField("pendant");
    this.appendDummyInput()
        .appendField("ms");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(330);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['formeonde'] = {
  init: function() {
    this.appendValueInput("synthID")
        .setCheck("Number")
        .appendField("Mettre le synth n°");
    this.appendDummyInput()
        .appendField("en forme d'onde ")
        .appendField(new Blockly.FieldDropdown([["sin", "sin"], ["scie", "scie"], ["square", "square"]]), "forme");
    this.appendValueInput("durée")
        .setCheck("Number")
        .appendField("pendant");
    this.appendDummyInput()
        .appendField("ms");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['pitchtofrequ'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField("Donner la fréquence en Hz de la note n°");
    this.appendDummyInput();
    this.setOutput(true, null);
    this.setColour(20);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['attendre'] = {
  init: function() {
    this.appendValueInput("durée")
        .setCheck(null)
        .appendField("attendre pendant");
    this.appendDummyInput()
        .appendField("ms");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(60);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['boucle_inf'] = {
  init: function() {
    this.appendDummyInput()
		.setAlign(Blockly.ALIGN_CENTRE)
        .appendField(new Blockly.FieldImage("/static/blockly/media/boucle2.png", 50, 70, "<->"))
        .appendField("               ");
    this.appendStatementInput("sequence_boucle")
        .setCheck(null);
    this.setColour(65);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
    Blockly.BlockSvg.START_HAT=true;
  }
};
