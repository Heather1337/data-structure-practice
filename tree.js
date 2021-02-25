/* ==== Build a Tree class ==== */

class Tree {

    constructor(data) {
        this.data = data;
        this.children = []
    }

    addChild(node) {
        this.children.push(node);
    }

    printChildren() {
        for(const child of this.children) {
            console.log(child.data)
        }
    }

    printDescendants(child) {
        if(this.children.length === 0) console.log('No descendants');
        if(child) {
            console.log(child.data);
            if(child.children) {
                for(const des of child.children) this.printDescendants(des);
            }
            return;
        }
        for(const child of this.children) {
           this.printDescendants(child)
        }
    }

    isChild(node) {
        for(const child of this.children) {
            if(child === node) return true;
        }
        return false;
    }

    // isDescendant(node) {
    //     for(const child of this.children) {
    //         if(child === node) return true
    //     }
    // }
}

// const tree1 = new Tree(1);
// const tree2 = new Tree(2);
// const tree3 = new Tree(3);
// const tree4 = new Tree(4);
// const tree5 = new Tree(5);

// tree1.addChild(tree2);
// tree1.addChild(tree3);
// tree2.addChild(tree4);
// tree2.addChild(tree5);

// // tree1.printChildren();
// tree1.printDescendants();
// console.log(tree2.isChild(tree5))

module.exports = Tree;