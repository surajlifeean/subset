The code follows a recursive approche to get the subsets of a given array.
Initially the function starts with a null subset.
Once the function all_subsets receives the array it calls the helper function and then traversing the index elements one by one it is added to one of the subset starting from null set and missed on the other.



         				  {}

	  		{}
		   		  		  {2}

{}

		    	   		   {1}
	  		{1} 

		    	   		   {1,2}

    takes 1       takes 2
    adds in one   add in one set
    missed in     missed in
    other         other