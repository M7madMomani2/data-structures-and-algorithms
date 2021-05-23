from Data_Structures.stacks_and_queues.stacks_and_queues import *
import pytest

def test_push(stack_op):
    stack_op.push(3)
    stack_op.push(1)
    assert stack_op.top.value == 1
    assert stack_op.top.next.value == 3

def test_pop(stack_op):
    assert stack_op.top.value == 6
    assert stack_op.pop() == 6
    assert stack_op.top.value == 7

def test_empty(stack_op):
    stack_op.pop()
    stack_op.pop()
    stack_op.pop()
    assert stack_op.top == None

def test_peek(stack_op):
    assert stack_op.peek() == 6

def test_is_empty(stack_op):
    assert stack_op.isEmpty() == False


def test_enqueue(queue_op):
    queue_op.enqueue(3)
    queue_op.enqueue(1)
    assert queue_op.rear.value == 1


def test_dequeue(queue_op):
    assert queue_op.dequeue() == 8
    assert queue_op.front.value == 7


def test_peek_q(queue_op):
    assert queue_op.peek() == 8
    assert queue_op.front.value == 8


def test_empty_q(queue_op):
    queue_op.dequeue()
    queue_op.dequeue()
    queue_op.dequeue()
    assert queue_op.isEmpty() == True


def test_is_empty_q(queue_op):
    assert queue_op.isEmpty() == False


@pytest.fixture
def stack_op():
        stack1=Stack()
        stack1.push(8)
        stack1.push(7)
        stack1.push(6)
        return stack1

@pytest.fixture
def queue_op():
        queue1=Queue()
        queue1.enqueue(8)
        queue1.enqueue(7)
        queue1.enqueue(6)
        return queue1
