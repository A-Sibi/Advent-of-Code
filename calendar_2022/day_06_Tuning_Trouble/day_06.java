package day_06_Tuning_Trouble;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class day_06 {
    
    public static void main(String[] args) throws FileNotFoundException {
        File myObj = new File("data/day6.txt");
        List<String> dataRowsAL = new ArrayList<String>();
        Scanner myReader = new Scanner(myObj);
        while (myReader.hasNextLine()) {
            dataRowsAL.add(myReader.nextLine());
        }
        myReader.close();
        String[] dataRows = new String[ dataRowsAL.size() ];

        // sacuvani podaci it txt fajla kao: dataRows String[];
        dataRowsAL.toArray( dataRows );
        String input = dataRows[0];

        // char[] lastFour = new char[4];
        // lastFour[0] = input.charAt(0);
        // lastFour[1] = input.charAt(1);
        // lastFour[2] = input.charAt(2);
        // lastFour[3] = input.charAt(3);
        // int counter = 3;
        
        char[] message = new char[14];
        for (int i = 0; i < 14; i++) {
            message[i] = input.charAt(i);
        }
        int counter = 13;

        
        boolean valid = true;

        while (counter != input.length()) {

            // check the last 4 (13) symbols
            valid = true;
            for (int i = 0; i < message.length; i++) {
                for (int j = 0; j < message.length; j++) {
                    if (i != j && message[i] == message[j]) {
                        valid = false;
                        break;
                    }
                }
                if (!valid) {
                    break;
                }
            }
            if (valid) {
                System.out.println(counter + 1);
                break;
            }

            // insert next symbol
            counter++;
            for (int i = 0; i < 13; i++) {
                message[i] = message[i+1];
            }
            message[13] = input.charAt(counter);


        }
        System.out.println("End of string.");
        
    }
}
