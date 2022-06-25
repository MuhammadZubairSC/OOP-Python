from datetime import datetime
class Machine():
    def __init__(self):
        self.users={}
        self.usersLogout={}
        self.event={}
        self.loginTime={}
        self.logoutTime={}
    def users_add(self, user):
        self.users[user]=[datetime.now().strftime("%Y-%m-%d-%H-%M-%S"), "Login"]
        
    def users_logout(self, user):
        self.usersLogout[user]=[users[user][0], users[user][1], datetime.now().strftime("%Y-%m-%d-%H-%M-%S"), "Logout"]
        del self.users[user]
        
    def load(self):
        """Calculates the current load for all users."""
        total = 0
        # Add up the load for each of the connections
        total=len(self.users)
        print("Totol {}".format(total))
        return total
    def __str__(self):
        return "Total number of users logged in are {}:".format(len(self.users))
    

class System():
    def __init__(self):
        self.machines=[Machine()]
        self.machineReport={}
    def User_add(self, user_id):
        self.MachineLoad()
        print(self.machines[-1])
        self.machines[-1].users_add(user_id)
    def Users_in_Machine(self):
        for i in self.machines:
            self.machineReport[i]=i.users
    def MachineLoad(self):
        LoadUsers=0 
        for i in self.machines:
            LoadUsers+=i.load()
        print(LoadUsers)
        if LoadUsers>25:
            self.machines.append(Machine())


report = System()
for i in range(51):
    report.User_add("Tony"+str(i))
report.User_add("Leny")
report.Users_in_Machine()
print(report.machineReport)
        