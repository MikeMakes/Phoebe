import pygame

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

def init_joystick(n=0):
	joysticks[n].init()

def whoareyou(n=0):
	return joysticks[n].get_name()

def howmanyaxes(n=0):
	return joysticks[n].get_numaxes()

def get_all_axes(n=0):
	return [joysticks[n].get_axis(i) for i in range(joysticks[n].get_numaxes())]

def get_axes(selection=None, n=0):
	if selection:
		if isinstance(selection[0],tuple):
			out=[]
			for i in range(0,len(selection[0])):
				if selection[0][i] is None:
					out.insert(i,get_all_axes())
				else:
					out.insert(i,joysticks[n].get_axis(selection[0][i]))
		else
			out=joysticks[n].get_axis(selection[0])
	else:
		out = get_all_axes(n)
	return out

def howmanybuttons(n=0):
	return joysticks[n].get_numbuttons()

def get_all_buttons(n=0):
	return [joysticks[n].get_button(i) for i in range(joysticks[n].get_numbuttons())]

def get_buttons(selection=None, n=0):
	if selection:
		out = joysticks[n].get_button(selection[-2])
	else:
		out=get_all_buttons(n)
	return out

def howmanyhats(n=0):
	return joysticks[n].get_numhats()

def get_all_hats(n=0):
	return [joysticks[n].get_hat(i) for i in range(joysticks[n].get_numhats())]

def get_hats(selection=None, n=0):
	if selection:
		out=joysticks[n].get_hat(selection[-1])
	else:
		out=get_all_axes(n)	
	return out


#create a group of axes, usefull for sticks
#ls = left stick = ( (axe x , axe y , axe z,...,), button , hat )
