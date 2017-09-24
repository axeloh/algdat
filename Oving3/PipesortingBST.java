package algdat;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;

public class PipesortingBST {
	
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
		
		public Node successor(Node node){
			if (node.rChild != null){
				return min(node.rChild);
			}
			Node y = node.parent;
			while (y != null && node == y.rChild){
				node = y;
				y = y.parent;
			}
			return y;
		}
		
		public Node predecessor(Node node){
			if (node.lChild != null){
				return max(node.lChild);
			}
			Node y = node.parent;
			while (y != null && node == y.lChild){
				node = y;
				y = y.parent;
			}
			return y;
		}
	}


	public static ArrayList<Integer> findMinMax(BinaryTree tree, int min, int max) {
		ArrayList<Integer> list = new ArrayList<>();
		Node lower = tree.search(tree.root, min);
		Node upper = tree.search(tree.root, max);
		if (lower == null){
			Node node = new Node(min);
			tree.addNode(node);
			lower = tree.predecessor(node);
			if (lower == null){
				lower = node.parent;
			}
		}
		if (upper == null){
			Node node = new Node(max);
			tree.addNode(node);
			upper = tree.successor(node);
			if (upper == null){
				upper = node.parent;
			}
		}
		list.add(lower.value);
		list.add(upper.value);
		return list;
	}
	
	public static void main(String args[]) {
		BinaryTree tree = new BinaryTree();
		
		try {
			BufferedReader in;
			if (args.length > 0) {
				try {
					in = new BufferedReader(new FileReader(args[0]));
				}
				catch (FileNotFoundException e) {
					System.out.println("Not able to open the file " + args[0]);
					return;
				}
			} else {
				in = new BufferedReader(new InputStreamReader(System.in));
			}
				StringTokenizer st = new StringTokenizer(in.readLine());
				int numTokens = st.countTokens();
				int list[] = new int[numTokens];
				Node root = new Node(Integer.parseInt(st.nextToken()));
				tree.addNode(root);
				for(int i = 1; i < numTokens; i++){
					list[i] = Integer.parseInt(st.nextToken());
					Node node = new Node(list[i]);
					tree.addNode(node);
				}
				String line = in.readLine();
				while(line != null){
					st = new StringTokenizer(line);
					ArrayList<Integer> ret = findMinMax(tree, Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
					System.out.println(ret.get(0) + " " + ret.get(1));
					line = in.readLine();
				}
			} catch (Exception e) {
				e.printStackTrace();
			}
	}

}

