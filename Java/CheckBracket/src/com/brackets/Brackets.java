package com.brackets;

import java.util.*;

public class Brackets {
	
	public String balanced(String st) {
		HashMap<Character,Character> hm = new HashMap<Character,Character>();
        hm.put('}','{');
        hm.put(')','(');
        hm.put(']','[');
        char[] s = st.toCharArray();
        Stack<Character> stack = new Stack<Character>();
        for(int i = 0; i<s.length ; i++) {
        	System.out.println(stack);
            if(s[i]=='{'||s[i]=='['||s[i]=='(')
                stack.push(s[i]);
            else {
                if(!stack.empty()){
                	char c = stack.peek();
                	if(!( c==hm.get(s[i]) )) 
                		return "NO";
                	stack.pop();
                }else {
                	return "NO";
                }
            }
        }
        if(stack.empty())
        	return "YES";
        else
        	return "NO";
	}

}
