package day_03_Rucksack_Reorganization;
import java.io.File;
import java.util.*;

public class day_03 {

    public static int itemValue(char x) {
        int code = (int) x; //ASCII value
        if (code > 96) {
            code -= 96;
        } else {
            code -= 38;
        }
        return code;
    }
    // @SuppressWarnings("unchecked")
    public static void main(String[] args) throws Exception {

        File myObj = new File("data/day3.txt");
        List<String> dataRowsAL = new ArrayList<String>();
        Scanner myReader = new Scanner(myObj);
        while (myReader.hasNextLine()) {
            dataRowsAL.add(myReader.nextLine());
        }
        myReader.close();
        String[] dataRows = new String[ dataRowsAL.size() ];

        // sacuvani podaci iz txt fajla kao: dataRows String[];
        dataRowsAL.toArray( dataRows );

        int prioritySum = 0;
        for (int i = 0; i < dataRows.length; i++) {

            char[] items = dataRows[i].toCharArray();
            int len = items.length;

            Set front = new HashSet();
            Set back = new HashSet();


            for (int j = 0; j < items.length/2; j++) {
                front.add(items[j]);
            }
            for (int j = items.length/2; j < items.length; j++) {
                back.add(items[j]);
            }

            Set intersection = new HashSet(front);
            intersection.retainAll(back);

            char x = (char) intersection.toArray()[0];
            prioritySum += itemValue(x);
        }

        System.out.println("Part 1 answer: " + prioritySum);


        // PART 2
        

        int badgePrioritySum = 0;
        for (int i = 0; i < dataRows.length-2; i+=3) {
            char[] items1 = dataRows[i].toCharArray();
            char[] items2 = dataRows[i+1].toCharArray();
            char[] items3 = dataRows[i+2].toCharArray();

            Set bag1 = new HashSet();
            Set bag2 = new HashSet();
            Set bag3 = new HashSet();

            for (int j = 0; j < items1.length; j++) {
                bag1.add(items1[j]);
            }
            for (int j = 0; j < items2.length; j++) {
                bag2.add(items2[j]);
            }
            for (int j = 0; j < items3.length; j++) {
                bag3.add(items3[j]);
            }

            Set intersectionBagde = new HashSet(bag1);
            intersectionBagde.retainAll(bag2);
            intersectionBagde.retainAll(bag3);

            char badge = (char) intersectionBagde.toArray()[0];
            badgePrioritySum += itemValue(badge);

        }

        System.out.println("Part 2: " + badgePrioritySum);
    }
}