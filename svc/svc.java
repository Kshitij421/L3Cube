import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Timer;


public class Svc{
	
	static String Filename=null;
	
	LinkedList<String> list=new LinkedList<String>();
	HashMap<Integer,LinkedList<String>> map=new HashMap<Integer,LinkedList<String>>();
	
	
	public boolean isfilevalid(String file)
	{
		return true;
	}
	public int filelen(String file) throws IOException
	{
		int lines=0;
		String sCurrentLine="";
		BufferedReader br = new BufferedReader(new FileReader(file));
		
		while ((sCurrentLine = br.readLine()) != null) {
			lines++;
		}
		return lines;
	}
	public void commit(String file) throws IOException
	
	{
		
		Svc.Filename=file;
		
		if(map.isEmpty())
		{
			map.put(0,new LinkedList<String>());
			String sCurrentLine="";
			BufferedReader br = new BufferedReader(new FileReader(file));
			
			while ((sCurrentLine = br.readLine()) != null) {
				map.get(0).addLast(sCurrentLine);
			}
		}
		else
		{
			int newversion=map.size();
			int lastversion=newversion-1;
			map.put(newversion,new LinkedList<String>());
			String sCurrentLine="";
			if ((map.get(lastversion).size()-1==filelen(file) || map.get(lastversion).size()+1==filelen(file)&& filelen(file)<=20))
			{
				BufferedReader br = new BufferedReader(new FileReader(file));
				
				while ((sCurrentLine = br.readLine()) != null) {
					map.get(newversion).addLast(sCurrentLine);
				}
			}
			
		}
	}
		

	
	public void displayversion(int version) throws InterruptedException
	{
		if(Svc.Filename==null)
		{
			System.out.println("Invalid Version First Commit File");
			return;
		}
		LinkedList<String> list=map.get(version);
		int size=list.size();
		
		for(int i=0;i<size;i++)
		{
			System.err.println(list.get(i));
		}
		Thread.sleep(2);
		
	}
	
	public static void main(String[] args) throws IOException, InterruptedException {
		Svc svcobj=new Svc();
		
		while(true){
			
			
		System.out.println("Enter Command  \n svc <filename> \n svc <Version No>");
		Scanner sc=new Scanner(System.in);
		String Command=sc.nextLine();
		String command[]=Command.split(" ");
	
		if(command[0].equals(new String("svc"))&& !command[1].matches("^-?\\d+$"))
		{
			svcobj.commit(command[1]);
		}
		else if(command[0].equals("svc")&& command[1].matches("^-?\\d+$"))
		{
			int version=Integer.parseInt(command[1]);
			if(svcobj.map.size()<version)
			{
				System.out.println("Invalid Version No.");
				continue;
			}
			svcobj.displayversion(version);
		}
		else
		{
			System.out.println("1Invalid Input");
			break;
		}
		
		
		
		}
	}
	
}
