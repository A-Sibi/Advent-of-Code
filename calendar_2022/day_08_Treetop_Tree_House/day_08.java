package day_08_Treetop_Tree_House;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class day_08 {
    public static void main(String[] args) throws FileNotFoundException {
        File myObj = new File("data/day8.txt");
        List<String> dataRowsAL = new ArrayList<String>();
        Scanner myReader = new Scanner(myObj);
        while (myReader.hasNextLine()) {
            dataRowsAL.add(myReader.nextLine());
        }
        myReader.close();
        String[] dataRows = new String[ dataRowsAL.size() ];

        // sacuvani podaci it txt fajla kao: dataRows String[];
        dataRowsAL.toArray( dataRows );

        int[][] trees = new int[dataRows.length][dataRows[0].length()];

        for (int i = 0; i < dataRows.length; i++) {
            for (int j = 0; j < dataRows[0].length(); j++) {
                trees[i][j] = Integer.parseInt(String.valueOf(dataRows[i].charAt(j)));
            }
        }
        // end of setup

        int numVisables = 0;
        boolean visible = true;

        for (int i = 0; i < trees.length; i++) {
            for (int j = 0; j < trees[0].length; j++) {
                visible = true;
                
                // if tree on edge of the forest
                if (i == 0 || j == 0) {
                    numVisables++;
                    continue;
                }
                
                // check row
                for (int k = 0; k < j; k++) {
                    if (trees[i][k] >= trees[i][j]) {
                        visible = false;
                        break;
                    }
                }
                if (visible) {
                    numVisables++;
                    continue;
                }
                visible = true;


                for (int k = j + 1; k < trees[0].length; k++) {
                    if (trees[i][k] >= trees[i][j]) {
                        visible = false;
                        break;
                    }
                }
                if (visible) {
                    numVisables++;
                    continue;
                }
                visible = true;

                // check column
                for (int k = 0; k < i; k++) {
                    if (trees[k][j] >= trees[i][j]) {
                        visible = false;
                        break;
                    }
                }
                if (visible) {
                    numVisables++;
                    continue;
                }
                visible = true;

                for (int k = i + 1; k < trees.length; k++) {
                    if (trees[k][j] >= trees[i][j]) {
                        visible = false;
                        break;
                    }
                }
                if (visible) {
                    numVisables++;
                    continue;
                }



            }
        }
        System.out.println("Part 1: " + numVisables);

        int maxScenicScore = 0;
        int currScore;
        int scoreLeft;
        int scoreRight;
        int scoreUp;
        int scoreDown;
        
        for (int i = 0; i < trees.length; i++) {
            for (int j = 0; j < trees[0].length; j++) {

                currScore = 0;
                scoreLeft = 0;
                scoreRight = 0;
                scoreUp = 0;
                scoreDown = 0;
                
                // check row
                for (int k = j-1; k >= 0; k--) {
                    scoreLeft++;
                    if (trees[i][k] >= trees[i][j]) {
                        break;
                    }
                }

                for (int k = j + 1; k < trees[0].length; k++) {
                    scoreRight++;
                    if (trees[i][k] >= trees[i][j]) {
                        break;
                    }
                }

                // check column
                for (int k = i-1; k >= 0; k--) {
                    scoreUp++;
                    if (trees[k][j] >= trees[i][j]) {
                        break;
                    }
                }

                for (int k = i + 1; k < trees.length; k++) {
                    scoreDown++;
                    if (trees[k][j] >= trees[i][j]) {
                        break;
                    }
                }

                currScore = scoreLeft * scoreRight * scoreDown * scoreUp;
                if (currScore > maxScenicScore) {
                    maxScenicScore = currScore;
                }

            }
        }
        System.out.println("Part 2: " + maxScenicScore);


    }
}
