format 224

classcanvas 128002 class_ref 148482 // HumiditySensor
  simpleclassdiagramsettings end
  xyz 65.6 25.6 2000
end
classcanvas 128130 class_ref 148610 // TemperatureSensor
  simpleclassdiagramsettings end
  xyz 56.7 93.4 2000
end
classcanvas 128258 class_ref 148738 // IMUSensor
  simpleclassdiagramsettings end
  xyz 77.7 158.9 2000
end
usecasecanvas 128386 usecase_ref 135170 // View Trip Information
  xyzwh 619.2 498.8 3005 128 65 label_xy 631 521
end
usecasecanvas 128642 usecase_ref 135298 // View Logged Data
  xyzwh 620.5 346.2 3005 123 66 label_xy 636 372
end
subject 128770 "Embedded System & Local Database"
  xyzwh 184.8 47.5 2000 588 276
usecasecanvas 129154 usecase_ref 135554 // Collection of Data
  xyzwh 199.5 86.2 3005 133 73 label_xy 223 115
end
usecasecanvas 129794 usecase_ref 135682 // View Enviromental & Inertial Warnings on LED Matrix
  xyzwh 608.4 85.1 3005 133 73 max_width 23 label_xy 618 100
end
usecasecanvas 129922 usecase_ref 135810 // Processing Data
  xyzwh 399.8 84.2 3005 139 77 label_xy 429 111
end
usecasecanvas 130178 usecase_ref 135938 // View Enviromental Readings on LED Matrix
  xyzwh 611.8 163.8 3005 131 71 max_width 18 label_xy 627 179
end
classcanvas 130562 class_ref 148866 // Delivery_Driver
  simpleclassdiagramsettings end
  xyz 804.7 126.3 2000
end
usecasecanvas 130946 usecase_ref 136066 // Write Data to Local Database
  xyzwh 304.3 238.4 3005 139 73 max_width 18 label_xy 337 258
end
subject 131202 "Remote Server & Remote Database"
  xyzwh 184.6 332.9 2000 588 255
usecasecanvas 131458 usecase_ref 136322 // Write Data to Remote Database
  xyzwh 519.5 240.4 3005 132 69 max_width 18 label_xy 544 259
end
usecasecanvas 131842 usecase_ref 136450 // User Authentication
  xyzwh 619.5 420.6 3005 125 65 label_xy 632 446
end
classcanvas 131970 class_ref 148994 // Maintainence_Crew
  simpleclassdiagramsettings end
  xyz 800.4 289.7 2000
end
classcanvas 132098 class_ref 149122 // Driver_Manager
  simpleclassdiagramsettings end
  xyz 817.7 455.4 2000
end
usecasecanvas 132738 usecase_ref 136578 // Read Information from Remote Database
  xyzwh 214.5 419.5 3005 135 65 max_width 20 label_xy 222 436
end
usecasecanvas 132866 usecase_ref 136706 // Read Trip Table from Database
  xyzwh 402.2 500.9 3005 129 71 max_width 22 label_xy 413 521
end
usecasecanvas 132994 usecase_ref 136834 // Read Trip_Data Table from Database
  xyzwh 404.2 344.9 3005 125 67 max_width 19 label_xy 416 364
end
classcanvas 135682 class_ref 156674 // Staff
  simpleclassdiagramsettings end
  xyz 950 289 2000
end
line 129410 ----
  from ref 128002 z 3006 to ref 129154
line 129538 ----
  from ref 128130 z 3006 to ref 129154
line 129666 ----
  from ref 128258 z 3006 to ref 129154
simplerelationcanvas 130050 simplerelation_ref 134658
  from ref 129922 z 3006 stereotype "<<include>>" xyz 338 127 3000 to ref 129154
end
simplerelationcanvas 130306 simplerelation_ref 134786
  from ref 129794 z 3006 stereotype "<<include>>" xyz 546.5 124 3000 to ref 129922
end
simplerelationcanvas 130434 simplerelation_ref 134914
  from ref 130178 z 3006 stereotype "<<include>>" xyz 545 172 3000 to ref 129922
end
line 130690 ----
  from ref 129794 z 3006 to ref 130562
line 130818 ----
  from ref 130178 z 3006 to ref 130562
simplerelationcanvas 131074 simplerelation_ref 135042
  from ref 130946 z 3006 stereotype "<<include>>" xyz 420 200.5 3000 to ref 129922
end
simplerelationcanvas 131714 simplerelation_ref 135298
  from ref 131458 z 3006 stereotype "<<include>>" xyz 451 273 3000 to ref 130946
end
line 132482 ----
  from ref 131970 z 3006 to point 782.5 358.9
  line 135554 z 3006 to ref 128642
line 132610 ----
  from ref 128386 z 3006 to ref 132098
simplerelationcanvas 133634 simplerelation_ref 135554
  from ref 128642 z 3006 stereotype "<<include>>" xyz 544 377.5 3000 to ref 132994
end
simplerelationcanvas 133762 simplerelation_ref 135682
  from ref 128386 z 3006 stereotype "<<include>>" xyz 549 535.5 3000 to ref 132866
end
simplerelationcanvas 133890 simplerelation_ref 135810
  from ref 132866 z 3006 stereotype "<<include>>" xyz 327.5 500 3000 to ref 132738
end
simplerelationcanvas 134018 simplerelation_ref 135938
  from ref 132994 z 3006 stereotype "<<include>>" xyz 376.5 415 3000 to ref 132738
end
simplerelationcanvas 134146 simplerelation_ref 136066
  from ref 131842 z 3006 stereotype "<<include>>" xyz 455 449.5 3000 to ref 132738
end
line 134530 ----
  from ref 129794 z 3006 to point 789.8 210.7
  line 134786 z 3006 to ref 131970
line 134658 ----
  from ref 130178 z 3006 to point 779.8 245.3
  line 134914 z 3006 to ref 131970
relationcanvas 136322 relation_ref 136834 // <generalisation>
  from ref 130562 z 2001 to ref 135682
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 136450 relation_ref 136962 // <generalisation>
  from ref 131970 z 2001 to ref 135682
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
relationcanvas 136578 relation_ref 137090 // <generalisation>
  from ref 132098 z 2001 to ref 135682
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
line 136706 ----
  from ref 131842 z 3006 to point 811 424
  line 136962 z 3006 to ref 135682
end
