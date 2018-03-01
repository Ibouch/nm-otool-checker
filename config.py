
# Author : Ilyes Bouchlaghem
###########################################
##        C O N F I G  -  F I L E        ##
###########################################

dirs =\
[
	#"/bin",
	#"/usr/bin",
	#"/usr/lib",
	"./unittest/32",
	"./unittest/64",
	"./unittest/ar"
#	"correc"
];

args =\
{
	'nm':
	(
		['-U', '-t', 'd'],		# User program arguments
		['-U', '-t', 'd']		# System program arguments
	),
	'otool':
	(
		['-d'],					# User program arguments
		['-t', '-d']			# System program arguments
	)
};
