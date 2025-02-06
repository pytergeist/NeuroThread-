from typing import Optional, Tuple


class Block:
    def __init__(self):
        self._inheritance_lock = False

    def _check_super_called(self):  # TODO add inheritance_lock attr in child classes
        if getattr(self, "_inheritance_lock", True):
            raise RuntimeError(
                f"In layer {self.__class__.__name__},"
                "you forgot to call super.__init__()"
            )

    def add_weight(
        self, shape: Optional[Tuple[int, int]] = None, initialiser=None, dtype=None
    ):  # TODO: Add tensor with initialised weights and set it as a Node (for grad tracking/autodiff)
        pass

    def forward(self, *inputs):
        raise NotImplementedError

    def __call__(self, *inputs):
        return self.forward(*inputs)
