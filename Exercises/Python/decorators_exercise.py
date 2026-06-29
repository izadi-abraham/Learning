
def show_run_time(f):
    def wrapper(n):
        from datetime import datetime
        time_before_run = datetime.now()
        # we need to await here, the function will be run asyncronously if not
        f(n)
        time_after_run = datetime.now()
        print(f"The function started running at {time_before_run} and finished running at {time_after_run}")
        print(f"It took {time_after_run - time_before_run} to run this function.")
    return wrapper

@show_run_time
def create_list(n):
    return [i for i in range(n)]


create_list(2000)