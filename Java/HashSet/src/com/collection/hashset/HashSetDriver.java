package com.collection.hashset;

import java.util.HashSet;
/**
 * As it implements the Set Interface, duplicate values are not allowed.
 * Underlying data structure for HashSet is hashtable.
 * Objects that you insert in HashSet are not guaranteed to be inserted 
 * in same order. Objects are inserted based on their hash code.
 * NULL elements are allowed in HashSet.
 * */
class O{
	int i;
	String j;
	
	O(int i,String j){
		this.i = i;
		this.j = j;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + i;
		result = prime * result + ((j == null) ? 0 : j.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		O other = (O) obj;
		if (i != other.i)
			return false;
		if (j == null) {
			if (other.j != null)
				return false;
		} else if (!j.equals(other.j))
			return false;
		return true;
	}

	@Override
	public String toString() {
		return "O [i=" + i + ", j=" + j + "]";
	}
	
	
		
}

public class HashSetDriver {
	public static void main(String[] args) {
		HashSet<O> h = new HashSet<O>();
		
		O s = new O(1,"Tush");
		O s2 = new O(1,"Tush");
		
		h.add(s);
		h.add(s2);
		System.out.print(s.hashCode() + " " + s2.hashCode());
		
		System.out.print(h);
	}
}
