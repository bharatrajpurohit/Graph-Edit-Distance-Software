from Tkinter import *
import numpy as np
import tkMessageBox
from PIL import ImageTk
from PIL import Image

key1=0
key2=0






class Vertex:
    def __init__(self,key,weight):
        self.id = int(key)
        self.connectedTo = {}
        self.cost = int(weight)

    def addNeighbor(self,nbr,weight= -1):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getCost(self):
        return self.cost

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,k,cost=1):
	key = int(k)        
	self.numVertices = self.numVertices + 1
        newVertex = Vertex(key,cost)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def getVertWeight(self,k):
        key = int(k)
        return self.vertList[key].getCost()


    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=1):        
	if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.vertList[t].addNeighbor(self.vertList[f], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())




g1 = Graph();
g2 = Graph();









class UI(Frame):
   def __init__(self,parent):
     Frame.__init__(self,parent)
     self.parent  = parent;
     self.frame =Frame(self.parent)
     self.main2()
        
   def main2(self):
     self.frame.destroy()
     #print("hii bharat");    	
     self.parent.title("Graph Edit Distance " )
     fbg = "white"
     self.frame = Frame(self.parent)
     self.frame = Frame(self.parent,background=fbg)
     self.frame1 = Frame(self.frame,background=fbg)
     self.frame2 = Frame(self.frame,background=fbg)
     self.frame3 = Frame(self.frame,background=fbg)
     self.frame4 = Frame(self.frame,background=fbg)
     self.frame5 = Frame(self.frame,background=fbg)
     
     abg = "#f92727"
     mybg="orange"
     self.frame.pack()
     self.frame2.pack(side='top',fill='both',expand=True)
     self.frame1.pack(side='top',fill='both',expand=True)
     self.frame3.pack(side='top',fill='both',expand=True)
     self.frame4.pack(side='bottom',fill='both',expand=True)
     self.frame5.pack(side='bottom',fill='both',expand=True)    
     self.B = Button(self.frame1, text ="Import Graph2 ",pady=10,width = 40,height = 4,command=self.graph2,activebackground=abg,bg=mybg,relief="sunken")                                             
     self.C = Button(self.frame2,text = "Import Graph1",pady=10,command=self.VbyVgraph,width = 40,height = 4,activebackground=abg,bg=mybg,relief="groove")
     self.C.pack(expand=True,pady = 4)
     self.B.pack(expand=True,pady=4)
     self.D = Button(self.frame4,text = "Show Graphs",pady=10,width = 40,height = 4,command=self.printgraph,activebackground=abg,bg=mybg,relief="groove")
     self.D.pack(expand=True,pady=4)
     self.E = Button(self.frame3, text ="Cost Matrix",pady=10,command=self.vertexCostMatrix,width = 40,height = 4,activebackground=abg,bg=mybg,relief="sunken")
     #self.E.pack(expand= True,pady=4)
     self.F = Button(self.frame5, text ="Edit Distance",pady=10,command=self.edgeCostMatrix,width = 40,height = 4,activebackground=abg,bg=mybg,relief="sunken")
     self.F.pack(expand= True,pady=4)
        


   
   def VbyVgraph(self):
     global g1
     self.frame.destroy()
     self.parent.title("AddNode" )
     self.frame = Frame(self.parent)
     fbg= "white"
     abg="#f92727"
     mybg="orange"
     self.frame1 = Frame(self.frame,background=fbg)
     self.frame2 = Frame(self.frame,background=fbg)
     self.frame3 = Frame(self.frame,background=fbg)
     self.frame4 = Frame(self.frame,background=fbg)
     self.frame5 = Frame(self.frame,background=fbg)
     self.frame6 = Frame(self.frame,background=fbg)
     self.frame7 = Frame(self.frame,background=fbg)
     self.frame8 = Frame(self.frame,background=fbg)
     self.frame9 = Frame(self.frame,background=fbg)

     self.A1 = Label(self.frame1, text ="Total Node",bg=fbg)
     self.A1.pack(expand=True,side=LEFT)
     self.A2 = Text(self.frame1,width = 3,height =2)
     self.A2.insert(INSERT,"%s"%(g1.numVertices))
     self.A2.pack(side=RIGHT)
     self.D1 = Label(self.frame2, text ="Node Attribute",bg=fbg)
     self.D1.pack(expand=True,side=LEFT)
     self.D2 = Entry(self.frame2,bd=5)
     self.D2.pack(side=RIGHT)
     self.E1=  Label(self.frame4,text ="ADD EDGE",bg=fbg)
     self.E1.pack(expand=True,side=LEFT) 
     self.B1 = Label(self.frame5, text ="Edge Vertex1",bg=fbg)
     self.B1.pack(expand=True,side=LEFT)
     self.B2 = Entry(self.frame5,bd=5)
     self.B2.pack(side=RIGHT)
     self.C1 = Label(self.frame6, text ="Edge Vertex 2",bg=fbg)
     self.C1.pack(expand=True,side=LEFT)
     self.C2 = Entry(self.frame6,bd=5)
     self.C2.pack(side=RIGHT)
     self.E1 = Label(self.frame7, text ="Edge weight",bg=fbg)
     self.E1.pack(expand=True,side=LEFT)
     self.E2 = Entry(self.frame7,bd=5)     
     self.E2.pack(side=RIGHT)



     self.sub = Button(self.frame3,text = "Add VERTEX",pady=10,command=self.addV,width = 10,activebackground=abg,bg=mybg,relief="groove")
     self.sub.pack(expand=True,pady=5)
     self.sub = Button(self.frame8,text = "Add EDGE",pady=10,command=self.addE,width = 10,activebackground=abg,bg=mybg,relief="groove")
     self.sub.pack(expand=True,pady=5)
     
     self.sub = Button(self.frame9,text = "Back",pady=10,command=self.main2,width = 10,activebackground=abg,bg=mybg,relief="groove")
     self.sub.pack(expand=True,pady=5)
     self.frame.pack()
     self.frame1.pack(side='top',fill='both',expand=True)
     self.frame2.pack(side='top',fill='both',expand=True)
     self.frame3.pack(side='top',fill='both',expand=True)
     self.frame4.pack(side='top',fill='both',expand=True)
     self.frame5.pack(side='top',fill='both',expand=True)
     self.frame6.pack(side='top',fill='both',expand=True)
     self.frame7.pack(side='top',fill='both',expand=True)
     self.frame8.pack(side='top',fill='both',expand=True)
     self.frame9.pack(side='top',fill='both',expand=True)

     return 0;
    
   

   def addV(self):
     global g1
     global key1
     #node = int(self.A2.get())
     #print(int(node)+1)
     node = key1  
     key1+=1
     nodeweight = int(self.D2.get())    
     
     g1.addVertex(node,nodeweight)
     self.VbyVgraph()


   def addE(self):
     global g1
     global key1
     V1 = int(self.B2.get())
     V2 = int(self.C2.get())
     weight = int(self.E2.get())
     if V1 not in g1.vertList:
         key = key1
         key1+=1 
	 nv = g1.addVertex(key,1)
     if V2 not in g1.vertList:
         key = key1
	 key1+=1
         nv = g1.addVertex(key,1)

     if g1.vertList[V1] not in g1.vertList[V2].connectedTo:
        g1.addEdge(V1,V2,weight)
     else:
        tkMessageBox.showinfo("Sorry", "Edge alredy inseted")
     self.VbyVgraph()     


   def printgraph(self):
     global g1
     global g2
     self.frame.destroy()
     self.parent.title("Print" )
     self.frame = Frame(self.parent)
     fbg="white"
     abg="#f92727"
     mybg="orange"
     self.frame1 = Frame(self.frame,background="white")
     self.frame2 = Frame(self.frame,background="white")
     self.frame3 = Frame(self.frame,background="white")
     self.A1 = Label(self.frame1, text ="Graph G1",bg=fbg)
     self.A1.pack(expand=True,side=LEFT)
     self.B1 = Label(self.frame1, text ="Graph G2",bg=fbg)
     self.B1.pack(expand=True,side=RIGHT)
     
     text1 = Text(self.frame2,width=55,bd=5)
     text2 = Text(self.frame2,width=55,bd=5)
     
     
     for v in g1:
	for w in v.getConnections():
		text1.insert(INSERT,"[ %s(%s) , %s(%s) ]{%s}\n" % (v.getId(),v.getCost(), w.getId(),w.getCost(),v.getWeight(w) ))
     
     
     for v in g2:
	for w in v.getConnections():
		text2.insert(INSERT,"[ %s(%s) , %s(%s) ]{%s}\n" % (v.getId(),v.getCost(), w.getId(),w.getCost(),v.getWeight(w) ))
     

     self.sub = Button(self.frame3,text = "Back",pady=10,command=self.main2,width = 10,activebackground=abg,bg=mybg,relief="groove")
     self.sub.pack(expand=True)
     self.frame.pack(side='top',fill='both',expand=True)
     self.frame1.pack(side='top',fill='both',expand=True)
     self.frame2.pack(side='top',fill='both',expand=True)
     self.frame3.pack(side='top',fill='both',expand=True)
     
     text1.pack(side='left')
     text2.pack(side='right')


   def graph2(self):
     global g2
     self.frame.destroy()
     self.parent.title("AddNode" )
     self.frame = Frame(self.parent)
     fbg= "white"
     abg="#f92727"
     mybg="orange"
     self.frame1 = Frame(self.frame,background=fbg)
     self.frame2 = Frame(self.frame,background=fbg)
     self.frame3 = Frame(self.frame,background=fbg)
     self.frame4 = Frame(self.frame,background=fbg)
     self.frame5 = Frame(self.frame,background=fbg)
     self.frame6 = Frame(self.frame,background=fbg)
     self.frame7 = Frame(self.frame,background=fbg)
     self.frame8 = Frame(self.frame,background=fbg)
     self.frame9 = Frame(self.frame,background=fbg)

     self.A1 = Label(self.frame1, text ="Total Nodes",bg=fbg)
     self.A1.pack(expand=True,side=LEFT)
     self.F2 = Text(self.frame1,width = 3,height =2)
     self.F2.insert(INSERT,"%s"%(g2.numVertices))
     self.F2.pack(side=RIGHT)
     self.D1 = Label(self.frame2, text ="Node Attribute",bg=fbg)
     self.D1.pack(expand=True,side=LEFT)
     self.G2 = Entry(self.frame2,bd=5)
     self.G2.pack(side=RIGHT)
     self.E1=  Label(self.frame4,text ="ADD EDGE",bg=fbg)
     self.E1.pack(expand=True,side=LEFT) 
     self.B1 = Label(self.frame5, text ="Edge Vertex1",bg=fbg)
     self.B1.pack(expand=True,side=LEFT)
     self.H2 = Entry(self.frame5,bd=5)
     self.H2.pack(side=RIGHT)
     self.C1 = Label(self.frame6, text ="Edge Vertex 2",bg=fbg)
     self.C1.pack(expand=True,side=LEFT)
     self.I2 = Entry(self.frame6,bd=5)
     self.I2.pack(side=RIGHT)
     self.E1 = Label(self.frame7, text ="Edge weight",bg=fbg)
     self.E1.pack(expand=True,side=LEFT)
     self.J2 = Entry(self.frame7,bd=5)     
     self.J2.pack(side=RIGHT)



     self.sub = Button(self.frame3,text = "Add VERTEX",pady=10,command=self.addV_in_g2,width = 10,activebackground=abg,bg=mybg,relief="groove")
     self.sub.pack(expand=True,pady=5)
     self.sub = Button(self.frame8,text = "Add EDGE",pady=10,command=self.addE_in_g2,width = 10,activebackground=abg,bg=mybg,relief="groove")
     self.sub.pack(expand=True,pady=5)
     
     self.sub = Button(self.frame9,text = "Back",pady=10,command=self.main2,width = 10,activebackground=abg,bg=mybg,relief="groove")
     self.sub.pack(expand=True,pady=5)
     self.frame.pack()
     self.frame1.pack(side='top',fill='both',expand=True)
     self.frame2.pack(side='top',fill='both',expand=True)
     self.frame3.pack(side='top',fill='both',expand=True)
     self.frame4.pack(side='top',fill='both',expand=True)
     self.frame5.pack(side='top',fill='both',expand=True)
     self.frame6.pack(side='top',fill='both',expand=True)
     self.frame7.pack(side='top',fill='both',expand=True)
     self.frame8.pack(side='top',fill='both',expand=True)
     self.frame9.pack(side='top',fill='both',expand=True)

     return 0;
    
   
   def addV_in_g2(self):
     global g2
     global key2
     #node = int(self.F2.get())
     node = key2
     key2+=1
     nodeweight = int(self.G2.get())    
     g2.addVertex(node,nodeweight)
     self.graph2()


   def addE_in_g2(self):
     global g2
     global key2
     edgeV1 = int(self.H2.get())
     edgeV2 = int(self.I2.get())
     edgeweight = int(self.J2.get())
     if edgeV1 not in g2.vertList:
         key = key2
	 key2+=1
         nv = g2.addVertex(key,1)
     if edgeV2 not in g2.vertList:
         key = key2
         key2+=1
         nv = g2.addVertex(key,1)

     if g2.vertList[edgeV1] not in g2.vertList[edgeV2].connectedTo:
        g2.addEdge(edgeV1,edgeV2,edgeweight)
     else:
        tkMessageBox.showinfo("Sorry", "Edge alredy inseted")
     
     #g2.addEdge(edgeV1,edgeV2,edgeweight)
     self.graph2()  
     return 0;



   def vertexCostMatrix(self):   
     global g1
     global g2
  
     length = 0
     for v in g1:
	length+=1
     l1=length
     for v in g2:
	length+=1
     l2=length-l1
     costmat = np.zeros((length,length))
     print length
     for i in range(l1):
	for j in range(l2):
		c1=g1.getVertWeight(i)
		c2=g2.getVertWeight(j)
		if (c1 >= c2):
			costmat[i,j]= c1-c2
		else:
			costmat[i,j]= c2-c1
     j=l2
     for i in range(l1):
	for j in range(length):
		if((j-l2)==i):
			costmat[i,j]= g1.getVertWeight(i)
			costmat[i,j]= g1.vertList[i].getCost()
                        

		elif(j>=l2):
			costmat[i,j]=500
     for i in range(length):
	for j in range(l2):
		if((i-l1)==j):
			costmat[i,j]= g2.getVertWeight(j)
		elif(i>=l1):
			costmat[i,j]=500
     costmat1=costmat
     
     print(costmat1)
     starred = munkeres(costmat1,length)
     print("------------------starred-----------")
     print(starred)




   def edgeCostMatrix(self):   
     global g1
     global g2
     
    
     self.frame.destroy()
     self.parent.title("Nodes" )
     self.frame = Frame(self.parent,background="white")
     fbg= "white"
     abg="#f92727"
     mybg="orange"
     self.frame1 = Frame(self.frame,background=fbg)
     self.frame2 = Frame(self.frame,background=fbg)
     self.frame3 = Frame(self.frame,background=fbg)
     self.frame4 = Frame(self.frame,background=fbg)
     self.A1 = Label(self.frame1, text ="EDIT DISTANCE: ",bg=fbg)
     self.A1.pack(expand=True,side=LEFT)
     self.F2 = Text(self.frame1,width = 5,height =3)
     

     text = Text(self.frame3,width=100,height = 22	)
     
     
     
     
     self.sub = Button(self.frame4,text = "Back",pady=10,command=self.main2,width = 10,activebackground=abg,bg=mybg,relief="groove")
     self.sub.pack(expand=True)
    
     

     length = 0
     for v in g1:
	length+=1
     l1=length
     for v in g2:
	length+=1
     l2=length-l1
     costmat = np.zeros((length,length))
     print length
     for i in range(l1):
	for j in range(l2):
		c1=g1.getVertWeight(i)
		c2=g2.getVertWeight(j)
		if (c1 >= c2):
			costmat[i,j]= c1-c2
		else:
			costmat[i,j]= c2-c1
     j=l2
     for i in range(l1):
	for j in range(length):
		if((j-l2)==i):
			costmat[i,j]= g1.getVertWeight(i)
			costmat[i,j]= g1.vertList[i].getCost()
                        

		elif(j>=l2):
			costmat[i,j]=500
     for i in range(length):
	for j in range(l2):
		if((i-l1)==j):
			costmat[i,j]= g2.getVertWeight(j)
		elif(i>=l1):
			costmat[i,j]=500
     

     for i in range(l1):
       for j in range(length):
         if((j-l2)==i):
           sum=0
           for k in g1.vertList[i].connectedTo:
             sum+=g1.vertList[i].connectedTo[k]
           costmat[i,j]+=sum
     for i in range(length):
       for j in range(l2):
         if((i-l1)==j):
           sum=0
           for k in g2.vertList[j].connectedTo:
             sum+=g2.vertList[j].connectedTo[k]
           costmat[i,j]+=sum






     





     lengthList1 = {}
     lengthList2 = {}
     length = 0
     for v in g1.vertList:
        lengthList1[v] = 0
        length=0
	for e in g1.vertList[v].connectedTo:
          length+=1
        lengthList1[v] = length
        
     
     length = 0
     for v in g2.vertList:
        lengthList2[v] = 0
        length=0
	for e in g2.vertList[v].connectedTo:
          length+=1
        lengthList2[v] = length
     

     l1 =0
     for v in g1:
	l1+=1

     
     l2 =0
     for v in g2:
	l2+=1

     
     
     for i in range(l1):
       for j in range(l2):
         m=0;n=0;
         #print("length--",lengthList1[i],lengthList2[j])
	 ecostmat = np.zeros((lengthList1[i]+lengthList2[j],lengthList1[i]+lengthList2[j]))
         for k in g1.vertList[i].connectedTo:
           n=0
           for l in g2.vertList[j].connectedTo:
	     c1 = g1.vertList[i].connectedTo[k]
	     c2 = g2.vertList[j].connectedTo[l]    
             if (c1 >= c2):
                ecostmat[m,n]=c1-c2
             else:
                ecostmat[m,n]=c2-c1
             n+=1
           m+=1
         p=0
         for k in g1.vertList[i].connectedTo:
           for q in range(lengthList1[i]+lengthList2[j]):
             if((p+lengthList2[j])==q):
               ecostmat[p,q]=g1.vertList[i].connectedTo[k]
             elif(q>=lengthList2[j]):
               ecostmat[p,q]=500
           p+=1
         q=0
         for k in g2.vertList[j].connectedTo:
           for p in range(lengthList1[i]+lengthList2[j]):
             if((q+lengthList1[i])==p):
               ecostmat[p,q]=g2.vertList[j].connectedTo[k]
             elif(p>=lengthList1[i]):
               ecostmat[p,q]=500
           q+=1
         ecostmat1=np.zeros((lengthList1[i]+lengthList2[j],lengthList1[i]+lengthList2[j]))
         for p in range(lengthList1[i]+lengthList2[j]):
           ecostmat1[p,:]=ecostmat[p,:]
         starred = munkeres(ecostmat1,lengthList1[i]+lengthList2[j])
         print(i,j)
         print(ecostmat)
         print("####################################")
         print(starred)
         print("####################################")
         value=0

       	 

         for p in range(lengthList1[i]+lengthList2[j]):
           for q in range(lengthList1[i]+lengthList2[j]):
             if(starred[p,q] == 1):
               value+=ecostmat[p,q]
         costmat[i,j] += value
     


     print("---------------------------costmat--------------------")
     print costmat
     
     inf="inf"
     text.insert(INSERT, "-----------------------Cost Matrix----------------------------------------- \n")
     for i in range(l1+l2):
       for j in range(l1+l2):
         if(costmat[i,j]==500):
           text.insert(INSERT, "%s  "%(inf))
         else:
           text.insert(INSERT, "%d  "% (costmat[i,j])) 
       text.insert(INSERT,"\n")
     #text.insert(INSERT,"-----------------------------------------------------\n")

     costmatr=np.zeros((l1+l2,l1+l2))
     for i in range(l1+l2):
       costmatr[i,:]=costmat[i,:]     

     finalmat = munkeres(costmatr,l1+l2)
     print finalmat
     
     text.insert(INSERT, "-----------------------Assignment Pairs------------------------------------ \n")
     for i in range(l1+l2):
       for j in range(l1+l2):
         text.insert(INSERT, "%d  "% (finalmat[i,j])) 
       text.insert(INSERT,"\n")
     #text.insert(INSERT,"-----------------------------------------------------\n")


     print 
     value=0
     for p in range(l1+l2):
        for q in range(l1+l2):
          if(finalmat[p,q] == 1):
            value+=costmat[p,q]
     print value
         
     self.frame.pack()
     self.F2.insert(INSERT,"%s"%(value))
     self.F2.pack(side=RIGHT)
     text.pack()
     self.frame1.pack(side='top',fill='both',expand=True)
     self.frame2.pack(side='top',fill='both',expand=True)
     self.frame3.pack(side='top',fill='both',expand=True)
     self.frame4.pack(side='top',fill='both',expand=True)
     
     
     #for i in range(l1):
     #  for j in g1.vertList[i].connectedTo:
     #    print("##",j,"##",g1.vertList[i].connectedTo[j])
     #print("hii bharat")



     #for v in vertList:
	#for e in g2.vertList[v].connectedTo:
         # length[e]


class Index:
	def __init__(self,x,y):
		self.i = x
		self.j = y
	def getI(self):
		return self.i
	def getJ(self):
		return self.j
	def writeI(self,x):
		self.i = x
	def writeJ(self,y):
		self.j = y
z = Index(-1,-1)


def done(costmat,starred,covered,primed,k):
	return starred

def step3(costmat,starred,covered,coveredrow,primed,k):
	global z
	series=[]
	series.append(z)
	length = len(series) - 1
	done=False
	while(done == False):
		star=0
		l=-1
		for i in range(k):
			if(starred[i,series[length].getJ()]==1):
				star=1
				j=i
		if(star==1):
			z1=Index(j,series[length].getJ())
			series.append(z1)
			length=len(series) - 1
			l=z1.getI()
		else:
			done = True
		if(done == False):
			for j in range(k):
				if(starred[l,j] == 2):
					p=l
					q=j
			z2=Index(p,q)
			series.append(z2)
			length=len(series) - 1
	for ind in series:
		if(starred[ind.getI(),ind.getJ()]==1):
			starred[ind.getI(),ind.getJ()]=0
		else:
			starred[ind.getI(),ind.getJ()]=1
	for i in range(k):
		for j in range(k):
			if(starred[i,j]==2):
				starred[i,j]=0
	for i in range(k):
		coveredrow[i,:]=0
	for j in range(k):
		covered[:,j]=0
	return step1(costmat,starred,covered,coveredrow,primed,k)



def step2(costmat,starred,covered,coveredrow,primed,k):
	global z
	uncov_zero=0
	p=-1
	q=-1
	for i in range(k):
		for j in range(k):
			if(costmat[i,j] == 0 and covered[i,j] == 0 and coveredrow[i,j] == 0):
				p=i
				q=j
				uncov_zero=1
				break
		else:
			continue
		break
	if(uncov_zero==1):
		starred[p,q]=2
		star=0
		for i in range(k):
			if(starred[p,i]==1):
				star=1
				q=i
				break
		if(star==0):
			z.writeI(p)
			z.writeJ(q)
			return step3(costmat,starred,covered,coveredrow,primed,k)
		else:
			coveredrow[p,:]=1
			covered[:,q]=0
			return step2(costmat,starred,covered,coveredrow,primed,k)
	else:
		emin=500
		for i in range(k):
			for j in range(k):
				if(covered[i,j]==0 and coveredrow[i,j]==0 and emin>costmat[i,j]):
					emin=costmat[i,j]
		for i in range(k):
			if((0 in coveredrow[i,:]) == False):
				costmat[i,:] += emin
		for j in range(k):
			if((1 in covered[:,j]) == False):
				costmat[:,j] -= emin
		return step2(costmat,starred,covered,coveredrow,primed,k)


def step1(costmat,starred,covered,coveredrow,primed,k):
	cov=0
	for i in range(k):
		for j in range(k):
			if((starred[i,j])==1):
				covered[:,j]=1
	for j in range(k):
		if((0 in covered[:,j])==False):
			cov+=1
	if(cov == k):
		return done(costmat,starred,covered,primed,k)
	else:
		return step2(costmat,starred,covered,coveredrow,primed,k)

def munkeres(costmat,k):
	for i in range(k):
		minimum=min(costmat[i,:])
		costmat[i,:]-=minimum
	starred = np.zeros((k,k))
	covered = np.zeros((k,k))
	coveredrow = np.zeros((k,k))
	primed = np.zeros((k,k))
	for i in range(k):
		for j in range(k):
			if(costmat[i,j]==0 and covered[i,j]==0 and coveredrow[i,j]==0):
				starred[i,j]=1
				covered[:,j]=1
				coveredrow[i,:]=1
	for i in range(k):
		coveredrow[i,:]=0
	for j in range(k):
		covered[:,j]=0
	return step1(costmat,starred,covered,coveredrow,primed,k)



	



def main(): 
  window = Tk()
  canvas = Canvas(width = 200, height = 170, bg = 'white')
  canvas.pack(expand = NO, fill = BOTH)
  image = ImageTk.PhotoImage(file = "header.jpg")
  canvas.create_image(0, 0, image = image, anchor = NW)
  
  uiObject = UI(window)
  fbg="white"
  window.configure(background=fbg)
  window.geometry("800x600")
  window.title("Graph Edit Distance")
  window.mainloop()

main()
