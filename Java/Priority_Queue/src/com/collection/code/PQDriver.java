package com.collection.code;

import java.util.*;

public class PQDriver {
	public static void main(String[] args) {
		PriorityQueue<String> pq = new PriorityQueue<String>();
		pq.add("AAAA");
		pq.add("AA");
		pq.add("AAA");
		pq.add("AAA");
		pq.add("AAAA");
		System.out.print(pq.size() + "\n");
		for(int i = 0 ; i<5 ; i++) {
			System.out.print(pq.poll() + " ");
		}
	}
}
