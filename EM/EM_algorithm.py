import random
import math

def em_algo_run(values,k,varience_value,num):
    pass
    prior=[]
    mean=[]
    variance=[]
    postrior_of_variable=[[]]
    prior_of_variable=[[]]
    count=0
    while(True):
        prior.append(1/k)
        variance.append(varience_value)
        mean.append(values[random.randint(1, len(values))-1])
        count=count+1;
        if k==count:
            break;
    print("values",values)
    print("variance",variance)
    print("mean",mean)
    count=0
    while True:
        prior, mean, variance, postrior_of_variable, prior_of_variable=em_algo(values, k, varience_value, prior, mean, variance, postrior_of_variable, prior_of_variable)
        print("----------------")
        print(prior)
        print(mean)
        print(variance)
        print("-----------------")
        count=count+1
        if count==num:
            break

def em_algo(values,k,varience_value,prior,mean,variance,postrior_of_variable,prior_of_variable):
    count=0
    postrior_of_variable=[[]]
    prior_of_variable=[[]]
    sum_prior=[]
    sum_prior_with_value=[]
    sum_prior_with_variance=[]
    count_of_var_cluster=[]
    while(True):
        count=count+1;
        sum_prior.append(0)
        count_of_var_cluster.append(0)
        sum_prior_with_value.append(0)
        sum_prior_with_variance.append(0)
        if k==count:
            break;
    #print(sum_prior)
    #print(sum_prior_with_value)
    #print(sum_prior_with_variance)
    count=0
    count_k=0
    for cur in values:
        if count!=0:
            temp=[]
            temp1=[]
            postrior_of_variable.append(temp)
            prior_of_variable.append(temp1)
        sum_value=0
        while True:
            root_of_2_pi_var=round((2*3.14*pow(variance[count_k],2))**(1/2),4)
            #print(root_of_2_pi_var)
            exp_gausian_1=round(math.pow((values[count]-mean[count_k]),2),4)
            #print(exp_gausian_1)
            exp_gausian_2=2*math.pow(variance[count_k],2)
            #print(exp_gausian_2)
            if exp_gausian_2!=0:
                exp_gausian=round((-(exp_gausian_1)/(exp_gausian_2)),4)
            else:
                exp_gausian=0
            #print(exp_gausian)
            if root_of_2_pi_var!=0:
                prior_of_variable[count].insert(count_k,round((math.exp(exp_gausian)/root_of_2_pi_var),4))
            else:
                prior_of_variable[count].insert(count_k,0);
            #print(prior_of_variable[count][count_k])
            sum_value=sum_value+(prior_of_variable[count][count_k]*prior[count_k])
            #print(sum_value)
            count_k=count_k+1
            if count_k==k:
                break
        #print(sum_value)
        count_k=0
        while True:
            if(sum_value!=0):
                #print(prior_of_variable[count][count_k],prior[count_k],sum_value)
                postrior_of_variable[count].insert(count_k,round((prior_of_variable[count][count_k]*prior[count_k]/sum_value),4))
            else:
                postrior_of_variable[count].insert(count_k,0)
            if postrior_of_variable[count][count_k]!=0:
                count_of_var_cluster[count_k]=count_of_var_cluster[count_k]+1
            #print(postrior_of_variable[count][count_k])
            #print(count,count_k,postrior_of_variable[count][count_k]);
            sum_prior[count_k]=sum_prior[count_k]+postrior_of_variable[count][count_k]
            #print(sum_prior[count_k])
            sum_prior_with_value[count_k]=sum_prior_with_value[count_k]+postrior_of_variable[count][count_k]*values[count]
            #print(sum_prior_with_value[count_k])
            count_k=count_k+1
            if count_k==k:
                break
        #print(sum_prior)
        #print(sum_prior_with_value)
        count_k=0
        count=count+1
    
    count_k=0
    while(True):
        if(sum_prior[count_k]!=0):
            mean[count_k]=round((sum_prior_with_value[count_k]/sum_prior[count_k]),4)
        else:
            mean[count_k]=0
        #print(mean[count_k])
        prior[count_k]=round((sum_prior[count_k]/len(values)),4)
        #print(prior[count_k])
        count_k=count_k+1
        if count_k==k:
            break
    count_k=0
    count=0
    for cur in values:
        while True:
            sum_prior_with_variance.insert(count_k,sum_prior_with_variance[count_k]+postrior_of_variable[count][count_k]*(math.pow((values[count]-mean[count_k]),2)))
            #print(sum_prior_with_variance[count_k])
            count_k=count_k+1
            #print(count_k,k)
            if count_k==k:
                break
        count_k=0
        count=count+1
    count_k=0
    while True:
        if sum_prior[count_k]!=0:
            variance[count_k]=round((sum_prior_with_variance[count_k]/sum_prior[count_k]),4)
        else:
            variance[count_k]=round((0),4)
        #print(variance[count_k])
        count_k=count_k+1
        if count_k==k:
            break
    return prior, mean, variance, postrior_of_variable, prior_of_variable
    #print(prior_of_variable)
    #print(postrior_of_variable)