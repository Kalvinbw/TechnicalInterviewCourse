class Node {
    constructor(value) {
        this.left = null;
        this.right = null;
        this.data = value;
    }

    insert(value) {
        if (value === this.data) {
            return this
        }

        if (value < this.data) {
            if (!this.left) {
                this.left = new Node(value);
            } else {
                this.left.insert(value);
            }
        }
        else {
            if (!this.right) {
                this.right = new Node(value);
            } else {
                this.right.insert(value);
            }
        }
    }

    search(value) {
        if (value === this.data) {
            return true;
        }
    }

    delete(value) {

    }


    inOrderTraversal() {
        if (this.left !== null) {
            this.left.inOrderTraversal();
        }
        console.log(this.data);
        if (this.right !== null) {
            this.right.inOrderTraversal();
        }
    }
}

function delnode(value, node, parent) {
    if (node.data === value) {
        
    }
}

root = new Node(50);
root.insert(40);
root.insert(60);
root.insert(30);
root.insert(45);
root.insert(55);
root.insert(70);

root.insert(35);

root.inOrderTraversal();
