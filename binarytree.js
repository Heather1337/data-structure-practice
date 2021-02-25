class Node {

    constructor(data, left=null, right=null) {
        this.data = data;
        this.left = left;
        this.right = right;
    }
}

class BinaryTree {

    constructor(root=null) {
        this.root = root;
    }

    addNode(node) {
        if(!this.root) return this.root = node;
        const checkNodes = (curr) => {
            if(curr.left === null) return curr.left = node;
            else if(curr.right === null) return curr.right = node;
            else checkNodes(curr.left)
        }
        return checkNodes(this.root)
    }

    printNodes(node=this.root) {
        let curr = node;
        if(!curr) return
        console.log(curr.data);
        this.printNodes(curr.left)
        this.printNodes(curr.right)
    }

    replaceNode(newNode, nodeToReplace, node=this.root) {
        let curr = node;
        if(curr.data == nodeToReplace.data) return curr.data = newNode.data;
        else {
            if(curr.left !== null) this.replaceNode(newNode, nodeToReplace, curr.left)
            if(curr.right !== null) this.replaceNode(newNode, nodeToReplace, curr.right)
        }
        return;
    }
}

let node15 = new Node(15)
let node9 = new Node(9)
let node30 = new Node(30)
let node8 = new Node(8)
let node5 = new Node(5)
let node1337 = new Node(1337)

let tree = new BinaryTree()
tree.addNode(node15)
tree.addNode(node9)
tree.addNode(node30)
tree.addNode(node8)
tree.addNode(node5)
tree.printNodes()
tree.replaceNode(node1337, node5)
tree.printNodes()

exports.BinaryTree = BinaryTree
exports.Node = Node