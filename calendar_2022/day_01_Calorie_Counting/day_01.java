package day_01_Calorie_Counting;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class day_01 {

    public static void main(String[] args) throws Exception {

        File myObj = new File("data/day1.txt");
        List<String> dataRowsAL = new ArrayList<String>();
        Scanner myReader = new Scanner(myObj);
        while (myReader.hasNextLine()) {
            dataRowsAL.add(myReader.nextLine());
        }
        myReader.close();
        String[] dataRows = new String[ dataRowsAL.size() ];

        // sacuvani podaci it txt fajla kao: dataRows String[];
        dataRowsAL.toArray( dataRows );

        
        int currMax1 = 0;
        int currMax2 = 0;
        int currMax3 = 0;
        int s = 0;
        for (String el : dataRows) {
            // obrada input podataka iz txt fajla:
            if (el == "") {
                if (s >= currMax1) {
                    currMax3 = currMax2;
                    currMax2 = currMax1;
                    currMax1 = s;
                } else if (s >= currMax2) {
                    currMax3 = currMax2;
                    currMax2 = s;
                } else if (s >= currMax3) {
                    currMax3 = s;
                }
                s = 0;
                continue;
            }
            s += Integer.parseInt(el);

        }
        System.out.println(currMax1 + currMax2 + currMax3);
    }
}