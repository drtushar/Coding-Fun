package com.quickFind;

public class QuickFind {
	
	private int id[];
	
	public QuickFind(int n) {
		//At Initial stage every element is connected to itself.
		id = new int[n];
		for(int i = 0; i<n ; i++)
			id[i] = i;
	}
	
	public boolean find(int a, int b) {
		//Two elements are said to  be connected if both have id no at there index.
		return id[a] == id[b];
	}
	
	public void union(int first, int second) {
		//to connect 2 nodes the idea is to make id of first element equal to second.
		//Due to this we have to check over whole array for id of second and make it equal to that of first.
		//Hence now all nodes connected to first and second are also connected.
		int a = id[second];
		for(int i = 0; i<id.length; i++) {
			if(id[i] == a)
				id[i] = id[first];
		}
	}
	
	public void printArray() {
		for(int i = 0 ; i<id.length; i++) {
			System.out.print(id[i] + " ");
		}
	}
}
