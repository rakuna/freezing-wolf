import functions

#Definitions:
factor1 = 3
factor2 = 5
limit = 1000

#Computations:
factor1_sum =  functions.factor_summation(factor1,limit)
factor2_sum =  functions.factor_summation(factor2,limit)
factor12_sum = functions.factor_summation(factor1*factor2,limit)

#Result:
print(factor1_sum + factor2_sum - factor12_sum)
