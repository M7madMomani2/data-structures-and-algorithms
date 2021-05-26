from data_structures.stacks_and_queues.stacks_and_queues import *
import pytest


def test_enqueue(queue_op):
    queue_op.enqueue(3)
    queue_op.enqueue(1)
    assert queue_op.rear.pop() == 1


def test_dequeue(queue_op):
    assert queue_op.dequeue() == 8
    assert queue_op.front.pop() == 'Empty Stack'


def test_empty_q(queue_op):
    queue_op.dequeue()
    queue_op.dequeue()
    queue_op.dequeue()
    assert queue_op.isEmpty() == True


def test_is_empty_q(queue_op):
    assert queue_op.isEmpty() == False



@pytest.fixture
def queue_op():
        queue1=PseudoQueue()
        queue1.enqueue(8)
        queue1.enqueue(7)
        queue1.enqueue(6)
        return queue1
