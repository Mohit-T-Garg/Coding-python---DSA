import java.util.ArrayList;

public class poweroftwomaxheap
{   // A new Arraylist to store the Integers
    ArrayList Heap= new ArrayList<Integer>(2);

    // the given x
    public int pow2;

    //initiating the class
    public poweroftwomaxheap(int poweroftwo){
        this.pow2=poweroftwo;
        this.size=0;
    }

    public int size;

    // No. of possible chile --> 2 pow x
    public int childsize= (int) Math.pow(2, pow2);
    //child List of given index
    private int[] getChild (int parentId)
    {
        int batchId = (parentId - 1 + childsize ) / childsize ;
        int front = (batchId )* childsize +1 ;

        int back = (batchId + 1)* childsize  ;
        int[] ans = new int[2];
        ans[0]=front;
        ans[1]=back;
        return  ans;
    }
    //parent of a given childID
    private int parentId ( int childID) 
    {
        int batchId = (childID - 1 + childsize ) / childsize ;
        return (batchId - 1) ;
    }

    //check leaf node
    public boolean leaf(int i)
    {
        if (getChild(i)[0] > size ){
            return true;
        }else{
            return false;
        }
    }


    //insert 
    public void insert(int element) {
		Heap.add(element);
		int current = size;
        if (current!=0){
		while (((int) Heap.get(current) > (int) Heap.get(parentId(current))) && current > 0) {
            //System.out.println(current);
			swap(current, parentId(current));
			current = parentId(current);
            if (current ==0){
                break;
            }
		}
        int batchId = (current - 1 ) / childsize ;
        int front = (batchId )* childsize +1 ;
        while(current > front){
            if ((int) Heap.get(current) < (int) Heap.get(current-1)){
                swap(current,  current-1);
                current=current-1;
            }
        }
    }
		size++;
	}

    	// heapify the node at i
	private void maxHeapify(int i) {
        // If the node is a non-leaf node and any of its child is smaller
            if (!leaf(i)) {
                int max = getChild(i)[1];
                if (max >= size){
                    max = size-1;
                }
                if ((int)Heap.get(i) < (int)Heap.get(max)) {
                        swap(i, max);
                        maxHeapify(max);
                }
            }
        }
    

    	// removes and returns the minimum element from the heap
	public int remove() {
        // since its a min heap, so root = minimum
           int popped = (int) Heap.get(0);
           size=size-1;
           Heap.set(0,Heap.get(size));
           maxHeapify(0);
           return popped;
       }   
       
    public void print(){
        for (int i = 0; i < Heap.size(); i++) {
            System.out.println(Heap.get(i) + " ");
        }
    }

    // swaps two nodes of the heap
	private void swap(int x, int y) {
		int tmp;
		tmp = (int ) Heap.get(x);
		Heap.set(x,Heap.get(y));
		Heap.set(y,tmp);
	}

   /*  public static void main(String[] args)
    {
        poweroftwomaxheap H = new poweroftwomaxheap(4);
        H.insert(1);
        H.insert(2);
        H.insert(3);
        H.insert(6);
        H.insert(5);
        System.out.println(H.remove());
        System.out.println(H.remove());
        System.out.println(H.remove());
        System.out.println(H.remove());
        System.out.println(H.remove());
        //H.print();

    }
    */
} 
/* 
import java.util.ArrayList;
public class poweroftwomaxheap
{
    //A new Arraylist of Array list containing 1 batch of integers
    ArrayList batchList = new ArrayList<ArrayList>();

    //max at any given time
    public int max;

    //given x
    public int pow2;

    // power x of 2
    public int batchSize;

    //initiate the class

    public poweroftwomaxheap(int pow2)
    {
        this.pow2 = pow2 ; 
        this.batchSize  = ( int )Math.pow(2, pow2) ;
    }

    //parent batch no of given batch no

    private int parentBatchNo(int childBatchNo)
    {

    }

}*/