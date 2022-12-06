
import matplotlib.pyplot as plt

opcion = int(input("Si tu ecuacion es de la forma Ay^2 + By+ Cx+D=0, escribe 1, si es de la forma Ax^2 + Bx+ Cy+D=0, escribe 2. Cualquier otro caso, no es parabola:"))
#pedir coefecientes a,b,c,d
a,b,c,d = map(int,input("Escribe los coeficientes conforme a la ecuación general de una parábola separado por espacios: ").split())
#para saber si es horizontal o vertical 
coordenada_x = []
coordenada_y= []
if opcion == 1:
    #obtener el vertice
    h = ((b**2)/(4*a*c) - (d/c))
    k = -(b/(2*a))
    vertice = (h,k)
    #para obtener las coordenadas del foco = (h + p, k)
    p = -c /(4*a)
    foco = (h+p,k)
    plt.plot(h+p,k,'o',c= 'red')
    lr = abs(4*p) #valor absoluto
    #Las coordenadas de los extremos del lado recto: Se divide el lado recto entre 2, y se suma y resta el resultado a la ordenada del foco.
    lr_y = h+p, k + (lr/2)
    lr_y2 = h+p, k - (lr/2)
    cr_ladorecto= (lr_y2,lr_y)
    plt.plot(h+p, k + (lr/2), 'o', c= 'green')
    plt.plot(h+p, k - (lr/2),'o', c = 'green')
    for i in range(-50,50):
        coordenada_y.append(i)
        coordenada_x.append((-a*(i**2)-b*i -d)/c)
elif opcion == 2:
    #para obtener las coordenadas del foco = (h, k+p)
    k = (((b**2)/(4*a*c)) - (d/c))
    h = -(b/(2*a))
    p = -(c) / (4*a)
    vertice = (h,k)
    foco = (h,k+p)
    plt.plot(h,k+p,'o', c= 'red')
    #longitud del lado recto
    lr = abs(4*p) #valor absoluto
    #Las coordenadas de los extremos del lado recto: Se divide el lado recto entre 2, y se suma y resta el resultado a la abscisa del foco.
    lr_x = h+ (lr/2), (k+p)
    lr_x2 = h- (lr/2), (k+p)
    cr_ladorecto= (lr_x2,lr_x)
    plt.plot(h+ (lr/2), (k+p), 'o',c= 'green')
    plt.plot(h- (lr/2), (k+p),'o',c= 'green')
    for i in range(-100,100):
        coordenada_x.append(i)
        coordenada_y.append((-a*(i**2)-b*i -d)/c)

#para formar la ecuación ordinaria
if -(k) > 0: ec_k = "+" + (str(-(k))) #para que ponga el signo + en caso de que la coordenada de k sea negativa
else: ec_k = (str(-(k)))
if -(h) > 0: ec_h = "+"+(str(-(h))) #para que ponga el signo + en caso de que la coordenada de h sea negativa
else: ec_h = (str(-(h)))

if opcion == 1:
    ecuacion_ordinaria= (("(y"+ ec_k+")")+ "^2 = " + str(4*p) + "(x" + ec_h+")")
elif opcion == 2:
    ecuacion_ordinaria= (("(x"+ ec_h +")")+ "^2 = " + str(4*p) + "(y"+ ec_k +")")


print("Las coordenadas del vertice son: ",vertice )
print("Las coordenadas del foco son: ",foco)
print("La ecuacion ordinaria es: ", ecuacion_ordinaria)
print("La longitud del lado recto es: ", lr)
print("Las coordenadas de los extremos del lado recto son: ", cr_ladorecto)
plt.plot(coordenada_x,coordenada_y)
plt.plot(h,k,'o',c= 'blue',) #'o' es para indicar que es un punto #vertice
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()


