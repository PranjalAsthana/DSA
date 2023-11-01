import java.util.Arrays;
public class BinarySearchDSA {
    public static void main(String[] args) {
        int[] array = {8,5,4,7,3,1,6,9,2};

        Arrays.sort(array);

        int index = BinarySearch(array, 8);


        if(index!=-1){
            System.out.println("Element found at index:\t"+index);
        }
        else{
            System.out.println("Element not found");
        }
    }
    public static int BinarySearch(int[] array, int target){
        int low = 0;
        int high = array.length -1;
        while(low<=high){
            int middle = low + (high-low) /2;
            //int value = array[middle];
            int value = array[middle];

            if(value>target) high = middle-1;
            else if(value<target) low = middle+1;
            else if(value==target) return middle;
        }
        return -1;
    }
}
