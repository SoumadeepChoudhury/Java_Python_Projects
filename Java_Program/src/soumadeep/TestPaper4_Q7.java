package soumadeep;
public class TestPaper4_Q7 {    
    public static void main(String[] args) {
        String input[]={"Delhi","Bangalore","Agra","Mumbai","Calcutta"};
        for(int i=0;i<input.length-1;i++){
            for(int j=0;j<input.length-1;j++){
                if(input[j].compareTo(input[j+1])>0){
                    String t=input[j];
                    input[j]=input[j+1];
                    input[j+1]=t;
                }
            }
        }

        for(int i=0;i<input.length;i++){
            System.out.print(input[i]+", ");
        }
        System.out.println();
    }
}