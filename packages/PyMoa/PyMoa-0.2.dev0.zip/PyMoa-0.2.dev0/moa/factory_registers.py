from kivy.factory import Factory

r = Factory.register

r('StageTreeNode', module='moa.render.treerender')
r('StageSimpleDisplay', module='moa.render.stage_simple')


# --------------------- devices -----------------------------
r('Device', module='moa.device.__init__')
r('DigitalChannel', module='moa.device.digital')
r('DigitalPort', module='moa.device.digital')
r('ButtonChannel', module='moa.device.digital')
r('ButtonPort', module='moa.device.digital')

r('AnalogChannel', module='moa.device.analog')
r('AnalogPort', module='moa.device.analog')
r('NumericPropertyChannel', module='moa.device.analog')
r('NumericPropertyPort', module='moa.device.analog')


# ---------------------- stages --------------------------------
r('MoaStage', module='moa.stage.__init__')
r('Delay', module='moa.stage.delay')
r('GateStage', module='moa.stage.gate')
r('DigitalGateStage', module='moa.stage.gate')
r('AnalogGateStage', module='moa.stage.gate')
