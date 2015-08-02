
def doif():
    import subprocess

    # TODO(PMM) read in make command
    MAKE='make.bat'
    # TODO(PMM) read in test command
    TEST='test'
    # TODO(PMM) read in targets
    targets=['pass1', 'fail1', 'pass2', 'fail2'] 
    # TODO(PMM) read in fix command
    FIX='fix2'


    # TODO(PMM)
    for target in targets:
        print "target %s ========================" % target
        ret = subprocess.call([MAKE, target])
        if (ret > 0):
            print "target %s failed test - fixing" % target
            ret = subprocess.call([MAKE, 'fix1'])

            if (ret > 0):
                print "target %s fix process failed" % target
                # GAME OVER
            else:
                ret = subprocess.call([MAKE, target])
                if (ret > 0):
                    print "target %s failed to fix" % target
                else:
                    print "target %s fixed after initial fail" % target
        else:
            print "target %s passed test" % target

if (__name__ == '__main__'):
    # need args: test action, fix action, target names
    doif()
