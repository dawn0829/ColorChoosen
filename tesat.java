import java.util.*;
public class tesat {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter input score:");
		while(sc.hasNext()) {
			try {
				int input = sc.nextInt();
				switch((100-input)/10) {
					case 0:
						System.out.println("GradeA");
						break;
					case 1:
						System.out.println("GradeB");
						break;
				
					case 2:
						System.out.println("GradeC");
						break;
				
					case 3:
						System.out.println("GradeD");
						break;
				
					case 4:
						System.out.println("GradeE");
						break;
					default:
						System.out.println("GradeF");
						break;
				}
			}
			catch(Exception e){
				System.out.print("ERROR INPUT");
				break;
			}
			
			System.out.print("Enter input score:");
		}
		System.out.println("END");
	}
	
}
