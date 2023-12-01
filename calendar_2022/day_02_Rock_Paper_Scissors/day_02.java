package day_02_Rock_Paper_Scissors;
import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class day_02 {

    public static void main(String[] args) throws Exception {

        File myObj = new File("data/day2.txt");
        List<String> dataRowsAL = new ArrayList<String>();
        Scanner myReader = new Scanner(myObj);
        while (myReader.hasNextLine()) {
            dataRowsAL.add(myReader.nextLine());
        }
        myReader.close();
        String[] dataRows = new String[ dataRowsAL.size() ];

        // sacuvani podaci it txt fajla kao: dataRows String[];
        dataRowsAL.toArray( dataRows );

        int total = 0;

        for (String elString : dataRows) {
            char opponent = elString.charAt(0);
            char response = elString.charAt(2);

            // switch (opponent) {
            //     case 'A':
            //         switch (response) {
            //             case 'X':
            //                 total += 4;
            //                 break;
                    
            //             case 'Y':
            //                 total += 8;
            //                 break;
                    
            //             case 'Z':
            //                 total += 3;
            //                 break;
                    
            //             default:
            //                 total = -100000;
            //                 break;
            //         }
            //         break;
            
            //     case 'B':
            //     switch (response) {
            //         case 'X':
            //             total += 1;
            //             break;
                
            //         case 'Y':
            //             total += 5;
            //             break;
                
            //         case 'Z':
            //             total += 9;
            //             break;
                
            //         default:
            //             total = -100000;
            //             break;
            //     }
            //     break;
            
            //     case 'C':
            //     switch (response) {
            //         case 'X':
            //             total += 7;
            //             break;
                
            //         case 'Y':
            //             total += 2;
            //             break;
                
            //         case 'Z':
            //             total += 6;
            //             break;
                
            //         default:
            //             total = -100000;
            //             break;
            //     }
            //     break;
            
            //     default:
            //         break;
            // }
            switch (opponent) {
                case 'A':
                    switch (response) {
                        case 'X':
                            total += 3;
                            break;
                    
                        case 'Y':
                            total += 4;
                            break;
                    
                        case 'Z':
                            total += 8;
                            break;
                    
                        default:
                        throw new Exception("Invalid input");
                    }
                    break;
            
                case 'B':
                switch (response) {
                    case 'X':
                        total += 1;
                        break;
                
                    case 'Y':
                        total += 5;
                        break;
                
                    case 'Z':
                        total += 9;
                        break;
                
                    default:
                        throw new Exception("Invalid input");
                }
                break;
            
                case 'C':
                switch (response) {
                    case 'X':
                        total += 2;
                        break;
                
                    case 'Y':
                        total += 6;
                        break;
                
                    case 'Z':
                        total += 7;
                        break;
                
                    default:
                        throw new Exception("Invalid input");
                }
                break;
            
                default:
                    break;
            }
            System.out.println(total);
        }
    }
}