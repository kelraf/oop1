''' The module defines user bucketlist and its methods'''
import uuid
from datetime import date

class UserBucketlist():
    def __init__(self):
        #A list to store user bucketlists
        self.user_bucketlists = []

    #A method to create user bucketlist
    def create_bucketlist(self, bucketlist_name, title, content, created_by):
        #A dictionary to store bucketlist details
        bucketlist_details = {}

        #check if there are bucketlists in users account
        if len(self.user_bucketlists) > 0:
            #loop through users bucketlist to make sure that one user cannot create 
            # more than one bucketlist with the same name 
            for bucketlist in self.user_bucketlists:
                if bucketlist_name == bucketlist['bucketlist_name'] and created_by == bucketlist['created_by']:
                    return "The Bucketlist name you provided already exists in your account"
            else:
                #create bucketlist
                bucketlist_details['bucketlist_name'] = bucketlist_name
                bucketlist_details['title'] = title
                bucketlist_details['content'] = content
                bucketlist_details['created_by'] = created_by
                bucketlist_details['date_created'] = date.today()
                bucketlist_details['id'] = uuid.uuid1()
                self.user_bucketlists.append(bucketlist_details)
                return "Another bucketlist has been created successfully"

        else:
            #The user does not have any bucketlist in his/her account
            #Let the user create the bucketlist directly
            bucketlist_details['bucketlist_name'] = bucketlist_name
            bucketlist_details['title'] = title
            bucketlist_details['content'] = content
            bucketlist_details['created_by'] = created_by
            bucketlist_details['date_created'] = date.today()
            bucketlist_details['id'] = uuid.uuid1()
            self.user_bucketlists.append(bucketlist_details)
            return "You have created your first bucketlist successfully"


    #A method to update bucketlist
    def update(self, bucketlist_name, new_bucketlist_name, title, new_title, content, new_content, created_by):
        for bucketlist in self.user_bucketlists:
            if bucketlist['bucketlist_name'] == bucketlist_name and bucketlist['created_by'] == "kelraf":
                for bucketlist in self.user_bucketlists:
                   if bucketlist['bucketlist_name'] == new_bucketlist_name:
                        return "You already have a bucketlist with the name you provided in your account"
                else:
                    #update backetlist
                    bucketlist['bucketlist_name'] = new_bucketlist_name
                    bucketlist['title'] = new_title
                    bucketlist['content'] = new_content
                    bucketlist['created_by'] = created_by
                    return "bucketlist updated successfully"
                    
        else:
            return "The details you provided are invalid"          
                
                    
                
                    

    #A method to view bucketlist
    def view(self, bucketlist_name):
        for bucketlist in self.user_bucketlists:
            if bucketlist_name == bucketlist['bucketlist_name']:
                return True
        else:
            return "Your account does not have a bucketlist with the name you provided"


    #A method to delete backetlist
    def delete(self, bucketlist_name):
        for bucketlist in self.user_bucketlists:
            if bucketlist_name == bucketlist['bucketlist_name']:
                self.user_bucketlists.remove(bucketlist)
                return "Bucketlist deleted successfully"
        else:
            return "The bucketlistname you provided does not exist in your account"    
    

def run():
    Bucketlist = UserBucketlist()

    response = Bucketlist.create_bucketlist("My first bucketlist", "going to canada", "These is the content", "kelraf")
    print(response)

    response1 = Bucketlist.create_bucketlist("My second bucketlist", "going to canada", "These is the content", "kelraf")  
    print(response1)

    response2 = Bucketlist.create_bucketlist("My third bucketlist", "going to canada", "These is the content", "kelraf")
    print(response2)

    response3 = Bucketlist.delete("My second bucketlist")
    print(response3)

    response4 = Bucketlist.view("My third bucketlist")
    print(response4)

    response5 = Bucketlist.update("My third bucketlist", "My third2 bucketlist", "going to canada", "going to canada and kk", "These is the content", "These is the content wewe", "kelraf")
    print(response5)


if __name__ == "__main__":
    run()              
                        