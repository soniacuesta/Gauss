
#Sustitución
     for k in range(n-1,-1,-1):
         m= 0.0
         for i in range(k+1,n):
             m=m+ Ab[k,i]*x[i]
             
         x[k]= (Ab[k,n] -m)/ Ab[k,k]
     
     return x
x = Gauss(A, b)
print('\n El vector solución del sistema, x=', x)