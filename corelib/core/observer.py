# coding: utf-8

r"""Observer pattern implementation"""

import abc


class Observable(object):
    r"""An object that can be observed

    Intended use is by inheriting Observable

    """
    def __init__(self):
        self.observers = list()

    def add_observer(self, observer):
        r"""Add an observer"""
        self.observers.append(observer)

    def remove_observer(self, observer):
        r"""Remove an observer"""
        self.observers.remove(observer)

    def notify_observers(self, payload):
        r"""Notify all the observers"""
        for observer in self.observers:
            observer.handle_notification(payload)


class Observer(object):
    r"""An observer class that can be added to an Observable list of observers

    Observer is an abstract base class

    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def handle_notification(self, payload):
        r"""Abstract method, must be implemented by inheriting classes"""
        msg = 'The inheriting class must define handle_notification()'
        raise NotImplementedError(msg)
