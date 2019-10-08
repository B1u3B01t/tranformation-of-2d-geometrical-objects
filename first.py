import math
import matplotlib.pyplot as jingle_bell
from matplotlib.patches import Ellipse
def Matrix_Multiply(M,N):
	'''
	Multiplies 2 Matrices
	imput : M,N Twp Matrices to be multiplied
	'''
	r1,com,c2 = len(M),len(N),len(N[0])
	A,c=[[0 for i in range(c2)] for j in range(r1)],0
	for i in range(r1):
		for j in range(c2):
			for k in range(com):
				c += (M[i][k]*N[k][j])
			A[i][j] = c
			c=0
	return A
class Polygon():
	'''
	Ploygon Class
	data members: L - list of X cordinates and Y cordinates
	'''
	def __init__(self,L):
		self.X = L[0]# list of X cordinates
		self.Y = L[1]# list of Y cordinates
		self.Z = [1 for i in range(len(self.X))]# list of Z cordinates
	def Scale(self,sx,sy):
		Scale_Mat = [[sx,0,0],[0,sy,0],[0,0,1]]# Linear Transformation for Scaling
		xy = [self.X,self.Y,self.Z]
		L = Matrix_Multiply(Scale_Mat,xy)
		self.X = L[0]
		self.Y = L[1]
		self.Z = L[2]
	def Rotate(self,jinglly_theta1):
		xy = [self.X,self.Y,self.Z]
		jinglly_theta = math.radians(jinglly_theta1)#converting degree to radian
		cos = math.cos(jinglly_theta)#math.pi/2)#jinglly_theta)
		sin = math.sin(jinglly_theta)
		Rotate_Mat = [[cos,-sin,0],[sin,cos,0],[0,0,1]]# Linear Transformation for Rotation
		L = Matrix_Multiply(Rotate_Mat,xy)
		self.X = L[0]
		self.Y = L[1]
		self.Z = L[2]
	def Translate(self,dx,dy):
		xy = [self.X,self.Y,self.Z]
		Translate_Mat = [[1,0,dx],[0,1,dy],[0,0,1]]# Linear Transformation for Traslating
		L = Matrix_Multiply(Translate_Mat,xy)
		self.X = L[0]
		self.Y = L[1]
		self.Z = L[2]
	def plot(self):
		jingle_bell.gcf().clear()# clears the graph
		jingle_bell.fill(self.X,self.Y)# fills the graph with colour
		jingle_bell.show()# displays the graph
	def __str__(self):
		s1 = ''
		s2 = ''
		for i in range(len(self.X)):
			s1+=str(self.X[0][i])+' '
		for i in range(len(self.Y)):
			s2+=str(self.Y[0][i])+ ' '
		return s1+'\n'+s2 #str(self.X)+str(self.Y)+str(self.Z)
class Disc():
	def __init__(self,a,b,rx,ry):
		self.centre = [[a],[b],[1]]
		self.radius1 = [rx]
		self.radius2 = [ry]
	def Scale(self,sx,sy):
		Scale_Mat = [[sx,0,0],[0,sy,0],[0,0,1]]
		xy = [self.radius1,self.radius2,[1]]
		L = Matrix_Multiply(Scale_Mat,xy)
		self.radius1 = L[0]
		self.radius2 = L[1]
	def Translate(self,dx,dy):
		xy = self.centre
		Translate_Mat = [[1,0,dx],[0,1,dy],[0,0,1]]# Linear Transformation for Traslating
		self.centre = Matrix_Multiply(Translate_Mat,xy)
	def Rotate(self,jinglly_theta1):
		jinglly_theta = math.radians(jinglly_theta1)#converting degree to radian
		cos = math.cos(jinglly_theta)#math.pi/2)#jinglly_theta)
		sin = math.sin(jinglly_theta)
		print(cos,sin )
		Rotate_Mat = [[cos,-sin,0],[sin,cos,0],[0,0,1]]
		self.centre = Matrix_Multiply(Rotate_Mat,self.centre)
		print(Matrix_Multiply(Rotate_Mat,self.centre))
	def plot(self):
		jingle_bell.gcf().clear()# clears the graph
		jingle_bell.axes()
		ellipse = Ellipse((self.centre[0][0],self.centre[1][0]),2*(self.radius1[0]),2*(self.radius2[0])) # makes an object called ellipse
		jingle_bell.gca().add_patch(ellipse)
		jingle_bell.show()
		jingle_bell.axis('scaled')
	def __str__(self):
		x=2
		if self.radius1 == self.radius2:
			x=1
		s1 = str(self.centre[0][0]) +' '+ str(self.centre[1][0])+' '
		s1+=str(self.radius1[0])+' '
		if x == 2:
			s1 += str(self.radius2[0])
		return s1#str(self.centre)+'\n'+str(self.radius1)+'\n'+str(self.radius2)
flag = True
shape = input('enter shape - ')
if shape == 'polygon':
	X = list(map(float,input('enter x - ').split()))
	Y = list(map(float,input('enter y - ').split()))
	polygon = Polygon([X,Y])
elif shape == 'disc':
	L = input('enter centre and radius - ').split()
	a,b,rx = float(L[0]),float(L[1]),float(L[2])
	if len(L) == 4:
		ry = float(L[3])
	else:
		ry = rx
	disc = Disc(a,b,rx,ry)
while flag == True:
	if shape == 'polygon':
		jingle_bell.ion()
		jingle_bell.ylabel('Y-Axis By - Rahul Singh 2018178')
		jingle_bell.xlabel('X-Axis')
		jingle_bell.title('Polygon')
		polygon.plot()
		transform = list(input().split())
		if transform[0] == "S":
			polygon.Scale(float(transform[1]),float(transform[2]))
		elif transform[0] == "R":
			polygon.Rotate(float(transform[1]))
		elif transform[0] == "T":
			polygon.Translate(float(transform[1]),float(transform[2]))
		elif transform[0] == "R":
			disc.theta = float(transform[1])
		elif transform[0] == "quit":
			flag = False
		polygon.plot()
		print(polygon)
	if shape == 'disc':
		jingle_bell.ion()
		jingle_bell.title('Disc')
		jingle_bell.ylabel('Y-Axis By - Rahul Singh 2018178')
		jingle_bell.xlabel('X-Axis')
		disc.plot()
		transform = input().split()
		if transform[0] == "S":
			disc.Scale(float(transform[1]),float(transform[2]))
		elif transform[0] == "T":
			disc.Translate(float(transform[1]),float(transform[2]))
		elif transform[0] == "quit":
			flag = False
		elif transform[0] == 'R':
			print(float(transform[1]))
			disc.Rotate(float(transform[1]))
		disc.plot()
		print(disc)