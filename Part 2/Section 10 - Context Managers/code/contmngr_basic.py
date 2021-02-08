class MyContext:
    def __init__(self) -> None:
        print('init running')
        self.obj = None

    def __enter__(self):
        print('enetering context...')
        self.obj = 'the Return object'
        return self.obj

    def __exit__(self, exec_type, exc_value, exc_tb) -> bool:
        print('exiting context...')
        if exec_type:
            print(f"... Error occurred: {exec_type},{exc_value}")
        return False #to suppress the error, we return True


with MyContext() as obj:
    print('inside with block', obj)
    raise ValueError("custom message")
