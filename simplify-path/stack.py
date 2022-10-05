from inspect import stack


class Path:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for directory in path.split('/'):
            if directory == '':
                pass
            elif directory == '.':
                pass
            elif directory == '..':
                if stack:
                    stack.pop()
                else:
                    pass
            else:
                if directory:
                    stack.append(directory)
        return stack
