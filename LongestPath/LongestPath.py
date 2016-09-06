class Solution(object):
    def lengthLongestPath(self, input):
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.strip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(pathlen[depth]+len(name), maxlen)
            else:
                if depth+1 not in pathlen:
                    pathlen[depth + 1] = 0
                pathlen[depth + 1] = max(pathlen[depth]+len(name) + 1, pathlen[depth+1])
        print(pathlen)
        return maxlen



if __name__ == '__main__':
    s= Solution()
    a = s.lengthLongestPath("dir\n\tsubdir1aaaaaaaaaaaaaaaaaa\n\t\ta.ext\n\tsubdir2\n\t\tfile.ext")
    print("dir\n\tsubdir1aaaaaaaaaaaaaaaaaa\n\t\ta.ext\n\tsubdir2\n\t\tfile.ext")
    b = s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
    c = s.lengthLongestPath("a\n\taa\n\taaa\n\tfile1.txt")
    print("a\n\taa\n\taaa\n\tfile1.txt")
    d = s.lengthLongestPath("aaaaaaaaaaaaaaaaaaaaa\n\tsth.png")
    print("Longest Length: "+ str(a))
    print("Longest Length: "+ str(b))
    print("Longest Length: " + str(c))
    print("Longest Length: " + str(d))