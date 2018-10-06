import unittest
from app.registration import UserDetails

class Test_user(unittest.TestCase):


    def setUp(self):
        self.user = UserDetails()
 
    #Validate method
    def test_validate_method_does_validates_successfully(self):
        validate = self.user.validate_data("kelraf", "rafwambugu@gmail.com", "kelraf11746", "kelraf11746") 
        self.assertTrue(validate) 

    def test_validate_method_with_incorrect_email(self):
        response1 = self.user.validate_data("kelraf", "rafwambugugmail.com", "kelraf11746", "kelraf11746") 
        self.assertEqual(response1, "Username or email can only contain alphanumeric characters")  

    def test_validate_method_with_username_less_than_6_characters(self):
        response2 = self.user.validate_data("kelra", "rafwambugu@gmail.com", "kelraf11746", "kelraf11746") 
        self.assertEqual(response2, "Your username should be atleast six characters long")

    def test_validate_method_with_undefined_character(self):
        response3 = self.user.validate_data("kelra$f", "rafwambugu@gmail.com", "kelraf11746", "kelraf11746")  
        self.assertEqual(response3, "Username or email can only contain alphanumeric characters") 

    def test_validate_method_with_a_password_less_than_six_characters(self):
        response4 = self.user.validate_data("kelraf", "rafwambugu@gmail.com", "kelr", "kelr") 
        self.assertEqual(response4, "Your password should be atleast six characters long")  

    def test_validate_method_with_passwords_that_dont_match(self):
        response5 = self.user.validate_data("kelraf", "rafwambugu@gmail.com", "kelraf11746", "kelraf11744")    
        self.assertEqual(response5, "Your passwords must match")   


    #Registration Method
    def test_registration_method_if_registers_successfully(self):
        register = self.user.register("kelraf", "rafwambugu@gmail.com", "kelraf11746", "kelraf11746")
        self.assertEqual(register, "user registered successfully")

    def test_registration_method_if_raises_alarm_when_a_user_is_registered_twice(self):
        response6 = self.user.register("kelraf", "rafwambugu@gmail.com", "kelraf11746", "kelraf11746")   
        response7 = self.user.register("kelraf", "rafwambugu@gmail.com", "kelraf11746", "kelraf11746")
        self.assertEqual(response7, "Username or email already exists") 
        self.assertEqual(response6, "user registered successfully") 

    def test_registration_method_if_registers_a_second_user_succeessfully(self):
        reg = self.user.register("kelraf", "rafwambugu@gmail.com", "kelraf11746", "kelraf11746")
        response8 = self.user.register("kelrar", "rafkelwambugu@gmail.com", "kelraf11746", "kelraf11746")
        self.assertEqual(response8, "user registered successfully second") 

    def test_register_method_returns_an_error_message_given_an_invalid_email(self):
        register1 = self.user.register("kelrar", "rafkelwambugugmail.com", "kelraf11746", "kelraf11746") 
        self.assertEqual(register1, "Username or email can only contain alphanumeric characters") 

    def  test_register_method_returns_an_error_message_given_an_invalid_username(self):
        register2 = self.user.register("kelra@r", "rafkelwambugu@gmail.com", "kelraf11746", "kelraf11746")
        self.assertEqual(register2, "Username or email can only contain alphanumeric characters") 

    def test_register_method_returns_an_error_message_given_a_password_less_than_six_characters(self):
        register3 = self.user.register("kelrar", "rafkelwambugu@gmail.com", "kelr", "kelr")   
        self.assertEqual(register3, "Your password should be atleast six characters long") 

    #Login Method
    def test_login_method_works_correctly(self):
        self.user.register("kelraf", "rafwambugu@gmail.com", "kelraf11746", "kelraf11746")
        login1 = self.user.login("kelraf", "kelraf11746") 
        self.assertTrue(login1)

    def test_login_method_with_an_incorrect_password(self):
        self.user.register("kelraf", "rafwambugu@gmail.com", "kelraf11746", "kelraf11746")
        login1 = self.user.login("kelraf", "kelraf11745") 
        self.assertEqual(login1, "Usename and password or both do not exist") 

    def test_login_method_with_an_incorrect_username(self):
        self.user.register("kelraf", "rafwambugu@gmail.com", "kelraf11746", "kelraf11746")
        login1 = self.user.login("kelrafe", "kelraf1174") 
        self.assertEqual(login1, "Usename and password or both do not exist") 

    #Reset Method
    def test_reset_password_method_if_works_correctly(self):
        reg4 = self.user.register("kelraf", "rafwambugu@gmail.com", "kelraf11746", "kelraf11746")  
        reset1 = self.user.reset_password("kelraf", "kelraf11746", "kelrafwin")               
        self.assertEqual(reset1, "You have successfully updated your password")

    def test_reset_method_raises_error_with_new_password_lessthan_six_characters(self):
        reg4 = self.user.register("kelraf", "rafwambugu@gmail.com", "kelraf11746", "kelraf11746")  
        reset1 = self.user.reset_password("kelraf", "kelraf11746", "kelra")               
        self.assertEqual(reset1, "Your password must be atleast six characters")

    def test_reset_method_returns_an_error_message_given_same_password_as_earlier_one(self):
        reg4 = self.user.register("kelraf", "rafwambugu@gmail.com", "kelraf11746", "kelraf11746")  
        reset1 = self.user.reset_password("kelraf", "kelraf11746", "kelraf11746")               
        self.assertEqual(reset1, "Your initial password and new password are same")

    def test_reset_method_raises_error_given_parameters_that_do_not_exist(self):
        reset1 = self.user.reset_password("kelraf", "kelraf11746", "kelraf11746")               
        self.assertEqual(reset1, "You cannot reset password because username and password or both are not details of any user in the program")  