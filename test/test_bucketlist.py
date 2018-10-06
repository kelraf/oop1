import unittest
from app.bucketlist import UserBucketlist

 
class Test_bucketlist(unittest.TestCase):

    def setUp(self):
        self.bucketlist = UserBucketlist()

    #Create_bucketlist Method
    def test_create_bucketlist_method_if_creates_first_backetlist_successfully(self):
        response1 = self.bucketlist.create_bucketlist("My first bucketlist", "going to canada", "These is the content", "kelraf")
        self.assertEqual(response1, "You have created your first bucketlist successfully")

    def test_create_bucketlist_method_if_creates_more_than_one_bucketlist_successfully(self):
        response2 = self.bucketlist.create_bucketlist("My first bucketlist", "going to canada", "These is the content", "kelraf")
        response3 = self.bucketlist.create_bucketlist("My second bucketlist", "going to canada", "These is the content", "kelraf") 
        response4 = self.bucketlist.create_bucketlist("My third bucketlist", "going to canada", "These is the content", "kelraf") 
        self.assertEqual(response4, "Another bucketlist has been created successfully")

    def test_create_bucketlist_method_if_raises_error_given_two_bucketlists_with_same_name(self):
        response5 = self.bucketlist.create_bucketlist("My first bucketlist", "going to canada", "These is the content", "kelraf") 
        response6 = self.bucketlist.create_bucketlist("My first bucketlist", "going to canada", "These is the content", "kelraf")
        self.assertEqual(response6, "The Bucketlist name you provided already exists in your account")     

    #Update Method
    def test_update_method_if_works_as_expected(self):
        response7 = self.bucketlist.create_bucketlist("My first bucketlist", "going to canada", "These is the content", "kelraf")
        Update1 = self.bucketlist.update("My first bucketlist", "My third2 bucketlist", "going to canada", "going to canada and kk", "These is the content", "These is the content wewe", "kelraf")
        self.assertEqual(Update1, "bucketlist updated successfully")

    def test_update_method_if_can_update_a_backetlist_in_second_and_third_position(self):
        response9 = self.bucketlist.create_bucketlist("My first bucketlist", "going to canada", "These is the content", "kelraf")
        response12 = self.bucketlist.create_bucketlist("My second bucketlist", "going to canada", "These is the content", "kelraf") 
        response34 = self.bucketlist.create_bucketlist("My third bucketlist", "going to canada", "These is the content", "kelraf")
        update = self.bucketlist.update("My third bucketlist", "My third2 bucketlist", "going to canada", "going to canada and kk", "These is the content", "These is the content wewe", "kelraf") 
        self.assertEqual(update, "bucketlist updated successfully")  

    def test_update_method_if_can_raise_error_given_a_name_that_already_exists(self):
        response9 = self.bucketlist.create_bucketlist("My first bucketlist", "going to canada", "These is the content", "kelraf")
        response12 = self.bucketlist.create_bucketlist("My second bucketlist", "going to canada", "These is the content", "kelraf") 
        response34 = self.bucketlist.create_bucketlist("My third bucketlist", "going to canada", "These is the content", "kelraf")
        update2 = self.bucketlist.update("My third bucketlist", "My second bucketlist", "going to canada", "going to canada and kk", "These is the content", "These is the content wewe", "kelraf") 
        self.assertEqual(update2, "You already have a bucketlist with the name you provided in your account")  

    def test_update_method_if_can_raise_error_message_given_details_that_donot_exist(self):
        response7 = self.bucketlist.create_bucketlist("My first bucketlist", "going to canada", "These is the content", "kelraf")
        Update1 = self.bucketlist.update("My fi bucketlist", "My third2 bucketlist", "going to canada", "going to canada and kk", "These is the content", "These is the content wewe", "kelraf")
        self.assertEqual(Update1, "The details you provided are invalid")   

    #View Method
    def test_view_method_works_successfully(self):
        create_it = self.bucketlist.create_bucketlist("My first bucketlist", "going to canada", "These is the content", "kelraf")
        View1 = self.bucketlist.view("My first bucketlist") 
        self.assertTrue(View1) 

    def test_view_method_finds_second_and_third_bucketlists_in_the_program(self):
        response9 = self.bucketlist.create_bucketlist("My first bucketlist", "going to canada", "These is the content", "kelraf")
        response12 = self.bucketlist.create_bucketlist("My second bucketlist", "going to canada", "These is the content", "kelraf") 
        response34 = self.bucketlist.create_bucketlist("My third bucketlist", "going to canada", "These is the content", "kelraf")  
        view2 = self.bucketlist.view("My third bucketlist")   
        self.assertTrue(view2)  

    def test_view_method_if_raises_error_message_given_name_that_does_not_exist(self):
        view3 = self.bucketlist.view("My third bucketlist") 
        self.assertEqual(view3, "Your account does not have a bucketlist with the name you provided") 


    #Delete Method
    def test_del_method_if_works_correctly(self):
        create_it1 = self.bucketlist.create_bucketlist("My first bucketlist", "going to canada", "These is the content", "kelraf")
        del1 = self.bucketlist.delete("My first bucketlist")
        self.assertEqual(del1, "Bucketlist deleted successfully")

    def test_del_method_raises_error_give_incorrect_backetlist_name(self):
        del2 = self.bucketlist.delete("My first bucketlist")  
        self.assertEqual(del2, "The bucketlistname you provided does not exist in your account")

    def test_del_method_if_can_del_from_second_items(self):
        responsea = self.bucketlist.create_bucketlist("My first bucketlist", "going to canada", "These is the content", "kelraf")
        responseb = self.bucketlist.create_bucketlist("My second bucketlist", "going to canada", "These is the content", "kelraf") 
        responsec = self.bucketlist.create_bucketlist("My third bucketlist", "going to canada", "These is the content", "kelraf")             
        del3 = self.bucketlist.delete("My third bucketlist")
        self.assertEqual(del3, "Bucketlist deleted successfully")       