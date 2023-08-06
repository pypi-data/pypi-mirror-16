###########################################
# This is very naive replacement algorithm
# TODO
############################################
import subprocess
import string
import uuid
import logging
import os

# TODO: configurable variable
TEMP_DIR = "/tmp"

def replaceable(code, kv):
    # change keyword to value
    keys = kv.keys()
    # find keyword which is ${keyword}
    # replace value ${keyword} <- kv[keyword]
    for key in keys:
        nkey = "${%s}" % key
        code = string.replace(code, nkey, kv[key])
    logging.debug("#" * 20 + "\n%s" % code)
    logging.debug("#" * 20)

    return code


def shell_bash(**kwargs):
    """
    execute command
    @return: 
        dictionary of input, output, error
    """
    code = kwargs['code']
    kv = kwargs['kv']

    # call replaceable
    rcode = replaceable(code, kv)

    temp = uuid.uuid1()
    temp_file = "%s/%s" % (TEMP_DIR, str(temp))
     
    fp = open(temp_file, 'w')
    fp.write(rcode)
    fp.close()

    # Execute Cmd
    cmd = ['bash',temp_file]
    cmd2 = 'bash %s' % temp_file
    proc = subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE)
    out = ""
    while proc.poll() is None:
        line = proc.stdout.readline()
        print line
        out = out + line
    #(out, err) = proc.communicate()
    #out = subprocess.check_output(cmd2, shell=True)
    # Remove tempfile
    os.remove(temp_file)
    return {'input':rcode, 'output':out, 'error':''}
