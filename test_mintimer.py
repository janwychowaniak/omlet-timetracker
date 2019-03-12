import pytest
import time

from mintimer import Mintimer


def test_cant_start_twice():

	timer1 = Mintimer()
	timer1.start()

	with pytest.raises(Exception):
		timer1.start()


def test_cant_stop_twice():

	timer1 = Mintimer()

	with pytest.raises(Exception):
		timer1.stop()

	timer1.start()
	timer1.stop()

	with pytest.raises(Exception):
		timer1.stop()
