from model_mommy import mommy
import pytest
import string
import random

from core.models import Book, BookNode


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_node(parent=None):
    node = BookNode(
        parent=parent,
        node_class=id_generator(10),
        node_type=id_generator(10),
        number=random.randint(1, 100),
        title=id_generator(20),
        is_readonly=False,
        node_id=random.randint(1, 100),
        mpath=id_generator(20),
        label=id_generator(20)
    )
    node.save()
    return node

@pytest.mark.django_db
def test_node_get_book_from_leaf():
    root = get_node()
    leaf = get_node(parent=root)
    book = mommy.make(Book, tree=root)
    assert leaf.get_book() == book

@pytest.mark.django_db
def test_node_get_book_from_root():
    root = get_node()
    book = mommy.make(Book, tree=root)
    assert root.get_book() == book

