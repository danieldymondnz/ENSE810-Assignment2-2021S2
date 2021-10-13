format 224

classinstancecanvas 128002 classinstance_ref 128130 // 
  xyz 72 5 2000 life_line_z 2000
end
classinstancecanvas 128130 classinstance_ref 128258 // 
  xyz 382 6 2000 life_line_z 2000
end
classinstancecanvas 128258 classinstance_ref 128386 // 
  xyz 217 6 2000 life_line_z 2000
end
classinstancecanvas 128386 classinstance_ref 128514 // 
  xyz 526 8 2000 life_line_z 2000
end
durationcanvas 128514 classinstance_ref 128002 // :Controller
  xyzwh 97 78 2010 11 91
end
durationcanvas 128642 classinstance_ref 128258 // :DataCollection
  xyzwh 253 86 2010 11 25
end
durationcanvas 128898 classinstance_ref 128130 // :MatrixDriver
  xyzwh 413 113 2010 11 25
end
durationcanvas 129538 classinstance_ref 128386 // :DBAgent
  xyzwh 549 141 2010 11 85
  overlappingdurationcanvas 131330
    xyzwh 555 156 2020 11 25
  end
  overlappingdurationcanvas 131842
    xyzwh 555 184 2020 11 25
  end
end
msg 128770 synchronous
  from durationcanvas_ref 128514
  to durationcanvas_ref 128642
  yz 86 2015 msg operation_ref 129282 // "__init__(inout self : DataCollection [1], in senseHAT : SenseHat [1], in dataQueue : Queue [1])"
  show_full_operations_definition default show_class_of_operation default drawing_language default show_context_mode default
  label_xy 158 72
msg 129026 synchronous
  from durationcanvas_ref 128514
  to durationcanvas_ref 128898
  yz 113 2015 msg operation_ref 128002 // "__init__(inout self : MatrixDriver [1], in senseHAT : SenseHat [1])"
  show_full_operations_definition default show_class_of_operation default drawing_language default show_context_mode default
  label_xy 161 104
msg 129666 synchronous
  from durationcanvas_ref 128514
  to durationcanvas_ref 129538
  yz 141 2015 msg operation_ref 137090 // "__init__(inout self : DBAgent [1], in dataQueue : Queue<dict> [1], in registration : string [1], in localDBConfig : dict [1], in remoteDBConfig : dict)"
  show_full_operations_definition default show_class_of_operation default drawing_language default show_context_mode default
  label_xy 161 130
reflexivemsg 131458 synchronous
  to durationcanvas_ref 131330
  yz 156 2025 msg operation_ref 143874 // "_connectLocalDB(inout self : DBAgent [1])"
  show_full_operations_definition default show_class_of_operation default drawing_language default show_context_mode default
  label_xy 593 153
reflexivemsg 131970 synchronous
  to durationcanvas_ref 131842
  yz 184 2025 msg operation_ref 151810 // "_disconnectLocalDB(inout self : DBAgent [1])"
  show_full_operations_definition default show_class_of_operation default drawing_language default show_context_mode default
  label_xy 594 181
end
