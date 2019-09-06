import java.io.*;
class FileConstructors
{
  public static void main(String[] args) throws IOException
  {
      //Constructor 1
      File d1 = new File("1");
      d1.mkdir();
      //Constructor 2
      File d2 = new File("1", "2");
      d2.mkdir();
      File d3 = new File("1/2" , "3");
      d3.mkdir();
      //Constructor 3
      File d4 = new File(d3 ,"4");
      File d5 = new File(d4 ,"5");
      d4.mkdir();
      d5.mkdir();
      File f = new File(d5 ,"HelloBigshow.txt");
      f.createNewFile();
  }
}
