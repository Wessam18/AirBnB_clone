#!/usr/bin/python3
"""to test review class"""

import unittest
import os
import models
from datetime import datetime, timedelta
from time import sleep
from unittest.mock import patch
from models.review import Review


class TestReview(unittest.TestCase):
    """test review class"""

    @classmethod
    def setUp(cls):
        """setup the test"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """setup the test"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_review_instance(self):
        """test init"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_attributes(self):
        """test attribute"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_two_reviews_ids(self):
        """test id"""
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_two_reviews_created_at(self):
        """test createat"""
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.created_at, review2.created_at)

    def test_two_reviews_updated_at(self):
        """test updatedat"""
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.updated_at, review2.updated_at)

    def test_save_method(self):
        """test save"""
        with patch('models.storage.save') as mock_save:
            review = Review()
            review.save()
            mock_save.assert_called_once()

    def test_to_dict_method(self):
        """test dict"""
        review = Review()
        obj_dict = review.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)

    def test_init_with_kwargs(self):
        """test init"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        review = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(review.id, "345")
        self.assertEqual(review.created_at, dt)
        self.assertEqual(review.updated_at, dt)

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_save_review(self):
        """test save method"""
        new_review = Review()
        old_update_at = new_review.updated_at
        old_created_at = new_review.created_at
        sleep(1)
        new_review.save()
        self.assertTrue((new_review.updated_at > old_update_at))
        self.assertTrue(old_created_at == new_review.created_at)

    def test_to_dict_review(self):
        """test dict"""
        new_review = Review()
        new_review.text = "test_to_dict"
        actual_dict = new_review.to_dict()
        self.assertIsNotNone(actual_dict)
        self.assertIsInstance(actual_dict["id"], str)
        self.assertIsInstance(actual_dict["created_at"], str)
        self.assertIsInstance(actual_dict["updated_at"], str)
        self.assertEqual(actual_dict["__class__"], "Review")
        self.assertEqual(actual_dict["id"], new_review.id)
        self.assertEqual(actual_dict["text"], new_review.text)
        self.assertEqual(actual_dict["text"], "test_to_dict")


if __name__ == '__main__':
    unittest.main()
