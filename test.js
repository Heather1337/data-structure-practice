const Tree = require('./tree');


const tree1 = new Tree(15)

test('Adds node to a tree', () => {
    expect(tree1.data).toBe(15);
});