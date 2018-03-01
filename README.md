# [ Nm-Otool </> Checker ]

## Installation

	$> git clone https://github.com/Ibouch/nm-otool-checker.git
    $> cd nm-otool-checker && ./install.sh
## Configuration

    $> vim config.py
Then you can edit the file to add / replace / remove directories path and arguments lines of you're programs and / or system programs
## Usage
Make sure you are at the root of you're nm-otool project !

    $> source nm-otool-checker/venv/bin/activate
    $> python nm-otool-checker/checker.py
    $> deactivate

## Description

 - This tool compare the data difference's of two outputs.
 - No order or repetition are make in consideration.

***Nb :** Sometimes the buffer are cut with whitespace padding and can generate a false positive.<br />
Please comment the padding in your source code or use the option* `--remove-space`<br />
*With this option the checker log is less readable.*

    $> python nm-otool-checker/checker.py --remove-space
