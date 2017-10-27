from __future__ import division, print_function
from visual import *
from Tkinter import *
from visual.graph import *
import wx

value1 = 0

###############################################################

def railGunStart(event):
    i=1.7
    B=5*i*cross(gun.direct,gun.paral)
    bullet.mass=3
    g=vector(0,-9.8,0)
    bullet.force=i*cross(4*gun.paral,B)
    bullet.acceleration=bullet.force/bullet.mass
    bullet.velocity=vector(0,0,0)
    global trail
    trail = curve(color=color.red)
    #gun.rotate(angle=-pi/4, axis=gun.paral, origin=base.pos)
    deltat = 0.1
    t = 0

    while t < 100:
        rate(100)
        if (bullet.pos.z + bullet.size.z/2) > (rail1.pos.z - rail1.size.z/2):
            bullet.velocity = bullet.velocity + bullet.acceleration*deltat
            print("on rail")
            print("direct=",gun.direct)
            print("paral=",gun.paral)
            print("f=",bullet.force)
            print("a=",bullet.acceleration)
        else:
            bullet.velocity = bullet.velocity + g*deltat
            print("falling")
            print("a=",g)
        if (bullet.pos.y - bullet.size.y/2) < (ground.pos.y+ground.size.y/2):
            bullet.velocity.y = -bullet.velocity.y
        if (bullet.pos.z < -35):
            print("BREAK!!!")
            break
        bullet.pos = bullet.pos + bullet.velocity*deltat
        trail.append(pos=bullet.pos)
        t = t + deltat
        #print("B=",B)
        print("bullet.pos=",bullet.pos)
        print("bullet.velocity=",bullet.velocity)
        #print("a=",bullet.acceleration+g)
    print("-------------------------------")
    print(bullet.pos-base.pos)
    print("-------------------------------")

###########################################################

def railGunEnd(self):
    setangletozero(self)
    
def setangletozero(self):
    global value1
    global bullet
    value2 = 0
    value_return = value2-value1
    value1 = value2
    print(value2)
    value_return = value_return*2*pi/360
    print( value_return)
    rotate_up(value_return)
    bullet.pos=(0,0.75,5)
    


def setangle(evt):
    global value1
    value2 = slider.GetValue()
    value_return = value2-value1
    value1 = value2
    print(value2)
    value_return = value_return*2*pi/360
    print( value_return)
    rotate_up(value_return)
    
def rotate_up(a):
    rail1.rotate(angle=-a, axis=gun.paral, origin=base.pos)
    rail2.rotate(angle=-a, axis=gun.paral, origin=base.pos)
    redblock.rotate(angle=-a, axis=gun.paral, origin=base.pos)
    base.rotate(angle=-a, axis=gun.paral, origin=base.pos)
    bullet.rotate(angle=-a, axis=gun.paral, origin=base.pos)
    gun.direct=rotate(vector=gun.direct, angle=-a, axis=gun.paral)

Window = window(width=840, height=720,
           menus=True, title='RailGun',
           style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

panel = Window.panel
title = wx.StaticText(panel, -1, "Rail Gun", pos = (0, 10), size = (800, -1),  style = wx.ALIGN_CENTRE)
title.SetForegroundColour('white')
title.SetBackgroundColour('blue')
button_Start = wx.Button(panel, label = 'Start', pos = (300, 620), size = (60, 60))
button_End = wx.Button(panel, label ='End', pos = (400, 620), size = (60, 60))
button_Start.Bind(wx.EVT_BUTTON, railGunStart)
button_End.Bind(wx.EVT_BUTTON, railGunEnd)
slider = wx.Slider(panel, -1, value= 0, minValue=0, maxValue=90, pos=(10, 600), size = (780, -1), style = wx.SL_AUTOTICKS | wx.SL_MIN_MAX_LABELS | wx.SL_VALUE_LABEL)
slider.Bind(wx.EVT_SCROLL, setangle)
slider.SetTickFreq(5, 1)

disp = display(window=Window, x=20, y=30, width=840-2*20, height=620-3*20,center=(0,15,0),forward=(-1,-1,-1),stereodepth = 2)
ground=box(pos=(0,-4,0), size=(70,2,70), material=materials.bricks)
wall=box(pos=(0,32,-35), size=(70,70,2), material=materials.glass)

gun=frame()
gun.direct=vector(0,0,-1)
gun.paral=vector(-1,0,0)
rail1=box(frame=gun, pos=(-1,0,0), size=(0.5,0.5,15), material=materials.shiny)
rail2=box(frame=gun, pos=(1,0,0), size=(0.5,0.5,15), material=materials.shiny)
redblock=box(frame=gun, pos=(0,0,7.5), size=(2,1,1), color=color.red)
base=cylinder(frame=gun, pos=(-3,0,12), axis=(6,0,0), radius=4.5)
bullet=box(pos=(0,0.75,5), size=(3,0.7,0.7), color=color.red)
