import os
import sys


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, "r", encoding="utf-8") as f:
            tokens = []
            for line in f:
                tokens += line.split()

        if len(tokens) == 0 or tokens[0].lower() == "n":
            return None

        root = cls(int(tokens[0]))
        queue = [root]
        i = 1

        while len(queue) > 0 and i < len(tokens):
            current = queue.pop(0)

            if i < len(tokens):
                if tokens[i].lower() != "n":
                    current.left = cls(int(tokens[i]))
                    queue.append(current.left)
                i += 1

            if i < len(tokens):
                if tokens[i].lower() != "n":
                    current.right = cls(int(tokens[i]))
                    queue.append(current.right)
                i += 1

        return root

    def sum_of_depths(self):
        def rec(node, depth):
            if node is None:
                return 0
            return depth + rec(node.left, depth + 1) + rec(node.right, depth + 1)

        return rec(self, 0)

    def height(self):
        def rec(node):
            if node is None:
                return 0
            return 1 + max(rec(node.left), rec(node.right))

        return rec(self)

    def show(self, vgap=3):
        def node_text(n):
            return "(" + str(n.value) + ")"

        h = self.height()

        max_len = 1
        stack = [self]
        while len(stack) > 0:
            cur = stack.pop()
            if cur is None:
                continue
            max_len = max(max_len, len(node_text(cur)))
            stack.append(cur.left)
            stack.append(cur.right)

        node_w = max(3, max_len)

        leaf_gap = max(1, node_w - 1)

        width = (2 ** h) * leaf_gap + node_w + 2
        height_lines = (h - 1) * vgap + 2

        canvas = [list(" " * width) for _ in range(height_lines)]

        def put_text(y, x_center, text):
            start = x_center - len(text) // 2
            start = max(0, min(width - len(text) - 1, start))
            for k in range(len(text)):
                canvas[y][start + k] = text[k]

        def node_center(depth, index_on_level):
            step = (2 ** (h - depth)) * leaf_gap
            x = (step // 2) + index_on_level * step
            y = depth * vgap
            return y, x

        def draw_edge(py, px, cy, cx):
            dy = cy - py
            if dy <= 0:
                return

            direction = 1 if cx > px else -1

            diag_steps = max(1, dy - 2)
            y = py + 1
            x = px + direction

            for _ in range(diag_steps):
                if 0 <= y < height_lines and 0 <= x < width:
                    canvas[y][x] = "\\" if direction == 1 else "/"
                y += 1
                x += direction

            hy = min(cy - 1, y)
            if 0 <= hy < height_lines:
                start = min(x, cx)
                end = max(x, cx)

                for xx in range(start, end + 1):
                    if 0 <= xx < width and canvas[hy][xx] == " ":
                        canvas[hy][xx] = "-"

                if 0 <= cx < width:
                    canvas[hy][cx] = "\\" if direction == 1 else "/"

        def draw(cur, depth, idx):
            if cur is None:
                return

            y, x = node_center(depth, idx)
            put_text(y, x, node_text(cur))

            if cur.left is not None:
                ly, lx = node_center(depth + 1, idx * 2)
                draw_edge(y, x, ly, lx)
                draw(cur.left, depth + 1, idx * 2)

            if cur.right is not None:
                ry, rx = node_center(depth + 1, idx * 2 + 1)
                draw_edge(y, x, ry, rx)
                draw(cur.right, depth + 1, idx * 2 + 1)

        draw(self, 0, 0)

        for row in canvas:
            print("".join(row).rstrip())


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))z
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if not os.path.isabs(file_path):
            file_path = os.path.join(here, file_path)
    else:
        file_path = os.path.join(here, "1.txt")

    root = TreeNode.load_from_file(file_path)

    if root is None:
        print("N")
        print("sum =", 0)
    else:
        root.show(vgap=3)
        print("sum =", root.sum_of_depths())