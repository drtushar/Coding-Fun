package com.quickFind;

public class Driver {
	
	
	/**
	 * Quick Find is also called eager find
	 * Data structure : Integer array id[] of size N
	 * Two nodes p and q are said to be connected iff they have the same id
	 * 
	 * 		   0  1  2  3  4  5  6  7  8  9
	 * id[] :: 0  1  1  8  8  0  0  1  8  8
	 * Here nodes 0, 5 and 6 are connected nodes.
	 * nodes 1, 2 and 7 are connected.
	 * nodes 3, 4, 8, and 9 are connected.
	 * 
	 * find() : o(1) ie only compares value at particular 2 indices.
	 * union() : o(n) ie for N union operations complexity will be quadratic ie o(n2)
	 * constructor : o(n) : for initialization of array.
	 * 
	 * */
	
	public static void main(String[] args) {
		QuickFind qf = new QuickFind(10);
		qf.union(4, 3);
		qf.union(3, 8);
		qf.union(6, 5);
		qf.union(9, 4);
		qf.union(2, 1);
		qf.union(8, 9);
		qf.union(5, 0);
		qf.union(7, 2);
		qf.union(1, 6);
		qf.printArray();
		
	}

}
