format 224

classcanvas 128002 class_ref 128002 // MatrixDriver
  classdiagramsettings show_members_full_definition yes show_members_visibility yes show_members_stereotype yes show_members_multiplicity yes show_members_initialization yes show_attribute_modifiers yes member_max_width 0 show_stereotype_properties yes end
  xyz 34.84 692.1 2000
end
classcanvas 128130 class_ref 128130 // Controller
  classdiagramsettings member_max_width 0 end
  xyz 215.92 448.56 2000
end
classcanvas 128258 class_ref 128258 // DataCollection
  classdiagramsettings member_max_width 0 end
  xyz 54.08 -9.38 2000
end
classcanvas 128514 class_ref 128514 // DBAgent
  classdiagramsettings member_max_width 0 end
  xyz 701.16 194.02 2000
end
relationcanvas 128642 relation_ref 128002 // <association>
  from ref 128258 z 2001 to ref 128130
  no_role_a no_role_b
  multiplicity_a_pos 297 462 3000 multiplicity_b_pos 297 386 3000
end
relationcanvas 128770 relation_ref 128130 // <association>
  from ref 128130 z 2001 to ref 128002
  no_role_a no_role_b
  multiplicity_a_pos 297 717 3000 multiplicity_b_pos 297 637 3000
end
relationcanvas 128898 relation_ref 128258 // <association>
  from ref 128130 z 2001 to ref 128514
  no_role_a no_role_b
  multiplicity_a_pos 675 564 3000 multiplicity_b_pos 435 564 3000
end
preferred_whz 1453 840 1.5
end
