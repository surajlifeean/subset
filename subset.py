#this code gives all subset of any given array
def all_subsets(given_array):
    subset=[None,None,None,None]
    helper(given_array,subset,0)

#generating the subsets
def helper(given_array, subset, i):
    if(i==len(given_array)):
        print_set(subset)
    else:
        subset[i]=None
        helper(given_array, subset, i+1)
        subset[i]=given_array[i]
        helper(given_array, subset, i+1)

#this function is to print the values of set excluding None 
def print_set(subset):
    a=list(filter(lambda x: x is not None, subset))
    print(a)

#passing array to the all_subsets() function
all_subsets([1,2,3,5])
