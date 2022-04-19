from abc import ABC, abstractmethod
from typing import Generic, TypeVar

A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')

class TwoTypes(Generic[A, B]): pass

class ReproBase(ABC, Generic[C]):

  @abstractmethod
  def repro(self, a: A) -> TwoTypes[C, A]: pass

class ReproSub(ReproBase[C]):

  @abstractmethod
  def repro_defer(self, a: A) -> TwoTypes[C, A]: pass

  def repro(self, a: A) -> TwoTypes[C, A]:
    return self.repro_defer(a)

class ReproSub2(ReproBase[C], Generic[C]):

  @abstractmethod
  def repro_defer(self, a: A) -> TwoTypes[C, A]: pass

  def repro(self, a: A) -> TwoTypes[C, A]:
    return self.repro_defer(a)
