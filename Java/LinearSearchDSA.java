public class LinearSearchDSA {
    public static void main(String[] args) {
        int[] array = {8,5,4,7,3,1,6,9,2};

        int index = LinearSearch(array, 10);

        if(index!=-1){
            System.out.println("Element found at index:\t"+index);
        }
        else{
            System.out.println("Element not found");
        }
    }

    public static int LinearSearch(int[] array, int data){
        for(int i = 0; i< array.length; i++){
            if(array[i]==data){
                return i;
            }
        }
        return -1;
    }
}
