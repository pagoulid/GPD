from sympy import CRootOf, expand, groebner, LC, LT, LM, N, quo, gcd
from sympy import reduced, rem, roots, simplify, solve, nsolve, symbols
###############################UNMARK A SAMPLE BELOW TO TEST######################################################## 
def GPD_meth(poly,var,div,myorder):
    x,y=symbols('x y')
    zero=symbols('0')
    dlen=len(div) # num of dividents
    q=[]
    NotDivide = False
    divoccur = True
    
    for k in range(0,len(div)): # init list of quos
        q.append(zero)
###############################################
    for i in range(0,len(div)):
        #print("iteration",i)
        if poly == 0 :
            break
        
        
        if NotDivide == True :
            NotDivide = False
        
        while NotDivide == False :
            LTP=LT(poly,var, order=myorder) # check if LTD divides LTP
            LTD=LT(div[i], var, order=myorder)
            #print("check3")
           
            
            
            if quo(LTP,LTD)!= 0  and rem(LTP,LTD)== 0:
                #print("leading tems divisor/divident0:",LTP,LTD)
                divLT=simplify(LTP/LTD) #works thatsgood
                
                #print(divLT)
        ##########check changes in quo rem################
                if q[i] == zero : # if quo is initialized
                    q[i]=simplify(divLT)
                else:
                    q[i]=simplify(q[i] + divLT)  
                poly=simplify(poly - simplify(divLT*div[i]))
                #print("check0",poly)
                #print("new poly,new quo",poly,q[i])
        ##################################################
            else:
                NotDivide = True
                break
    return poly,q # final results

##################################################
  
###############################UNMARK A SAMPLE TO TEST########################################################  
  
'''    
############################
x, y = symbols('x, y')

###########Sample#########
p = x**2*y + x* y**2 + y**2
q1 = x * y - 1
q2 = y**2 - 1
div_list=[q1,q2]
symbol=[y,x]
order='grlex'

print('reduce p by [q1, q2] = ', reduced(p, [q1, q2], [y, x]), '\n')
###########################
'''
'''
###########Sample#########
p = x**2 * y - y
q1 = x * y - x
q2 = x**2 - y
div_list=[q1,q2]
symbol=[y,x]
order='lex'
print('reduce p by [q1, q2] = ', reduced(p, [q1, q2], [y, x]), '\n')
###########################
'''

'''
###########Sample#########
p = x**3  + 2*x**2*y - 5*x + y**3 -3*y
q1 = x * y - 1
q2 = x**2 + y**2 - 4
div_list=[q2,q1]
symbol=[y,x]
order='lex'
print('reduce p by [q1, q2] = ', reduced(p, [q1, q2], [y, x]), '\n')
###########################
'''

'''
###########Sample#########
p = 2*x**3  + x**2 + x*y 
q1 = x **3 - x*y
q2 = x + y**2
div_list=[q1,q2]
symbol=[y,x]
order='lex'
print('reduce p by [q1, q2] = ', reduced(p, [q1, q2], [y, x]), '\n')
###########################
'''





'''
###########Sample#########
p = x * y**2 + 1
q1 = x * y + 1
q2 = y + 1
div_list=[q1,q2]
symbol=[y,x]
order='lex'
print('reduce p by [q1, q2] = ', reduced(p, [q1, q2], [y, x]), '\n')
###########################
'''





'''
########Sample##############
p = x**5 - 2*x**4 + 5*x**3 + 2*x**2 - 4*x + 10
q1 = x**3 - x**2 + 3*x + 5
div_list=[q1]
symbol=[y,x]
order='lex'
print('reduce p by q1:',quo(p,q1),rem(p,q1))
##########################
'''


'''
########Sample##############
q1 = x**3 * y + y**2 - 1
p = x**3 + 3*y - 1
div_list=[q1]
symbol=[y,x]
order='lex'
print('reduce p by q1:',quo(p,q1),rem(p,q1))
##########################
'''





frem,fquos=GPD_meth(p,symbol,div_list,order)
print('Final Remainder :',frem)
print('Final Quotient :', fquos)



print('######################GPD####################################################')


