import unittest
import YTvideoList
import videoInfo
import comments

class Test_YTInfo(unittest.TestCase):
    def test_YTvideoList(self):
        self.assertEqual(type(YTvideoList.getvideoIdList('UCsAjl9dMJFLYnAobCWLWjmA')), list)
        self.assertLessEqual(len(YTvideoList.getvideoIdList('UCsAjl9dMJFLYnAobCWLWjmA')), 10)

    def test_videoInfo(self):
        self.assertEqual(type(videoInfo.getVideoInfo('nFZpJGoGjHI')), dict)
        self.assertEqual(type(videoInfo.getVideoInfo('nFZpJGoGjHI')['items']), list)

    def test_comments(self):
        self.assertEqual(type(comments.getComments('nFZpJGoGjHI')), dict)
        self.assertEqual(type(comments.getComments('nFZpJGoGjHI')['items']), list)

if __name__ == '__main__':
    unittest.main()