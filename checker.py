# coding: utf-8
# Author : Ilyes Bouchlaghem

import os
import re
import sys
import select 
import subprocess
from config import *
from tqdm import tqdm
from prettytable import PrettyTable

def write_data_log(data_log):
	filename = "nm-otool-checker/nm-otool-checker.txt";
	with open(filename, 'w') as f: 
		f.write(data_log);
	os.system("open " + filename);

def diff(first, second):
	# Consider both outputs with only one line as an error message
	if (len(first) == 1 and len(second) == 1):
		return ([]);
	second = set(second);
	return ([item for item in first if item not in second]);

def get_diff_to_string(diff_list, char):
	diff_str = str();
	for e in diff_list:
		diff_str += char + ' ' + e + '\n';
	if char == '<':
		diff_str += "- - - - - -" + '\n';
	elif diff_str:
		diff_str += '\n';
	return (diff_str);

def clean_data(stdout):
	lines = stdout.splitlines();
	char = ('' if ("--remove-space" in sys.argv) else ' ');
	for i, line in enumerate(lines):
		str_trimmed = re.sub("\s+", char, line).strip();
		if (str_trimmed == ""):
			del (lines[i]);
		else:
			lines[i] = str_trimmed;
	return (lines);

def async_exec(bin, args, path):
	# Create a buffer and a pipe to receive stdout and stderr from process
	(pipe_r, pipe_w) = os.pipe();
	buffer = str();
	args_lst = [bin];
	for arg in args:
		args_lst.append(arg);
	args_lst.append(path);
	# Call subprocess
	process = subprocess.Popen(args_lst,
                               shell  = False,
                               stdout = pipe_w,
                               stderr = pipe_w);
	# Loop while the process is executing
	while (process.poll() is None):
		while (len(select.select([pipe_r], [], [], 0)[0]) == 1):
			buffer += os.read(pipe_r, 4096);
	# Cleanup
	os.close(pipe_r)
	os.close(pipe_w)
	return (clean_data(buffer));

def exec_tests(Ptable, data, args):
	index = 0;
	data_log = str();
	result = dict();
	while (index < len(data)):
		for directory in data[index]:
			for prog in tqdm(args, desc=directory):
				correct = 0;
				for path in tqdm(data[index][directory], desc='[ ' + prog.title() + ' ]'):
					# Running user and system programs
					nm_sys_output = async_exec(prog, args[prog][1], path);
					nm_usr_output = async_exec("./ft_" + prog, args[prog][0], path);
					# Make diff
					diff_sys = diff(nm_sys_output, nm_usr_output);
					diff_usr = diff(nm_usr_output, nm_sys_output);
					# Write result
					str_log = "[ " + prog.upper() + " ]\t" + path + '\n';
					if (not diff_sys and not diff_usr):
						correct += 1;
						data_log += "[ Success ] " + str_log;
					else:
						data_log += "[ Error ] " + str_log;
					data_log += get_diff_to_string(diff_sys, '<');
					data_log += get_diff_to_string(diff_usr, '>');
				result[prog] = correct;
			nb_e = len(data[index][directory])
			Ptable.add_row([directory, result['nm'], result['otool'], nb_e - result['nm'], nb_e - result['otool'],
			str(result['nm'] + result['otool']) + " / " + str(2 * nb_e)]);
		index += 1;
	write_data_log(data_log);

def	main():
	Ptable = PrettyTable();
	Ptable.field_names = ["PATH", u"NM \u2705 ",  u"OTOOL \u2705 ", u"NM \u2b55 ", u"OTOOL \u2b55 ", "TOTAL"]
	data = list();
	for directory in dirs:
		files = list();
		for filename in os.listdir(directory):
			path = directory + '/' + filename;
			if os.path.isfile(path) and os.access(path, os.X_OK):
				files.append(path);
		data.append({directory : files});
	exec_tests(Ptable, data, args);
	Ptable.align = 'r';
	Ptable.align["PATH"] = "c"
	print '\n\033[1;33m'
	print Ptable

if __name__ == '__main__':
	os.system("make re > /dev/null");
	print "\033[1;31m [ Nm-Otool-Checker ] by Ibouchla\033[1;34m";
	main();
