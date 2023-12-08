from unittest import TestCase, main
class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.cat = Cat("Test")

    def test_successful_initial(self):
        self.assertEqual("Test", self.cat.name)
        self.assertEqual(False, self.cat.fed)
        self.assertEqual(False, self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_unsuccessful_eat_raise_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_successful_eat(self):
        self.cat.eat()

        self.assertEqual(True, self.cat.fed)
        self.assertEqual(True, self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_unsuccessful_sleep_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_successful_sleep(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertEqual(False, self.cat.sleepy)


if __name__ == "__main__":
    main()
