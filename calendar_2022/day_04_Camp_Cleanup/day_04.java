package day_04_Camp_Cleanup;
import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class day_04 {
    public static void main(String[] args) throws Exception {

        File myObj = new File("data/day4.txt");
        List<String> dataRowsAL = new ArrayList<String>();
        Scanner myReader = new Scanner(myObj);
        while (myReader.hasNextLine()) {
            dataRowsAL.add(myReader.nextLine());
        }
        myReader.close();
        String[] dataRows = new String[ dataRowsAL.size() ];

        // sacuvani podaci it txt fajla kao: dataRows String[];
        dataRowsAL.toArray( dataRows );

        int counterPart1 = 0;
        int counterPart2 = 0;

        for (int i = 0; i < dataRows.length; i++) {
            String[] ranges = dataRows[i].split(",");
            String[] r1 = ranges[0].split("-");
            String[] r2 = ranges[1].split("-");
            
            int a1 = Integer.parseInt(r1[0]);
            int a2 = Integer.parseInt(r1[1]);
            int b1 = Integer.parseInt(r2[0]);
            int b2 = Integer.parseInt(r2[1]);

            if ((a1 >= b1 && a2 <= b2) || (b1 >= a1 && b2 <= a2)) {
                counterPart1 += 1;
            }
            if (a1 <= b2 && a2 >= b1) {
               counterPart2 += 1; 
            }
        }
        System.out.println("Part 1: " + counterPart1);
        System.out.println("Part 2: " + counterPart2);
        
    }

}
