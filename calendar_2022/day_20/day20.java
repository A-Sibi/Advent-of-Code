package day_20;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

class Number {
  public final int value;
  public final int orgIndex;
  public boolean wasMoved;
  public int targetIndex;

  public Number(int value, int index) {
    this.value = value;
    this.orgIndex = index;
    this.wasMoved = false;
    this.targetIndex = -1;
  }
}

public class day20 {
  public static void main(String[] args) throws IOException {
    try (BufferedReader reader = new BufferedReader(new FileReader("data/day20.txt"))) {
      List<Number> dataClass = new ArrayList<>();

      String line;
      while ((line = reader.readLine()) != null) {
        dataClass.add(new Number(Integer.parseInt(line), dataClass.size()));
      }

      for (int i = 0; i < dataClass.size(); i++) {
        Number number = dataClass.get(i);
        if (!number.wasMoved) {
          number.targetIndex = (i + number.value) % dataClass.size();
          dataClass.remove(i);
          number.wasMoved = true;
          dataClass.add(number.targetIndex, number);
        }
      }

      for (int i = 0; i < dataClass.size(); i++) {
          System.out.println(dataClass.get(i).value);
      }
    } catch (NumberFormatException e) {
      e.printStackTrace();
    }
}
}