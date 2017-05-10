import pygame

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

def init_joystick(n=0):
	joysticks[n].init()

def whoareyou(n=0):
	return joysticks[n].get_name()

def howmanyaxes(n=0):
	return joysticks[n].get_numaxes()

def get_axes(selection, n=0):
	out=[None]
	for i in range(0,len(selection)-1):
		out.insert(i,joysticks[n].get_axis(selection[i]))
	out.pop()
	return out

def get_all_axes(n=0):
	return [joysticks[n].get_axis(i) for i in range(joysticks[n].get_numaxes())]

def howmanybuttons(n=0):
	return joysticks[n].get_numbuttons()

def get_buttons(selection, n=0):
	return joysticks[n].get_button(selection[1])

def get_all_buttons(n=0):
	return [joysticks[n].get_button(i) for i in range(joysticks[n].get_numbuttons())]

def howmanyhats(n=0):
	return joysticks[n].get_numhats()

def get_hats(selection, n=0):
	return joysticks[n].get_hat(selection[0])

def get_all_hats(n=0):
	return [joysticks[n].get_hat(i) for i in range(joysticks[n].get_numhats())]

#create a group of axes, usefull for sticks
#ls = left stick = ( axe x , axe y , axe z, ... , button/None if there is not button )
