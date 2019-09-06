import java.io.*;
class Test
{
  public static void main(String[] args) throws IOException
  {
    //Code to create file
    File f = new File("testFile.txt");
    System.out.println(f.exists());
    f.createNewFile();
    System.out.println(f.exists());
    //Code to create directory
    File d = new File("testFile");
    d.mkdir();
    System.out.println(d.exists());
  }
}
