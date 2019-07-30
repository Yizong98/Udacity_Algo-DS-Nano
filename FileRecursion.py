
import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    ans = []
    def DFS(suffix,path):
      if os.path.isfile(path):
        if path.endswith(".c"):
          ans.append(path)
      elif os.path.isdir(path):
        for elem in os.listdir(path):
          DFS(suffix,os.path.join(path,elem))
      else:
        print("Please enter valid path!")
    DFS(suffix,path)
    return ans
if __name__ == "__main__":
  print("The Paths that end with .c are \n")
  print(find_files(".c",input("Type your path \n")))
  # test case: ./testdirs
  # result: "Please enter valid path!" []
  # test case ./testdir
  # result: [./testdir/subdir1/a.c, ./testdir/subdir3/subsubdir1/b.c, ./testdir/subdir5/a.c, ./testdir/t1.c]

"""
explanation: 

Effciency:

Space Complexity:

1. O(n) where n refers to total number of possible paths in the directory, also
the size of call stack in recursion.


Time Complexity:

1. O(n) where n refers to total number of possible paths in the directory.

Design Choice:

Simple Recursion and conditional checking
"""