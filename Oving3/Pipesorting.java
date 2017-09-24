package algdat;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

public class Pipesorting {
	
	public static class Node{
		int value;
		Node parent;
		Node lChild;
		Node rChild;
		
		public Node(int value){
			this.value = value;
		}
	}

	public static class BinaryTree{
		Node root;
		ArrayList<Integer> sorted_list = new ArrayList<>();
		public void addNode(Node node){
			Node y = null;
			Node x = root;
			while (x != null){
				y = x;
				if (node.value < x.value){
					x = x.lChild;
				}
				else {
					x = x.rChild;
				}
			}
			node.parent = y;
			if (y == null){
				root = node;
			}
			else if (node.value < y.value){
				y.lChild = node;
			}
			else{
				y.rChild = node;
			}
		}
		
		public Node search(Node node, int value){
			while (node != null && value != node.value){
				if (value < node.value){
					node = node.lChild;
				}
				else{
					node = node.rChild;
				}
			}
			return node;
		}
		
		public Node min(Node node){
			while (node.lChild != null){
				node = node.lChild;
			}
			return node;
		}
		public Node max(Node node){
			while (node.rChild != null){
				node = node.rChild;
			}
			return node;
		}
		public ArrayList<Integer> inOrderTraversal(Node node){
			if (node != null){
				inOrderTraversal(node.lChild);
				sorted_list.add(node.value);
				inOrderTraversal(node.rChild);
			}
			return sorted_list;
		}
	}

	public static void sort(int[] list) {
		// SKRIV DIN KODE HER
	}
	
//	public static int[] findMinMax(int[] sortedList, int min, int max) {
//		// SKRIV DIN KODE HER
//	}
	
	public static void main(String args[]) {
		BinaryTree tree = new BinaryTree();
		Node n1 = new Node(5);
		Node n2 = new Node(10);
		Node n3 = new Node(22);
		Node n4 = new Node(7);
		Node n5 = new Node(1);
		tree.addNode(n1);
		tree.addNode(n2);
		tree.addNode(n3);
		tree.addNode(n4);
		tree.addNode(n5);
		ArrayList<Integer> list1 = tree.inOrderTraversal(n1);
		for (int i : list1){
			System.out.print(i + ", ");
		}
		
		
		
		
		
		
		
		
		
		
//		try {
//			BufferedReader in;
//		  if (args.length > 0) {
//					try {
//						in = new BufferedReader(new FileReader(args[0]));
//					}
//					catch (FileNotFoundException e) {
//						System.out.println("Not able to open the file " + args[0]);
//						return;
//					}
//				} else {
//					in = new BufferedReader(new InputStreamReader(System.in));
//				}
//				StringTokenizer st = new StringTokenizer(in.readLine());
//				int numTokens = st.countTokens();
//				int list[] = new int[numTokens];
//				for(int i = 0; i < numTokens; i++){
//					list[i] = Integer.parseInt(st.nextToken());
//					System.out.println(list[i]);
//				}
//				sort(list);
//				String line = in.readLine();
//				while(line != null){
//					st = new StringTokenizer(line);
//					int[] ret = findMinMax(list, Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
//					System.out.println(ret[0] + " " + ret[1]);
//					line = in.readLine();
//				}
//			} catch (Exception e) {
//				e.printStackTrace();
//			}
	}

}

