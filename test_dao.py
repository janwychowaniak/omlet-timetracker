from dao import TaskEntry
from dao import DAO
import pytest



class TestTaskEntry(object):


	def test_te_throwup_content(self):


		line1 = TaskEntry()
		line1.set_time('123')
		line1.set_string('a multiword phrase')

		assert line1.throwup_content() == '123:a multiword phrase'


		line2 = TaskEntry()
		line2.set_time('223')
		line2.set_string('1 number, some commas')

		assert line2.throwup_content() == '223:1 number, some commas'

		line3 = TaskEntry()
		line3.set_time('323')
		line3.set_string('some:additional:colons')

		assert line3.throwup_content() == '323:some:additional:colons'



	def test_te_load_content(self):
		

		line1 = TaskEntry()
		line1.load_content('123:a multiword phrase')

		assert line1.tasktime == '123'
		assert line1.taskstring == 'a multiword phrase'


		line2 = TaskEntry()
		line2.load_content('223:1 number, some commas')

		assert line2.tasktime == '223'
		assert line2.taskstring == '1 number, some commas'


		line3 = TaskEntry()
		line3.load_content('323:some:additional:colons')

		assert line3.tasktime == '323'
		assert line3.taskstring == 'some:additional:colons'



	def test_te_load_throwup(self):
		
		line1 = TaskEntry()
		line1.load_content('123:a multiword phrase')

		assert line1.throwup_content() == '123:a multiword phrase'



class TestDAO(object):


	def test_empty(self):

		data1 = DAO([])
		assert data1.is_empty()

		testDataContent = [
		  '648:abcdefghi',
		  '517:QjhWkizN5t',
		  '323:dwcIY99gTN1',
		  '653:UlfY2UvMfeuX'
		]
		data2 = DAO(testDataContent)
		assert not data2.is_empty()


	def test_find(self):
		
		testDataContent = [
		  '648:abcdefghi',
		  '517:QjhWkizN5t',
		  '323:dwcIY99gTN1',
		  '653:UlfY2UvMfeuX'
		]
		data1 = DAO(testDataContent)

		found = data1.find('abcdefghi')
		assert found.tasktime == '648' and found.taskstring == 'abcdefghi'

		notFound = data1.find('nonexistent')
		assert notFound is None


	def test_add_entry(self):

		data1 = DAO([])
		assert data1.is_empty()

		data1.add_entry('648', 'abcdefghi')

		assert not data1.is_empty()

		found = data1.find('abcdefghi')
		assert found.tasktime == '648' and found.taskstring == 'abcdefghi'

		with pytest.raises(Exception):
			data1.add_entry('648', 'abcdefghi')
			data1.add_entry('000', 'abcdefghi')


	def test_remove_entry(self):

		testDataContent = [
		  '648:abcdefghi',
		  '517:QjhWkizN5t',
		  '323:dwcIY99gTN1',
		  '653:UlfY2UvMfeuX'
		]
		data1 = DAO(testDataContent)
		assert data1.find('abcdefghi')

		data1.remove_entry('abcdefghi')
		assert data1.find('abcdefghi') is None

		with pytest.raises(Exception):
			data1.remove_entry('abcdefghi')


	def test_reset_time(self):

		testDataContent = [
		  '648:abcdefghi',
		  '517:QjhWkizN5t',
		  '323:dwcIY99gTN1',
		  '653:UlfY2UvMfeuX'
		]
		data1 = DAO(testDataContent)

		with pytest.raises(Exception):
			data1.reset_time('nonexistent')

		data1.reset_time('abcdefghi')

		assert data1.find('abcdefghi').tasktime == '0'


	def test_update_time(self):

		testDataContent = [
		  '648:abcdefghi',
		  '517:QjhWkizN5t',
		  '323:dwcIY99gTN1',
		  '653:UlfY2UvMfeuX'
		]
		data1 = DAO(testDataContent)

		with pytest.raises(Exception):
			data1.update_time('nonexistent', '30')

		data1.update_time('abcdefghi', '30')

		assert data1.find('abcdefghi').tasktime == '30'


	def test_advance_time(self):

		testDataContent = [
		  '648:abcdefghi',
		  '517:QjhWkizN5t',
		  '323:dwcIY99gTN1',
		  '653:UlfY2UvMfeuX'
		]
		data1 = DAO(testDataContent)

		with pytest.raises(Exception):
			data1.advance_time('nonexistent', '30')

		data1.advance_time('abcdefghi', '30')

		assert data1.find('abcdefghi').tasktime == '678'

