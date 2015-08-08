
def doif(test_action, fix_action, targets):
    count, fixed, failed = 0, 0, 0
    import subprocess

    for target in targets:
        count += 1
        print "targets %d/%d, fixed %d, failed to fix %d" % (count, len(targets), fixed, failed)
        print "==== TEST 1 target %s ========================" % target
        test_cmd = "%s %s 2> %s-test.err 1> %s-test.out" % (test_action, target, target, target)
#        test_cmd = "%s %s " % (test_action, target)
        ret = subprocess.call([test_cmd], shell=True)
        if (ret != 0):
            print "target %s failed test with %d - fixing with %s" % (target, ret, fix_action)
            fix_cmd = "%s %s 2> %s-fix.err 1> %s-fix.out" % (fix_action, target, target, target)
#            fix_cmd = "%s %s" % (fix_action, target)
            print "==== FIX target %s ========================" % target
            ret = subprocess.call([fix_cmd], shell=True)
            if (ret != 0):
                print "target %s fix process failed with %d" % (target, ret)
                # GAME OVER
                failed += 1
            else:
                print "target %s fix process succeeded" % target
                print "==== TEST 2 target %s ========================" % target
                ret = subprocess.call([test_cmd], shell=True)
                if (ret != 0):
                    print "target %s failed to fix with %d" % (target, ret)
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
        test, fix, targets = sys.argv[1], sys.argv[2], sys.argv[3:]
        print "test: '%s' fix: '%s' targets: %s" % (test, fix, targets)
        sys.exit(doif(test, fix, targets))
