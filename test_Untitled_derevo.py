from Untitled_derevo import TreeNode, sum_of_depths 

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

result = sum_of_depths(root)
print("Test 1 result:", result)
assert result == 6

root2 = TreeNode(10)
result2 = sum_of_depths(root2)
print("Test 2 result:", result2)
assert result2 == 0

root3 = None
result3 = sum_of_depths(root3)
print("Test 3 result:", result3)
assert result3 == 0
print("done")
