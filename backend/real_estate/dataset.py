from dataclasses import dataclass


@dataclass #2칸 띄우기 PEP에 따라서
class Dataset(object):

    context: str
    fname: str
    cost : object

    @property
    def context(self) -> str: return self._context
    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname
    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def cost(self) -> object: return self._cost
    @cost.setter
    def cost(self, cost): self._cost = cost

