package com.coding.code;

import java.util.Vector;
import java.util.Collections;
import java.util.Enumeration;


/**
 * 1. Vector implements dynamic arrays.
 * 	  Like an array it can access components using integer index.
 * 2. Vector is synchronized and have legacy methods which collection framework
 *    does not have.
 * 3. It extends AbstractList and implements List.    
 * */

public class VectorDriver {
	public static void main(String[] args) {
		Vector<Integer> v = new Vector<Integer>();
		for(int i = 0; i < 10 ; i++) {
			v.addElement(i);
		}
		
		Enumeration e = v.elements();
		int i = 0;
		while(e.hasMoreElements()) {
			System.out.print(e.nextElement() + " " + v.get(i) + "  ");
			i++;
		}
		Collections.reverse(v);
		Collections.sort(v);
		System.out.println(v);
	}
}
