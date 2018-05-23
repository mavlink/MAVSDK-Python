import grpc

from .base import Base
from .generated import core_pb2, core_pb2_grpc


class Core(Base):
    """
    @TODO
    """

    def _setup_stub(self):
        """
        @TODO
        """
        # Actual Core stub
