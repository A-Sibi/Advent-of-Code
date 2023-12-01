package day_12_Hill_Climbing_Algorithm;

import java.util.HashMap;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

import java.util.Arrays;
import java.util.Comparator;

class IntArrayKey {
    private final int[] data;

    public IntArrayKey(int[] data) {
        this.data = data;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        IntArrayKey that = (IntArrayKey) o;
        return Arrays.equals(data, that.data);
    }

    @Override
    public int hashCode() {
        return Arrays.hashCode(data);
    }
}

class Position implements Comparable<Position> {

    public static char[][] map;

    private int x;
    private int y;
    private int height;
    private int[][] path;
    private int g_x;
    private int h_x;
    private int f_x;

    public Position(int[][] path) {
        this.x = path[path.length - 1][0];
        this.y = path[path.length - 1][1];
        char h = map[y][x];
        if (h == 'S') {
            this.height = 0;
        } else if (h == 'E') {
            this.height = 25;
        } else {
            this.height = (int) h - 97;
        }
        
        this.path = path;
        this.g_x = path.length - 1;
        this.h_x = 25 - this.height;
        this.f_x = this.g_x + this.h_x;
    }

    public void setGX(int g_x) {
        this.g_x = g_x;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public int[][] getPath() {
        return this.path;
    }

    public int getHeight() {
        return this.height;
    }

    public int getGval() {
        return this.g_x;
    }
    
    @Override
    public int compareTo(Position other) {
        // compare based on y
        int posCompare = Integer.compare(this.f_x, other.f_x);
        return posCompare;
        
    }
}


public class day_12 {

    public static int[][] extendPath(int[][] oldPath, int[] Coords) {
        int[][] newPath = new int[oldPath.length + 1][2]; // initialize new empty path
        int[][] copyPath = oldPath;                       // copy the old path
        for (int i = 0; i < copyPath.length; i++) {
            newPath[i] = copyPath[i];
        }
        int[] thisPos = new int[]{Coords[0], Coords[1]};  
        newPath[newPath.length - 1] = thisPos;            // add the currPos to the path
        return newPath;
    }

    public static int charHeight(char c) {
        if (c == 'S') {
            return 0;
        } else if (c == 'E') {
            return 25;
        } else {
            return (int) c - 97;
        }

    }
    
    public static void main(String[] args) throws FileNotFoundException{
        File myObj = new File("data/day12.txt");
        List<String> dataRowsAL = new ArrayList<String>();
        Scanner myReader = new Scanner(myObj);
        while (myReader.hasNextLine()) {
            dataRowsAL.add(myReader.nextLine());
        }
        myReader.close();
        String[] dataRows = new String[ dataRowsAL.size() ];
        
        // sacuvani podaci iz txt fajla kao: dataRows String[];
        dataRowsAL.toArray( dataRows );

        char[][] map = new char[dataRows.length][dataRows[0].length()];

        for (int i = 0; i < dataRows.length; i++) {
            for (int j = 0; j < dataRows[i].length(); j++) {
                map[i][j] = dataRows[i].charAt(j);
            }
        }
        Position.map = map;

        int startX = -1;
        int startY = -1;
        int endX = -1;
        int endY = -1;
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[0].length; j++) {
                if (map[i][j] == 'S') {
                    startX = j;
                    startY = i;
                } else if (map[i][j] == 'E') {
                    endX = j;
                    endY = i;
                }
            }
        }

        HashMap<IntArrayKey, Integer> gCost = new HashMap<>();
        PriorityQueue<Position> frontier = new PriorityQueue<>(new Comparator<Position>() {
            @Override
            public int compare(Position p1, Position p2) {
                return p1.compareTo(p2);
            }
        });
        Position startPos = new Position(new int[][]{{startX, startY}});
        
        frontier.add(startPos);
        gCost.put(new IntArrayKey(new int[] {startX, startY}), 0);
        // end of techincal setup :)

        int turnCounter = 0;

        while (!frontier.isEmpty()) {
            Position currPos = frontier.remove();
            int x = currPos.getX();
            int y = currPos.getY();

            // process visualization
            if (turnCounter % 100000 == 0) {
                System.out.println("Number of reached positions: " + turnCounter);
            }
            turnCounter++;

            // print the end state and teriminate
            if (x == endX && y == endY ) {
                System.out.println(currPos.getPath().length);
                int[][] endPath = currPos.getPath();
                for (int i = 0; i < endPath.length; i++) {
                    System.out.println(endPath[i][1] + "," + endPath[i][0] + " " + Position.map[endPath[i][1]][endPath[i][0]]);
                }
                return; //terminate program
            }

            // IntArrayKey currKeyVal = new IntArrayKey(new int[]{currPos.getX(), currPos.getY()});
            // if (!gCost.containsKey(currKeyVal) || currPos.getGval() < gCost.get(currKeyVal)) {
            //     gCost.put(currKeyVal, currPos.getGval());
            // }
            


            // try to add all neighbouring positions
            if (x > 0 && Math.abs(currPos.getHeight() - charHeight(map[y][x - 1])) < 2) {
                int[][] newPath = extendPath(currPos.getPath(), new int[]{x-1, y});
                if (!gCost.containsKey(new IntArrayKey(newPath[newPath.length - 1]))) {
                    frontier.add(new Position(newPath));
                }

            }
            if (x < map[0].length-1 && Math.abs(currPos.getHeight() - charHeight(map[y][x + 1])) < 2) {
                int[][] newPath = extendPath(currPos.getPath(), new int[]{x+1, y});
                if (!gCost.containsKey(new IntArrayKey(newPath[newPath.length - 1]))) {
                    frontier.add(new Position(newPath));
                }

            }
            if (y > 0 && Math.abs(currPos.getHeight() - charHeight(map[y - 1][x])) < 2) {
                int[][] newPath = extendPath(currPos.getPath(), new int[]{x, y-1});
                if (!gCost.containsKey(new IntArrayKey(newPath[newPath.length - 1]))) {
                    frontier.add(new Position(newPath));
                }

            }
            if (y < map.length-1 && Math.abs(currPos.getHeight() - charHeight(map[y + 1][x])) < 2) {
                int[][] newPath = extendPath(currPos.getPath(), new int[]{x, y+1});
                if (!gCost.containsKey(new IntArrayKey(newPath[newPath.length - 1]))) {
                    frontier.add(new Position(newPath));
                }

            }

        } // end while frontier
        

    }
}
