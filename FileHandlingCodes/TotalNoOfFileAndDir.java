import java.io.*;

class TotalNoOfFileAndDir
{
  public static void main(String[] args) throws IOException
  {
    int count = 0 ;
    File f = new File("C:\\Users\\ItsTRD\\Desktop\\3rd Year\\MyCode\\JavaCodes\\FileHandlingCodes");
    String[] s = f.list();
    for(String s1:s)
    {
      count++;
      System.out.println(s1);
    }
    System.out.println("The TotalNoOfFileAndDir : " + count);
  }
}
