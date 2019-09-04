package com.coding.linkedList;

import java.util.LinkedList;
import java.util.ListIterator;

/**
 * Linked List are linear data structures where the elements are 
 * not stored in contiguous locations and every element is a separate 
 * object with a data part and address part.
 * Advantage : Due to the dynamicity and ease of insertions and deletions, they are preferred over the arrays.
 * Disadvantage : It also has few disadvantages like the nodes cannot be accessed directly instead we need 
 * to start from the head and follow through the link to reach to a node we wish to access.
 * To store the elements in a linked list we use a doubly linked list which provides a linear data structure
 * 
 *  Constructor
 *  LinkedList() : Empty list.
 *  LinkedList(Collection c) : List Initialized to collection c
 * */

@FunctionalInterface
interface Ll{
	void printLinkedList(LinkedList<Integer> l);
}

public class LinkedListDriver {
	public static void main(String[] args) {
		LinkedList<Integer> l = new LinkedList<Integer>();
		for(int i = 0 ; i < 10 ; i++ ) {
			l.add(i);
		}
		
		Ll ll = (LinkedList<Integer> linkedlist) -> {
			ListIterator<Integer> i = linkedlist.listIterator();
			while(i.hasNext()) {
				System.out.print((Integer)i.next() + " ");
			}
		};
		ll.printLinkedList(l);
		
		System.out.println("\n Printing LL using getter");
		for(int i = 0 ; i< l.size() ; i++) {
			System.out.print(l.get(i) + " ");
		}
	}
}
