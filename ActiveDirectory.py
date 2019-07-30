class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.users:
        return True
    for g in group.groups:
        if is_user_in_group(user, g):
            return True
    return False

if __name__ == "__main__":
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print("check sub_child_user in child: \n")
    print(is_user_in_group(sub_child_user,child))
    # True

    print("check sub_child_user in parent: \n")
    print(is_user_in_group(sub_child_user,parent))
    # True

    print("check haha not in child: \n")
    print(is_user_in_group("haha",child))
    # False

"""
explanation: 

Effciency: 

Space Complexity:

O(n) where n is all the possible users in the current group, including users in the sub-group.

This is because recursion takes call stack space.

Time Complexity:

O(n) where n is all the possible users in the current group, including users in the sub-group.

Design Choice: Recursion that check each user and its sub-group if not found.
"""



