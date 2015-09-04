import kronos


class test_scheduler():

    def test_output():
        print "TESTING!!!!"

    sched = kronos.ThreadedScheduler()
    sched.start()

    sched.add_interval_task(action=test_output,
                            taskname="testoutput",
                            initialdelay=1,
                            interval=2,
                            processmethod=kronos.method.threaded,
                            args=None,
                            kw=None)

sched = test_scheduler()
