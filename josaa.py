DICTIONARY={1:"Andra Pradesh" ,2:"Arunachal Pradesh" ,3:"Assam" ,4:"Bihar" ,5:"Chhattisgarh" ,6:"Goa" ,7:"Gujarat" ,8:"Haryana" ,9:"Himachal Pradesh" ,10:"Jammu and Kashmir" ,11:"Jharkhand" ,12:"Karnataka" ,13:"Kerala" ,14:"Madya Pradesh" ,15:"Maharashtra" ,16:"Manipur" ,17:"Meghalaya" ,18:"Mizoram" ,19:"Nagaland" ,20:"Orissa" ,21:"Punjab" ,22:"Rajasthan" ,23:"Sikkim" ,24:"Tamil Nadu" ,25:"Telangana" ,26:"Tripura" ,27:"Uttaranchal" ,28:"West Bengal" ,29:"Delhi" ,}
nani=0
#to find the collage 
def k(fin,y):
	i=open(fin,"r")
	line=i.readline()	
	while(line!=""):	
		words=line.split("  ")		
		if  y < int(words[5]):
			print("CHOICE NUMBER:",end="")
			print(words[0])
			print ("NAME OF THE INSTITUTION:",end="")
			print (words[1])
			print ("PROGRAMME:",end="")
			print (words[2])
			print ("COURSE:",end="")
			print (words[3])
			print ("QUOTA:",end="")
			print (words[4])
			print ("OPENING RANK:",end="")
			print (words[5])
			print ("CLOSING RANK:",end="")
			print (words[6])
			nani=1
			print("*******************************************************************************")
		elif  (y > int(words[5])) and (y< int(words[6])):
			print("CHOICE NUMBER:",end="")
			print(words[0])
			print ("NAME OF THE INSTITUTION:",end="")
			print (words[1])
			print ("PROGRAMME:",end="")
			print (words[2])
			print ("COURSE:",end="")
			print (words[3])
			print ("QUOTA:",end="")
			print (words[4])
			print ("OPENING RANK:",end="")
			print (words[5])
			print ("CLOSING RANK:",end="")
			print (words[6])
			nani=1
			print("*******************************************************************************")		
		line=i.readline()
	i.close()
	
	
#SORTING BASED ON PROGRAMME
def prog(fin,y,h):
	i=open(fin,"r")
	line=i.readline()	
	while(line!=""):	
		words=line.split("  ")		
		if  y == words[2] and h < int(words[5]):
			print("CHOICE NUMBER:",end="")
			print(words[0])
			print ("NAME OF THE INSTITUTION:",end="")
			print (words[1])
			print ("PROGRAMME:",end="")
			print (words[2])
			print ("COURSE:",end="")
			print (words[3])
			print ("QUOTA:",end="")
			print (words[4])
			print ("OPENING RANK:",end="")
			print (words[5])
			print ("CLOSING RANK:",end="")
			print (words[6])
			nani=1
			print("*******************************************************************************") 			 
		if y == words[2] and	((h > int(words[5])) and (h< int(words[6]))):
			print("CHOICE NUMBER:",end="")
			print(words[0])
			print ("NAME OF THE INSTITUTION:",end="")
			print (words[1])
			print ("PROGRAMME:",end="")
			print (words[2])
			print ("COURSE:",end="")
			print (words[3])
			print ("QUOTA:",end="")
			print (words[4])
			print ("OPENING RANK:",end="")
			print (words[5])
			print ("CLOSING RANK:",end="")
			print (words[6])
			nani=1
			print("*******************************************************************************")			  	
		line=i.readline()
	i.close()


#SORTING BASED ON QUOTA
def quota(fin,y,h):
	i=open(fin,"r")
	line=i.readline()	
	while(line!=""):	
		words=line.split("  ")		
		if  y == words[4] and h < int(words[5]):
			print("CHOICE NUMBER:",end="")
			print(words[0])
			print ("NAME OF THE INSTITUTION:",end="")
			print (words[1])
			print ("PROGRAMME:",end="")
			print (words[2])
			print ("COURSE:",end="")
			print (words[3])
			print ("QUOTA:",end="")
			print (words[4])
			print ("OPENING RANK:",end="")
			print (words[5])
			print ("CLOSING RANK:",end="")
			print (words[6])
			nani=1
			print("*******************************************************************************") 			 
		if y == words[4] and((h > int(words[5])) and (h< int(words[6]))):
			print("CHOICE NUMBER:",end="")
			print(words[0])
			print ("NAME OF THE INSTITUTION:",end="")
			print (words[1])
			print ("PROGRAMME:",end="")
			print (words[2])
			print ("COURSE:",end="")
			print (words[3])
			print ("QUOTA:",end="")
			print (words[4])
			print ("OPENING RANK:",end="")
			print (words[5])
			print ("CLOSING RANK:",end="")
			print (words[6])
			nani=1
			print("*******************************************************************************")	
		line=i.readline()
	i.close()

#TO DISPLAY IN FILE
def display():
	fp=open("newfile.txt","w")
	x= input().split()
	hu = open('INPUT.txt', 'r').read().split('\n')
	hu.pop()
	#print(hu)
	clg = [w for w in hu if w.split()[0] in x]
	fp.write('\n'.join(clg))
	#fp.close()
		
	
#TO FIND RANK FROM INPUT
def rank(fin,y):
	i=open(fin,"r")
	line=i.readline()	
	while(line!=""):	
		words=line.split("  ")		
		if  y == words[1] or y == words[0]: 
			print ("NAME OF THE STUDENT:",end="")
			print (words[1])
			print ("ROLL NO:",end="")
			print (words[0])
			print ("QUALIFYFING STATE:",end="")
			n=int(words[2])
			print (DICTIONARY[n])
			print ("JEE MAINS MARKS:",end="")
			print (words[3])
			print ("12th CLASS EQUIVALENT:",end="")
			print (words[4])
			if(int(words[3])>89):
				print ("CONGRATULATIONS YOU ARE QUALIFIED")
			else:
			  	print ("NOT QUALIFIED BETTER LUCK NEXT TIME!!")
			print ("JEE MAINS RANK:",end="")
			print (words[5])  	
			print("*******************************************************************************")
			return 1		
		line=i.readline()
	i.close()	
flag=0
print ("\n****************************WELCOME TO JOSAA 2017******************************")
print ("ENTER YOUR NAME OR ROLL NUMBER:")
searchid=input()
ki=rank("name.txt",searchid)
if(ki==None):
	print("SORRY,YOU ARE NOT REGISTERED....")
	print("CENTRAL BOARD OF SECONDARY EDUCATION")
	flag=1

if(flag==0):
  print ("ENTER THE RANK:")
  x=int(input())
  k("INPUT.txt",x)
'''*************************************************SORTING BASED ON QUERIES*********************************************************'''  
if(flag==0):
	print("ENTER A QUERY")
	print("**PROGRAMME")
	print("**QUOTA")
	query=input()
	if(query=="programme" or query=="PROGRAMME"):
		print("ENTER A PROGRAMME")
		print("***Agricultural Engineering")
		print("***AerospaceEngineering")
		print("***Bio Technology")
		print("***CivilEngineering")
		print("***Computer Science andEngineering")
		print("***Chemical Engineering")
		print("***Carpet and Textile Technology")
		print("***ChemicalEngineering")
		print("***ElectricalEngineering")
		print("***Electrical and Electronics Engineering")
		print("***Engineering Physics")
		print("***Earth Sciences")
		print("***Food Technology")
		print("***Information Technology")
		print("***Industrial Design")
		print("***Production and IndustrialEngineering")
		print("***Mathematics and Scientific Computing")
		print("***Planning")	
		prg=input()
		print("YOU CHOOSED  %s PROGRAMME\n" %(prg)) 
		prog("INPUT.txt",prg,x)
		
		print("IF YOU ALSO WANT TO KNOW SEAT AVAILABILITY BASED ON QUOTA")
		print("ENTER QOUTA")
		print("***AI")
		print("***OS")
		print("***HS")
		query=input()
		quota("INPUT.txt",query,x)
		

	elif(query=="quota" or query=="QUOTA"):
		print("ENTER YOUR QUOTA")
		print("***AI")
		print("***OS")
		print("***HS")
		quot=input()
		quot=quot.upper()
		print("YOU CHOOSED %s QUOTA\n" %(quot))
		quota("INPUT.txt",quot,x)
		
		print("IF YOU ALSO WANT TO KNOW SEAT AVAILABILITY BASED ON PROGRAMME")
		print("ENTER PROGRAMME")
		print("***Agricultural Engineering")
		print("***AerospaceEngineering")
		print("***Bio Technology")
		print("***CivilEngineering")
		print("***Computer Science and Engineering")
		print("***Chemical Engineering")
		print("***Computer Engineering")
		print("***Carpet and Textile Technology")
		print("***ChemicalEngineering")
		print("***ElectricalEngineering")
		print("***Electrical and Electronics Engineering")
		print("***Engineering Physics")
		print("***Earth Sciences")
		print("***Food Technology")
		print("***Information Technology")
		print("***Industrial Design")
		print("***Production and IndustrialEngineering")
		print("***Mathematics and Scientific Computing")
		print("***Planning")	
		programme=input()
		prog("INPUT.txt",programme,x)
			
print("ENTER CHOICES OF COLLEGE YOU WNT TO FREEZE")		
display()

