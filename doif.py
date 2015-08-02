
def doif(test_action, fix_action, targets):
    fixed, failed = 0, 0
    import subprocess

    for target in targets:
        print "target %s ========================" % target
        ret = subprocess.call([test_action, target])
        if (ret > 0):
            print "target %s failed test - fixing with %s" % (target, fix_action)
            ret = subprocess.call([fix_action, target])
            if (ret > 0):
                print "target %s fix process failed" % target
                # GAME OVER
                failed += 1
            else:
                ret = subprocess.call([test_action, target])
                if (ret > 0):
                    print "target %s failed to fix" % target
                    failed += 1
                else:
                    print "target %s fixed after initial fail" % target
                    fixed += 1
        else:
            print "target %s passed test" % target

    print "tested %d, fixed %d, failed to fix %d" % (len(targets), fixed, failed)
    return failed
    
def usage(scriptname):
    import os
    print "usage: ", os.path.basename(scriptname), "test action, fix action, target name, target name..."

if (__name__ == '__main__'):
    import sys

    if ((len(sys.argv)) < 4):
        usage(sys.argv[0])
    else:
        sys.exit(doif(sys.argv[1], sys.argv[2], sys.argv[3:]))
