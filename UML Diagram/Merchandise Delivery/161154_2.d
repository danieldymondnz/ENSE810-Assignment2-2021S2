format 224

deploymentnodecanvas 128002 deploymentnode_ref 128002 // Embedded System
  xyzwh 37 89 0 147 269
end
deploymentnodecanvas 128642 deploymentnode_ref 128130 // RemoteServer
  xyzwh 386 156 0 145 103
end
textcanvas 128770 "MySQL Database
Apache Web Server
Local Network Access
"
  xyzwh 389 270 2000 110 56
textcanvas 129282 "Sense Hat
SQLite Database"
  xyzwh 43 369 2000 81 28
artifactcanvas 129410 artifact_ref 135042 // DatabaseConfig
  xyz 396 196 2000
end
textcanvas 129666 "1..n"
  xyzwh 195 212 2000 22 18
textcanvas 129794 "1"
  xyzwh 368 211 2000 16 20
line 128898 ---- decenter_begin 437
  from ref 128002 z 2001 label "internal network over wireless" max_width 255 xyz 211.5 184.5 2001 to ref 128642
end
