class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def is_mirror(a, b):
            if a is None and b is None:
                return True

            if a is None or b is None:
                return False

            return (
                a.val == b.val
                and is_mirror(a.left, b.right)
                and is_mirror(a.right, b.left)
            )

        return is_mirror(root.left, root.right)