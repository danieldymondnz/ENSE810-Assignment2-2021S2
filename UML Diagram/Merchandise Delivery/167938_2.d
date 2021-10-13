format 224

classcanvas 128002 class_ref 128514 // DBAgent
  classdiagramsettings member_max_width 0 end
  xyzwh 495.3 164.5 2000 77 39
end
classcanvas 128130 class_ref 155778 // datetime
  classdiagramsettings member_max_width 0 end
  color lightgray
  xyz 602.5 48.8 2000
end
classcanvas 128258 class_ref 155906 // pymysql
  classdiagramsettings member_max_width 0 end
  color lightgray
  xyz 504.3 49.8 2000
end
classcanvas 128386 class_ref 156034 // threading
  classdiagramsettings member_max_width 0 end
  color lightgray
  xyz 503.9 358.1 2000
end
classcanvas 128514 class_ref 156162 // sqlite3
  classdiagramsettings member_max_width 0 end
  color lightgray
  xyz 428.3 49.1 2000
end
classcanvas 129154 class_ref 128130 // Controller
  classdiagramsettings member_max_width 0 end
  xyz 255.9 163.4 2006
end
classcanvas 129666 class_ref 156290 // sense_emu
  classdiagramsettings member_max_width 0 end
  color lightgray
  xyz 133 254.8 2000
end
classcanvas 129794 class_ref 128002 // MatrixDriver
  classdiagramsettings member_max_width 0 end
  xyz 251.8 318.5 3005
end
classcanvas 130050 class_ref 156418 // queue
  classdiagramsettings member_max_width 0 end
  color lightgray
  xyz 168.5 61 2000
end
classcanvas 130178 class_ref 128258 // DataCollection
  classdiagramsettings member_max_width 0 end
  xyz 47.5 163.6 3005
end
classcanvas 131074 class_ref 156546 // time
  classdiagramsettings member_max_width 0 end
  color lightgray
  xyz 69.5 59.3 2000
end
relationcanvas 128642 relation_ref 134786 // <dependency>
  from ref 128002 z 2001 stereotype "<<import>>" xyz 614 96 3000 to ref 128130
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 128770 relation_ref 134914 // <dependency>
  from ref 128002 z 2001 stereotype "<<import>>" xyz 542 94 3000 to ref 128258
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 128898 relation_ref 135042 // <dependency>
  decenter_end 469
  from ref 128002 z 2001 stereotype "<<import>>" xyz 540.5 303.5 3000 to ref 128386
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 129026 relation_ref 135170 // <dependency>
  from ref 128002 z 2001 stereotype "<<import>>" xyz 415.5 97 3000 to ref 128514
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 129282 relation_ref 128258 // <association>
  from ref 129154 z 2007 to ref 128002
  no_role_a no_role_b
  multiplicity_a_pos 480 187 3000 multiplicity_b_pos 330 187 3000
end
relationcanvas 129538 relation_ref 135298 // <dependency>
  from ref 129154 z 2007 stereotype "<<import>>" xyz 456 303 3000 to ref 128386
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 129922 relation_ref 128130 // <association>
  from ref 129154 z 3006 to ref 129794
  no_role_a no_role_b
  multiplicity_a_pos 276 302 3000 multiplicity_b_pos 275 204 3000
end
relationcanvas 130306 relation_ref 128002 // <association>
  from ref 130178 z 3006 to ref 129154
  no_role_a no_role_b
  multiplicity_a_pos 241 187 3000 multiplicity_b_pos 144 187 3000
end
relationcanvas 130434 relation_ref 135426 // <dependency>
  from ref 130178 z 3006 stereotype "<<import>>" xyz 149 231 3000 to ref 129666
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 130562 relation_ref 135554 // <dependency>
  from ref 129154 z 2007 stereotype "<<import>>" xyz 225 230 3000 to ref 129666
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 130690 relation_ref 135682 // <dependency>
  from ref 129794 z 3006 stereotype "<<import>>" xyz 166 299.5 3000 to ref 129666
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 130818 relation_ref 135810 // <dependency>
  from ref 130178 z 3006 stereotype "<<import>>" xyz 419 382 3000 to point 90.7 375.2
  line 131330 z 3006 to ref 128386
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 130946 relation_ref 135938 // <dependency>
  from ref 129154 z 2007 stereotype "<<import>>" xyz 246 123 3000 to ref 130050
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 131202 relation_ref 136066 // <dependency>
  from ref 130178 z 3006 stereotype "<<import>>" xyz 33 111.5 3000 to ref 131074
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 131458 relation_ref 136194 // <dependency>
  from ref 130178 z 3006 stereotype "<<import>>" xyz 146 122.5 3000 to ref 130050
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 131586 relation_ref 136322 // <dependency>
  from ref 129794 z 3006 stereotype "<<import>>" xyz 417 343.5 3000 to ref 128386
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
end
