package day_05_Supply_Stacks;
import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

interface StackInterface {
    
    static final int DEFAULT_CAPACITY = 64;
    char top();
    void push(char x);
    char pop();

}


class Stack implements StackInterface {
    
    private int velikost = 0;
    private char[] sklad = new char[DEFAULT_CAPACITY];

    public int getVelikost() {
        return velikost;
    }
    public char top() {
        return sklad[velikost - 1];
    }
    public void push(char x) {
        sklad[velikost] = x;
        velikost++;
    }
    public char pop() {
        char x = sklad[velikost - 1];
        sklad[velikost - 1 ] = '\0';
        velikost--;
        return x;
    }
    public void printStack(int k) {
        int i = 0;
        System.out.print("Stanje na Stack[" + k + "]: ");
        while (sklad[i] != '\0') {
            System.out.print(sklad[i] + " ");
            i++;
        }
    }

}


interface SequenceInterface {

    static final int seqLength = 10; // number of stacks + 1
    static final String ERR_MSG_INDEX = "Wrong index in sequence.";
    Stack get(int i);
    void add(Stack x);

}

class Sequence implements SequenceInterface {

    private Stack[] skladList = new Stack[seqLength];
    boolean pogoj = false;

    public Stack get(int i) {
        return skladList[i];
    }

    public void add(Stack x) {
        // wtf?
    }

    public Stack[] getSkladList() {
        return skladList;
    }
    
}

public class day_05 {

    public static void main(String[] args) throws Exception {

        Sequence skladi = new Sequence();
        for (int i = 0; i < skladi.getSkladList().length; i++) {
            skladi.getSkladList()[i] = new Stack();
        }

        // I don't care input file is ugly vvv
        char[][] input = {
            {},
            {'Z','P','M','H','R'},
            {'P','C','J','B'},
            {'S','N','H','G','L','C','D'},
            {'F','T','M','D','Q','S','R','L'},
            {'F','S','P','Q','B','T','Z','M'},
            {'T','F','S','Z','B','G'},
            {'N','R','V'},
            {'P','G','L','T','D','V','C','M'},
            {'W','Q','N','J','F','M','L'}
        };

        // fill up the setup vvv
        for (int i = 1; i < skladi.getSkladList().length; i++) {
            for (int j = 0; j < input[i].length; j++) {
                skladi.getSkladList()[i].push(input[i][j]);
            }
        }

        
        File myObj = new File("data/day5-reduced.txt");
        List<String> dataRowsAL = new ArrayList<String>();
        Scanner myReader = new Scanner(myObj);
        while (myReader.hasNextLine()) {
            dataRowsAL.add(myReader.nextLine());
        }
        myReader.close();
        String[] dataRows = new String[ dataRowsAL.size() ];

        // sacuvani podaci it txt fajla kao: dataRows String[];
        dataRowsAL.toArray( dataRows );

        for (int i = 0; i < dataRows.length; i++) { // main loop
            String[] tempData1 = new String[6];
            tempData1 = dataRows[i].split(" ");
            int[] cmd = new int[3];
            cmd[0] = Integer.parseInt(tempData1[1]);
            cmd[1] = Integer.parseInt(tempData1[3]);
            cmd[2] = Integer.parseInt(tempData1[5]);

            // part 1 logic
            // for (int j = 0; j < cmd[0]; j++) {   
            //     skladi.getSkladList()[cmd[2]].push(skladi.getSkladList()[cmd[1]].pop());
            // }

            // part 2 logic
            for (int j = 0; j < cmd[0]; j++) {
                skladi.getSkladList()[0].push(skladi.getSkladList()[cmd[1]].pop());
            }
            for (int j = 0; j < cmd[0]; j++) {
                skladi.getSkladList()[cmd[2]].push(skladi.getSkladList()[0].pop());
            }
                
        }
        for (int i = 1; i < skladi.getSkladList().length; i++) {
            System.out.print(skladi.getSkladList()[i].top());
        }

        
    }

}
