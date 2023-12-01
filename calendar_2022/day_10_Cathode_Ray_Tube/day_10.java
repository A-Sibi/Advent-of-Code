package day_10_Cathode_Ray_Tube;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
/**
 * RayTube
 */
class RayTube {

    private ArrayList<Integer> signals = new ArrayList<Integer>();
    // value[number of finished cycles]

    public RayTube() {
        this.signals.add(0, 1);
    }

    public void addx(int num) {
        this.signals.add(this.signals.get(this.signals.size() - 1));
        this.signals.add(this.signals.get(this.signals.size() - 1) + num);

    }
    
    public void noop() {
        this.signals.add(this.signals.get(this.signals.size() - 1));
    }

    public int getValueAt(int i) {
        return signals.get(i);
    }

    public void drawImage(){
        for (int i = 0; i < signals.size(); i++) {
            
            if (i % 40 == 0 && i != 0) {
                System.out.println();
            }
            if (i%40 >= getValueAt(i)-1 && i%40 <= getValueAt(i)+1) {
                System.out.print("#");
            } else {
                System.out.print(".");
            }
        }
    }
    
}

public class day_10 {

    public static void main(String[] args) throws FileNotFoundException {
        
        File myObj = new File("data/day10.txt");
        List<String> dataRowsAL = new ArrayList<String>();
        Scanner myReader = new Scanner(myObj);
        while (myReader.hasNextLine()) {
            dataRowsAL.add(myReader.nextLine());
        }
        myReader.close();
        String[] dataRows = new String[ dataRowsAL.size() ];
        
        // sacuvani podaci iz txt fajla kao: dataRows String[];
        dataRowsAL.toArray( dataRows );

        RayTube rayTube = new RayTube();
        for (String lineString : dataRows) {
            if (lineString.equals("noop")) {
                rayTube.noop();
            } else {
                String[] lineArr = lineString.split(" ", 0);
                rayTube.addx(Integer.parseInt(lineArr[1]));
            }
        }
        int totalSignalStrength = 0;
        for (int i = 20; i <= 220; i+= 40) {
            int signalStrength = i * rayTube.getValueAt(i - 1);
            System.out.println("Signal during " + i + "th cycle: " + i + " * " + rayTube.getValueAt(i - 1) + " = " + signalStrength);
            totalSignalStrength += signalStrength;
        }
        System.out.println("Total signal strenght: " + totalSignalStrength);
        System.out.println();

        rayTube.drawImage();

        
    }

}
