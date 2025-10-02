# Windows-compatible simulation of Linux File Permissions

class File:
    def __init__(self, name, owner, group, permissions):
        """
        permissions: string like 'rwxr-xr--'
        """
        self.name = name
        self.owner = owner
        self.group = group
        self.permissions = permissions  # 9-char string

    def check_permission(self, user, action):
        """
        user: (username, groupname)
        action: 'r' (read), 'w' (write), 'x' (execute)
        """
        username, groupname = user

        # Decide which 3-char set to use
        if username == self.owner:
            perm_set = self.permissions[0:3]
        elif groupname == self.group:
            perm_set = self.permissions[3:6]
        else:
            perm_set = self.permissions[6:9]

        # Check action
        if action in perm_set:
            return True
        return False


if __name__ == "__main__":
    # Create a file with permissions rwxr-xr--
    file1 = File("demo.txt", owner="alice", group="dev", permissions="rwxr-xr--")

    users = [
        ("alice", "dev"),   # owner
        ("bob", "dev"),     # same group
        ("charlie", "test") # others
    ]

    actions = ["r", "w", "x"]

    for user in users:
        print(f"\nUser: {user[0]} (Group: {user[1]}) trying actions on {file1.name}:")
        for act in actions:
            result = "✅ Allowed" if file1.check_permission(user, act) else "❌ Denied"
            print(f"  {act.upper()} → {result}")
