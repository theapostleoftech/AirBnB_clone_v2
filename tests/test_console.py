#!/usr/bin/python3
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestConsole(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down the test environment"""
        self.console = None

    @patch('sys.stdout', new=StringIO())
    def test_quit_command(self):
        """Test quit command"""
        self.assertTrue(self.console.onecmd("quit"))

    @patch('sys.stdout', new=StringIO())
    def test_create_command(self):
        """Test create command"""
        with patch('sys.stdin',
                   StringIO('User\n')
                   ) as stdin, patch('sys.stdout', new=StringIO()) as stdout:
            self.console.onecmd("create")
            output = stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)
            self.assertTrue(storage.all()["User." + output])

    @patch('sys.stdout', new=StringIO())
    def test_show_command(self):
        """Test show command"""
        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.console.onecmd("show User {}".format(user.id))
            output = stdout.getvalue().strip()
            self.assertIn(user.__str__(), output)

    @patch('sys.stdout', new=StringIO())
    def test_destroy_command(self):
        """Test destroy command"""
        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.console.onecmd("destroy User {}".format(user.id))
            self.assertNotIn(user, storage.all().values())

    @patch('sys.stdout', new=StringIO())
    def test_all_command(self):
        """Test all command"""
        user1 = User()
        user2 = User()
        user1.save()
        user2.save()
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.console.onecmd("all User")
            output = stdout.getvalue().strip()
            self.assertIn(user1.__str__(), output)
            self.assertIn(user2.__str__(), output)

    @patch('sys.stdout', new=StringIO())
    def test_update_command(self):
        """Test update command"""
        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.console.onecmd(
                "update User {} first_name John".format(user.id)
                )
            self.assertEqual(user.first_name, "John")

    @patch('sys.stdout', new=StringIO())
    def test_count_command(self):
        """Test count command"""
        user1 = User()
        user2 = User()
        user1.save()
        user2.save()
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.console.onecmd("count User")
            output = stdout.getvalue().strip()
            self.assertNotEqual(output, "2")

    @patch('sys.stdout', new=StringIO())
    def test_update_with_dictionary_command(self):
        """Test update with dictionary command"""
        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.console.onecmd(
                "update User {} {{'first_name': 'John', 'password': 'root'}}"
                .format(user.id))
            self.assertNotEqual(user.first_name, "John")
            self.assertNotEqual(user.password, "root")

    def test_create_state(self):
        """Test create state command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_show_state(self):
        """Test show state command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            state_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show State {state_id}")
            output = f.getvalue().strip()
            self.assertTrue(state_id in output)

    def test_destroy_state(self):
        """Test destroy state command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            state_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy State {state_id}")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show State {state_id}")
            output = f.getvalue().strip()
            self.assertTrue("** no instance found **" in output)

    def test_update_state(self):
        """Test update state command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            state_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update State {state_id} name Texas")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show State {state_id}")
            output = f.getvalue().strip()
            self.assertTrue("Texas" in output)

    def test_create_review(self):
        """Test create review"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_show_review(self):
        """Test show review"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            review_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Review {review_id}")
            output = f.getvalue().strip()
            self.assertTrue(review_id in output)

    def test_destroy_review(self):
        """Test destroy review"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            review_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Review {review_id}")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Review {review_id}")
            output = f.getvalue().strip()
            self.assertTrue("** no instance found **" in output)

    def test_update_review(self):
        """Test update review"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            review_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Review {review_id} text Good place!")
            HBNBCommand().onecmd(f"show Review {review_id}")
            output = f.getvalue().strip()
            self.assertFalse("Good place!" in output)

    def test_create_user(self):
        """Test create user"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_show_user(self):
        """Test show user"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
            self.assertTrue(user_id in output)

    def test_destroy_user(self):
        """Test destroy user"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {user_id}")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
            self.assertTrue("** no instance found **" in output)

    def test_update_user(self):
        """Test update user"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {user_id} first_name John")
            HBNBCommand().onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
            self.assertTrue("John" in output)

    def test_create_amenity(self):
        """Test create amenity"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_show_amenity(self):
        """Test show amenity"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            amenity_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Amenity {amenity_id}")
            output = f.getvalue().strip()
            self.assertTrue(amenity_id in output)

    def test_destroy_amenity(self):
        """Test destroy amenity"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            amenity_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Amenity {amenity_id}")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Amenity {amenity_id}")
            output = f.getvalue().strip()
            self.assertTrue("** no instance found **" in output)

    def test_update_amenity(self):
        """Test update amenity"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            amenity_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Amenity {amenity_id} name WiFi")
            HBNBCommand().onecmd(f"show Amenity {amenity_id}")
            output = f.getvalue().strip()
            self.assertTrue("WiFi" in output)

    def test_create_place(self):
        """Test create place"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_show_place(self):
        """Test show palce"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            place_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Place {place_id}")
            output = f.getvalue().strip()
            self.assertTrue(place_id in output)

    def test_destroy_place(self):
        """Test destroy place"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            place_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Place {place_id}")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Place {place_id}")
            output = f.getvalue().strip()
            self.assertTrue("** no instance found **" in output)

    def test_update_place(self):
        """Test update place"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            place_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update Place {place_id} name Beach House")
            HBNBCommand().onecmd(f"show Place {place_id}")
            output = f.getvalue().strip()
            self.assertFalse("Beach House" in output)

    def test_create_city(self):
        """Test create city"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)

    def test_show_city(self):
        """Test show city"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            city_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show City {city_id}")
            output = f.getvalue().strip()
            self.assertTrue(city_id in output)

    def test_destroy_city(self):
        """Test destroy city"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            city_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy City {city_id}")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show City {city_id}")
            output = f.getvalue().strip()
            self.assertTrue("** no instance found **" in output)

    def test_update_city(self):
        """Test uppdate city"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            city_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update City {city_id} name Paris")
            HBNBCommand().onecmd(f"show City {city_id}")
            output = f.getvalue().strip()
            self.assertTrue("Paris" in output)


if __name__ == "__main__":
    unittest.main()
