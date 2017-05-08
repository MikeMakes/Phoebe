import pygame

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

def init_joystick(n=0):
	joysticks[n].init()

def whoareyou(n=0):
	return joysticks[n].get_name()

def howmanyaxes(n=0):
	return joysticks[n].get_numaxes()

def get_axes(n=0):
	return [joysticks[n].get_axis(x) for x in range(joysticks[n].get_numaxes())]

def howmanybuttons(n=0):
	return joysticks[n].get_numbuttons()

def get_buttons(n=0):
	return [joysticks[n].get_button(x) for x in range(joysticks[n].get_numbuttons())]

def howmanyhats(n=0):
	return joysticks[n].get_numhats()

def get_hats(n=0):
	return [joysticks[n].get_hat(x) for x in range(joysticks[n].get_numhats())]
