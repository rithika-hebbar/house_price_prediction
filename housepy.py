
#Author: Rithika Hebbar
print("PREDICTING HOUSE PRICES USING UNIVARIATE LINEAR REGRESSION - LINEAR ALGEBRA METHOD\n")
h1=int(input("Enter the size of house 1 in Sq Ft: "))
h2=int(input("Enter the size of house 2 in Sq Ft: "))
h3=int(input("Enter the size of house 3 in Sq Ft: "))
h4=int(input("Enter the size of house 4 in Sq Ft: "))

hs=[[1,h1],[1,h2],
    [1,h3],[1,h4]]
hf=[[-40,200,-150],
    [0.25,0.1,0.4]]
    
hp=[[0 for x in range(3)] for y in range(4)]
i=0
j=0

while i<=3:
	    hp[i]=[round(hs[i][0]*hf[0][j]+hs[i][1]*hf[1][j],1),
            round(hs[i][0]*hf[0][j+1]+hs[i][1]*hf[1][j+1],1),
            round(hs[i][0]*hf[0][j+2]+hs[i][1]*hf[1][j+2],1)]
	    i=i+1
	    
print("\nThree different hypotheses were used to make predictions and they are- ")
print("Hypothesis 1: h(x)=-40+0.25x")
print("Hypothesis 2: h(x)=200+0.1x")
print("Hypothesis 3: h(x)=-150+0.4x")

print("\nThe price of the house with "+str(h1)+" Sq ft could be "+str(hp[0][0])+", "
      +str(hp[0][1])+" and "+str(hp[0][2])+" based on the hypotheses 1,2 and 3 respectively.")
print("\nThe price of the house with "+str(h2)+" Sq ft could be "+str(hp[1][0])+", "
      +str(hp[1][1])+" and "+str(hp[1][2])+" based on the hypotheses 1,2 and 3 respectively.")
print("\nThe price of the house with "+str(h3)+" Sq ft could be "+str(hp[2][0])+", "
      +str(hp[2][1])+" and "+str(hp[2][2])+" based on the hypotheses 1,2 and 3 respectively.")
print("\nThe price of the house with "+str(h4)+" Sq ft could be "+str(hp[3][0])+", "
      +str(hp[3][1])+" and "+str(hp[3][2])+" based on the hypotheses 1,2 and 3 respectively. \n\n")
print("Example from Machine Learning course by Andrew Ng on Coursera")
