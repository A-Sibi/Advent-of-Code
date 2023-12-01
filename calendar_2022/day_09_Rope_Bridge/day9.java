package day_09_Rope_Bridge;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;

class Position {
    int x;
    int y;

    public Position(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Position position = (Position) o;
        return x == position.x &&
                y == position.y;
    }

    @Override
    public int hashCode() {
        return Arrays.hashCode(new int[] {x, y});
    }
}

public class day9 {

    public static int[] getNewTailCoords(int Hx, int Hy, int Tx, int Ty) {
            // move the part
            if (Hx > Tx) {
                Tx++;
                if (Hy > Ty) {
                    Ty++;
                } else if (Hy < Ty) {
                    Ty--;
                }
            } else if (Hx < Tx){
                Tx--;
                if (Hy > Ty) {
                    Ty++;
                } else if (Hy < Ty) {
                    Ty--;
                }
            } else if (Hx == Tx) {
                if (Hy > Ty) {
                    Ty++;
                } else if (Hy < Ty) {
                    Ty--;
                }
            }
        int[] newPos = {Tx, Ty};
        return newPos;
    }

    public static void main(String[] args) throws FileNotFoundException {
        
        File myObj = new File("data/day9.txt");
        List<String> dataRowsAL = new ArrayList<String>();
        Scanner myReader = new Scanner(myObj);
        while (myReader.hasNextLine()) {
            dataRowsAL.add(myReader.nextLine());
        }
        myReader.close();
        String[] dataRows = new String[ dataRowsAL.size() ];

        // sacuvani podaci it txt fajla kao: dataRows String[];
        dataRowsAL.toArray( dataRows );

        boolean part2 = true;

        // part 1
        int[] Hpos = {0, 0}; // initalization is actually redundant here!
        int[] oldHpos = {0, 0};
        int[] Tpos = {0, 0};

        // part 2
        int[][] rope = new int[10][2]; // old and new pos of each segment

        HashSet<Position> allReachedPos = new HashSet<>();
        Position startPos = new Position(0, 0);
        allReachedPos.add(startPos);

        if (!part2) {
            
            for (String dataString : dataRows) {
                String[] dataStrings = dataString.split(" ", 0);
                char direction = dataStrings[0].toCharArray()[0];
                int distance = Integer.parseInt(dataStrings[1]);

                switch (direction) {
                    case 'U':
                        for (int i = 0; i < distance; i++) {
                            oldHpos[0] = Hpos[0];
                            oldHpos[1] = Hpos[1];
                            Hpos[1]++;
                            
                            if (Math.abs(Hpos[0] - Tpos[0]) > 1 || Math.abs(Hpos[1] - Tpos[1]) > 1) {
                                Tpos[0] = oldHpos[0];
                                Tpos[1] = oldHpos[1];
                                Position currPos = new Position(Tpos[0], Tpos[1]);
                                allReachedPos.add(currPos);
                            }
                        }
                        break;
                        
                    case 'D':
                        for (int i = 0; i < distance; i++) {
                            oldHpos[0] = Hpos[0];
                            oldHpos[1] = Hpos[1];
                            Hpos[1]--;
                            
                            if (Math.abs(Hpos[0] - Tpos[0]) > 1 || Math.abs(Hpos[1] - Tpos[1]) > 1) {
                                Tpos[0] = oldHpos[0];
                                Tpos[1] = oldHpos[1];
                                Position currPos = new Position(Tpos[0], Tpos[1]);
                                allReachedPos.add(currPos);
                            }
                        }
                        
                        break;
                        
                        case 'L':
                        for (int i = 0; i < distance; i++) {
                            oldHpos[0] = Hpos[0];
                            oldHpos[1] = Hpos[1];
                            Hpos[0]--;
                            
                            if (Math.abs(Hpos[0] - Tpos[0]) > 1 || Math.abs(Hpos[1] - Tpos[1]) > 1) {
                                Tpos[0] = oldHpos[0];
                                Tpos[1] = oldHpos[1];
                                Position currPos = new Position(Tpos[0], Tpos[1]);
                                allReachedPos.add(currPos);
                            }
                        }
                        
                        break;
                        
                        case 'R':
                        for (int i = 0; i < distance; i++) {
                            oldHpos[0] = Hpos[0];
                            oldHpos[1] = Hpos[1];
                            Hpos[0]++;
                            

                            if (Math.abs(Hpos[0] - Tpos[0]) > 1 || Math.abs(Hpos[1] - Tpos[1]) > 1) {
                                Tpos[0] = oldHpos[0];
                                Tpos[1] = oldHpos[1];
                                Position currPos = new Position(Tpos[0], Tpos[1]);
                                allReachedPos.add(currPos);
                            }
                        }
                        
                        break;
                
                    default:
                        System.out.println("Error!");
                        break;
                }
            }
        } else {
            for (String dataString : dataRows) {
                String[] dataStrings = dataString.split(" ", 0);
                char direction = dataStrings[0].toCharArray()[0];
                int distance = Integer.parseInt(dataStrings[1]);

                switch (direction) {
                    case 'U':
                        for (int i = 0; i < distance; i++) {
                            
                            // move the head
                            rope[0][1]++;

                            for (int j = 1; j < rope.length; j++) {
                                
                                // check if you need to move the next part
                                int Hx = rope[j-1][0];
                                int Hy = rope[j-1][1];
                                int Tx = rope[j][0];
                                int Ty = rope[j][1];
                                if (Math.abs(Hx - Tx) > 1 || Math.abs(Hy - Ty) > 1) {
                                    int[] newPos = getNewTailCoords(Hx, Hy, Tx, Ty);
                                    rope[j][0] = newPos[0];
                                    rope[j][1] = newPos[1];
                                    if (j == 9) {
                                            Position currPos = new Position(rope[j][0], rope[j][1]);
                                            allReachedPos.add(currPos);
                                        }

                                } else { //  proceed to move the head again
                                    break;
                                }
                            }
                        }
                        break;
                    case 'D':
                    for (int i = 0; i < distance; i++) {
                            
                        // move the head
                        rope[0][1]--;

                        for (int j = 1; j < rope.length; j++) {
                            
                            // check if you need to move the next part
                            int Hx = rope[j-1][0];
                            int Hy = rope[j-1][1];
                            int Tx = rope[j][0];
                            int Ty = rope[j][1];
                            if (Math.abs(Hx - Tx) > 1 || Math.abs(Hy - Ty) > 1) {
                                int[] newPos = getNewTailCoords(Hx, Hy, Tx, Ty);
                                rope[j][0] = newPos[0];
                                rope[j][1] = newPos[1];
                                if (j == 9) {
                                        Position currPos = new Position(rope[j][0], rope[j][1]);
                                        allReachedPos.add(currPos);
                                    }

                            } else { //  proceed to move the head again
                                break;
                            }
                        }
                    }
                    break;
                    case 'L':
                    for (int i = 0; i < distance; i++) {
                            
                        // move the head
                        rope[0][0]--;

                        for (int j = 1; j < rope.length; j++) {
                            
                            // check if you need to move the next part
                            int Hx = rope[j-1][0];
                            int Hy = rope[j-1][1];
                            int Tx = rope[j][0];
                            int Ty = rope[j][1];
                            if (Math.abs(Hx - Tx) > 1 || Math.abs(Hy - Ty) > 1) {
                                int[] newPos = getNewTailCoords(Hx, Hy, Tx, Ty);
                                rope[j][0] = newPos[0];
                                rope[j][1] = newPos[1];
                                if (j == 9) {
                                        Position currPos = new Position(rope[j][0], rope[j][1]);
                                        allReachedPos.add(currPos);
                                    }

                            } else { //  proceed to move the head again
                                break;
                            }
                        }
                    }
                    break;
                    case 'R':
                    for (int i = 0; i < distance; i++) {
                            
                        // move the head
                        rope[0][0]++;

                        for (int j = 1; j < rope.length; j++) {
                            
                            // check if you need to move the next part
                            int Hx = rope[j-1][0];
                            int Hy = rope[j-1][1];
                            int Tx = rope[j][0];
                            int Ty = rope[j][1];
                            if (Math.abs(Hx - Tx) > 1 || Math.abs(Hy - Ty) > 1) {
                                int[] newPos = getNewTailCoords(Hx, Hy, Tx, Ty);
                                rope[j][0] = newPos[0];
                                rope[j][1] = newPos[1];
                                if (j == 9) {
                                        Position currPos = new Position(rope[j][0], rope[j][1]);
                                        allReachedPos.add(currPos);
                                    }

                            } else { //  proceed to move the head again
                                break;
                            }
                        }
                    }
                    break;
                        
                    default:
                        System.out.println("Error!");
                        break;
                }

            }
        }

        System.out.println(allReachedPos.size());
        // manje od 4537!

    }
    
}
