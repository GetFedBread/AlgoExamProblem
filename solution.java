import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;

public class solution {
    public static int[] cards;
    public static void main(String[] args) {
        long start_time = System.nanoTime();
        try(BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {
            int n = Integer.parseInt(reader.readLine());
            String[] cards_in = reader.readLine().split(" ");
            cards = new int[n];
            for(int i = 0; i < n; i++) {
                cards[i] = Integer.parseInt(cards_in[i]);
            }
            System.out.println(check(0, n-1, -1, -1));
        } catch (Exception e) {

        }
        System.out.println("Time: "+(System.nanoTime() - start_time));
    }

    static HashMap<Tuple, Integer> mem = new HashMap<>();
    public static int check(int lefti, int righti, int lo, int hi) {
        if (lefti > righti) return 0;
        Tuple args = new Tuple(lefti, righti, lo, hi);
        if(mem.containsKey(args)) return mem.get(args);
        int result = 0;
        
        // Take left card
        if(lo == -1) {
            result = check(lefti+1, righti, cards[lefti], cards[lefti]) + 1;
        } else if(cards[lefti] < lo) {
            result = check(lefti+1, righti, cards[lefti], hi) + 1;
        }else if (cards[lefti] > hi) {
            result = check(lefti+1, righti, lo, cards[lefti]) + 1;
        }
        
        // Discard left card
        result = Integer.max(check(lefti+1, righti, lo, hi), result);
        
        // Take right card
        if (hi == -1) {
            result = Integer.max(check(lefti, righti-1, cards[righti], cards[righti]) + 1, result);
        }
        else if (cards[righti] < lo) {
            result = Integer.max(check(lefti, righti-1, cards[righti], hi) + 1, result);
        }else if (cards[righti] > hi) {
            result = Integer.max(check(lefti, righti-1, lo, cards[righti]) + 1, result);
        }
        
        
        // Discard right card
        result = Integer.max(check(lefti, righti-1, lo, hi), result);
        
        
        mem.put(args, result);
        return result;
    }
}

class Tuple implements Comparable<Tuple> {
    int[] values;

    public Tuple(int... values) {
        this.values = values;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Tuple)) return false;
        Tuple p = (Tuple) o;
        if(p.values.length != values.length) return false;
        return Arrays.equals(values, p.values);
    }

    @Override
    public int compareTo(Tuple t) {
        return Arrays.compare(values, t.values);
    }

    @Override
    public int hashCode() {
        return Arrays.hashCode(values);
    }

    public static Tuple max(Tuple t1, Tuple t2) {
        if(t1.compareTo(t2) > 0) return t1;
        return t2;
    }
}