from subprocess import *
import os

def grade(grader_path, grader_config, student_response, sandbox):
  errors = []
  aux = []
  sout, serr = Popen(["/edx/app/xserver/venvs/xserver-sandbox/bin/python","-c",student_response,"-v"], stdout=PIPE, stderr=PIPE).communicate()
  if(serr == ""):
	correct = True
	shrt_desc = "Script output:"
	long_desc = " "
	corr = True
	aux = [[shrt_desc, long_desc, corr, " ", sout]]
    else:
        correct = False
        errors = [serr,sout]

    results = {
        'correct': correct,
        'score': 1,
        'tests': aux,
        'errors': errors
    }
    return results
