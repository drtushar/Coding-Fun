package com.algo.sorting;

public class SelectionSort {
	
	public SelectionSort() {
		System.out.print("Fuck main Constructor\n");
	}

	int[] sort(int arrr[]) 
    { 
        int n = arrr.length; 
  
        // One by one move boundary of unsorted subarray 
        for (int i = 0; i < n-1; i++) 
        { 
            // Find the minimum element in unsorted array 
            int min_idx = i; 
            for (int j = i+1; j < n; j++) 
                if (arrr[j] < arrr[min_idx]) 
                    min_idx = j; 
  
            // Swap the found minimum element with the first 
            // element 
            int temp = arrr[min_idx]; 
            arrr[min_idx] = arrr[i]; 
            arrr[i] = temp; 
        }
        return arrr;
    } 
  
	
    // Prints the array 
    void printArray(int arrrr[]) 
    { 
        int n = arrrr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arrrr[i]+" "); 
        System.out.println(); 
    }
    
    static {
    	System.out.println("Fuck2");
    }
	{
    	System.out.println("Fuck3");
    }
	static {
    	System.out.println("Fuck4");
    }
	{
    	System.out.println("Fuck5");
    }
    
    
    // Driver code to test above 
    public final synchronized strictfp static void main(String args[]) 
    { 
        SelectionSort ob = new SelectionSort(); 
        int arr[] = {64,25,12,22,11}; 
        int[] ar = ob.sort(arr); 
        System.out.println("Sorted array"); 
        ob.printArray(arr);
        ob.printArray(ar);
        Driver d = new Driver();
        Driver dd = new Driver();
    }
    
    
    
}
