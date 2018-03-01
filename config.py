
# Author : Ilyes Bouchlaghem
###########################################
##        C O N F I G  -  F I L E        ##
###########################################

dirs =\
[
	"/bin",
	"/usr/bin",
	"/usr/lib",
	"./unittest/32",
	"./unittest/64",
	"./unittest/ar"
];

args =\
{
	'nm':
	(
		['-U', '-t', 'd'],		# User 'nm' arguments
		['-U', '-t', 'd']		# System 'nm' arguments
	),
	'otool':
	(
		['-d'],					# User 'otool' arguments
		['-t', '-d']			# System 'otool' arguments
	)
};
