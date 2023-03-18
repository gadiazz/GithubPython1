clear all;close all; clc; %#ok

s = tf('s')

gp = 1/((s+1)*(s+2))
step(gp)
h = (2.59/10)
gpz = c2d(gp,h,"zoh")
gpz2 =(1/h)*c2d(gp,h,"impulse")