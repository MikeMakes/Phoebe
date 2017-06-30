import pmw

try:
	motor = __init__(24, 50)
	i=float(5)
	start(motor, i)
        while True:
                print ("Valor de i:{}".format(i))
                print ("Esperando nueva i: ")
                i=input()
                changedc(motor, i)
finally:
	end(motor)
	clean()
