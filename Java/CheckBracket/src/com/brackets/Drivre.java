package com.brackets;
import java.util.Scanner;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
public class Drivre {
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		int no = sc.nextInt();
		Brackets b = new Brackets();
		for(int i=0 ; i<no ; i++) {
			String s = sc.next();
			System.out.println(b.balanced(s));
		}
		sc.close();
//		BufferedReader reader1 = new BufferedReader(new FileReader("C:\\Users\\ItsTRD\\Desktop\\JavaFuckingCodes\\JavaIsFun\\CheckBracket\\bin\\com\\brackets\\new5.txt"));
//        
//        BufferedReader reader2 = new BufferedReader(new FileReader("C:\\Users\\ItsTRD\\Desktop\\JavaFuckingCodes\\JavaIsFun\\CheckBracket\\bin\\com\\brackets\\new6.txt"));
//         
//        String line1 = reader1.readLine();
//         
//        String line2 = reader2.readLine();
//         
//        boolean areEqual = true;
//         
//        int lineNum = 1;
//         
//        while (line1 != null || line2 != null)
//        {
//            if(line1 == null || line2 == null)
//            {
//                areEqual = false;
//                 
//                break;
//            }
//            else if(! line1.equalsIgnoreCase(line2))
//            {
//                areEqual = false;
//                 
//                break;
//            }
//             
//            line1 = reader1.readLine();
//             
//            line2 = reader2.readLine();
//             
//            lineNum++;
//        }
//         
//        if(areEqual)
//        {
//            System.out.println("Two files have same content.");
//        }
//        else
//        {
//            System.out.println("Two files have different content. They differ at line "+lineNum);
//             
//            System.out.println("File1 has "+line1+" and File2 has "+line2+" at line "+lineNum);
//        }
//         
//        reader1.close();
//         
//        reader2.close();
	}
}
