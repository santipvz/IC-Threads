from threading import Thread
from math import tan, atan


class miThread(Thread):

    def __init__(self, x=1):
        super().__init__()
        self.nr = x

    def run(self):
        # print(f"Empezó el hilo {self.name} con {self.nr} iteraciones\n")
        for i in range(self.nr):
            # print(f"Estamos el hilo {self.name} con {self.nr} iteraciones")
            d = (
                tan(
                    atan(
                        tan(atan(tan(atan(tan(atan(tan(atan(123456789.123456789))))))))
                    )
                )
            ) ** (1 / 3)
        # print(f"Acabó el hilo {self.name} con {self.nr} iteraciones\n")


def functionWithThread(nIterations: int) -> None:
    """
    This function creates a thread and runs it
    with the task.

    We need to create this function because
    ProcessPoolExecutor can't work directly with
    the class miThread.

    Args:
        - nIterations (int): Number of iterations to be done

    Returns:
        - None
    """
    thread = miThread(nIterations)
    thread.start()
    thread.join()
