package day_11_Monkey_in_the_Middle;

// import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
// import java.util.List;
// import java.util.Scanner;

@FunctionalInterface
interface MyBoolFunction {
    boolean apply(long x);
}

@FunctionalInterface
interface MyIntFunction {
    long apply(long x);
}

/**
 * Monkey
 */
class Monkey {

    public static int numOfMonkeys = 0;
    private static final int minimumPrimeProduct = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19;

    private ArrayList<Long> items = new ArrayList<>();
    private MyBoolFunction test;
    private MyIntFunction operation;
    private int throwTrue;
    private int throwFalse;
    private long timesInspected = 0;

    public Monkey(long[] items, MyBoolFunction testFun, MyIntFunction operationFun, int throwTrue, int throwFalse){
        numOfMonkeys++;
        for (long el : items) {
            this.items.add(el);
        }
        this.test = testFun;
        this.operation = operationFun;
        this.throwTrue = throwTrue;
        this.throwFalse = throwFalse;

    }

    public long[] getUpdatedItem(){
        long[] posVal = new long[2];

        long x = items.remove(0);
        x = updateItem(x);
        posVal[1] = x;
        if (testItem(x)) {
            posVal[0] = throwTrue;
        } else {
            posVal[0] = throwFalse;
        }

        return posVal;
    }

    public boolean testItem(long x){
        return test.apply(x);
    }

    public long updateItem(long x){
        this.timesInspected++;
        // return Math.round(operation.apply(x) / 3);
        x = operation.apply(x);
        while (x > minimumPrimeProduct) {
            x -= minimumPrimeProduct;
        }
        return x;
    }

    public long getTimesInspected(){
        return this.timesInspected;
    }

    public void addItem(long x) {
        this.items.add((long) x);
    }

    public boolean hasItems(){
        return this.items.size() != 0;
    }
}


public class day11 {
    
    public static void main(String[] args) throws FileNotFoundException {
        // File myObj = new File("data/day10.txt");
        // List<String> dataRowsAL = new ArrayList<String>();
        // Scanner myReader = new Scanner(myObj);
        // while (myReader.hasNextLine()) {
        //     dataRowsAL.add(myReader.nextLine());
        // }
        // myReader.close();
        // String[] dataRows = new String[ dataRowsAL.size() ];
        
        // // sacuvani podaci iz txt fajla kao: dataRows String[];
        // dataRowsAL.toArray( dataRows );

        // DIRECT INPUT! was easier...

        // direct example:
        Monkey[] monkeys = new Monkey[8];
        
        long[] i0 = {64,89,65,95};
        monkeys[0] = new Monkey(i0, (long x) -> (x% 3==0) ? true : false, (long x) -> x * 7, 4, 1);

        long[] i1 = {76, 66, 74, 87, 70, 56, 51, 66};
        monkeys[1] = new Monkey(i1, (long x) -> (x%13==0) ? true : false, (long x) -> x + 5, 7, 3);

        long[] i2 = {91, 60, 63};
        monkeys[2] = new Monkey(i2, (long x) -> (x% 2==0) ? true : false, (long x) -> x * x, 6, 5);

        long[] i3 = {92, 61, 79, 97, 79};
        monkeys[3] = new Monkey(i3, (long x) -> (x%11==0) ? true : false, (long x) -> x + 6, 2, 6);

        long[] i4 = {93, 54};
        monkeys[4] = new Monkey(i4, (long x) -> (x% 5==0) ? true : false, (long x) -> x * 11, 1, 7);

        long[] i5 = {60, 79, 92, 69, 88, 82, 70};
        monkeys[5] = new Monkey(i5, (long x) -> (x%17==0) ? true : false, (long x) -> x + 8, 4, 0);

        long[] i6 = {64, 57, 73, 89, 55, 53};
        monkeys[6] = new Monkey(i6, (long x) -> (x%19==0) ? true : false, (long x) -> x + 1, 0, 5);

        long[] i7 = {62};
        monkeys[7] = new Monkey(i7, (long x) -> (x% 7==0) ? true : false, (long x) -> x + 4, 3, 2);

        for (int i = 0; i < 10000; i++) {
            for (int j = 0; j < monkeys.length; j++) {
                while (monkeys[j].hasItems()) {
                    long[] posVal = monkeys[j].getUpdatedItem();
                    monkeys[(int) posVal[0]].addItem(posVal[1]);
                }
            }
        }

        long monkeyBuisness;
        long max1 = 0;
        long max2;
        for (int i = 0; i < monkeys.length; i++) {
            long val = monkeys[i].getTimesInspected();
            System.out.println(val);
            if (val > max1) {
                max1 = val;
            }
        }

        if (monkeys[0].getTimesInspected() != max1) {
            max2 = monkeys[0].getTimesInspected();
        } else {
            max2 = monkeys[1].getTimesInspected();
        }
        
        for (int i = 0; i < monkeys.length; i++) {
            long val = monkeys[i].getTimesInspected();
            if (val > max2 && val != max1) {
                max2 = val;
            }
        }

        monkeyBuisness = max1 * max2;
        System.out.println("Monkey buisness: " + monkeyBuisness);
        // > 24.215.461.800 - stored as int
        // > 24.103.245.208 - stored as long

    }
}
