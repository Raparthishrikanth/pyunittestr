import selenium_test_module
import unittest
from read_sheet import *
from helper_module import *



class MyTestCase(unittest.TestCase):
    def test_something(self):
        #loop through rows in xls
        for i in range(len(data)):
            if data[i]['Run'].lower()=='y':
                print("run the below")
                url_value = data[i]['URL']
                password_value=data[i]['password']
                username_value=data[i]['username']

                print(url_value)
                print(password_value)
                print(username_value)

                selenium_test_module_instance = selenium_test_module.SeleniumClass()

                selenium_test_module_instance.setUp()
                selenium_test_module_instance.go_to_url(url_value)
                selenium_test_module_instance.teardown()
                """Clean up screenshots. Move the files to relevant folders in Screenshots directory"""
                move_png(i + 1)

            elif data[i]['Run'].lower() == 'n':
                print("Don't run row " + str(i + 1))
                # tkMessageBox.showinfo("Information", "'" + Name_of_site + "'" + " not run")
            elif data[i]['Run'].lower() != 'n' or data[i]['Run'].lower() != 'y':
                print("enter something useful: Y or N")
            else:
                pass



if __name__ == '__main__':
    unittest.main()
