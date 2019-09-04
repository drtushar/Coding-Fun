package com.coding.code;

import java.util.ArrayList;
import java.util.ListIterator;

@FunctionalInterface
interface Al1{
	void printArraylist(ArrayList<Integer> al);
}


public class ArrayListDriver {
	public static void main(String[] args) {
		ArrayList<Integer> al = new ArrayList<Integer>();
		for(int i = 0 ; i<10 ; i++) {
			al.add(i);
		}
		Al1 a = (ArrayList<Integer> b) -> {
			ListIterator<Integer> i = b.listIterator();
			while(i.hasNext()) {
				System.out.print((Integer)i.next() + " ");
			}
		};
		
		a.printArraylist(al);
		System.out.println("\nPrinting Using getter");
		for(int i = 0 ; i<al.size() ; i++) {
			System.out.print(al.get(i) + " ");
		}
	}
}
