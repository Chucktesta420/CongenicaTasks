import os
import pytest
from click.testing import CliRunner
from upper_case_file import upper_case_file

inputDataFolder = 'input_data'
outputDataFolder = 'output_data'
inputFilePaths = os.listdir(inputDataFolder)
if os.path.isdir(outputDataFolder) == False:
    os.mkdir(outputDataFolder)


def compare_words(lowerCaseWord, upperCaseWord):
    lowerCaseLetters = [char for char in lowerCaseWord if char.islower()]
    return len(lowerCaseLetters) <= len(lowerCaseWord) and lowerCaseWord.upper() == upperCaseWord


def compare_lines(lowerCaseLine, upperCaseLine):
    linesMatch = False
    lowerCaseWords = lowerCaseLine.replace(',', '').split(' ')
    upperCaseWords = upperCaseLine.replace(',', '').split(' ')
    for wordIndex in range(0, len(lowerCaseWords)):
        linesMatch = compare_words(lowerCaseWords[wordIndex], upperCaseWords[wordIndex])
    return linesMatch


def compare_files(lowerCaseFilePath, upperCaseFilePath):
    filesMatch = False
    lowerCaseFile = open(lowerCaseFilePath, 'r')
    lowerCaseLines = lowerCaseFile.readlines()
    upperCaseFile = open(upperCaseFilePath, 'r')
    upperCaseLines = upperCaseFile.readlines()
    for lineIndex in range(0, len(lowerCaseLines)):
        filesMatch = compare_lines(lowerCaseLines[lineIndex], upperCaseLines[lineIndex])
    return filesMatch


def run_upper_case_file(inputFilesDir, outputFilesDir):
    inputFiles = os.listdir(inputFilesDir)
    runner = CliRunner()
    for inputFile in inputFiles:
        commandResult = runner.invoke(upper_case_file, ['--input-file', F'{inputFilesDir}\\{inputFile}',
                                                        '--output-file',
                                                        F'{outputFilesDir}\\{inputFile.replace("input", "output")}'])

        assert commandResult.exit_code == 0
        assert 'Done!' in commandResult.output


@pytest.mark.parametrize("inputFilePath", inputFilePaths)
def test_upper_case_file(inputFilePath):
    outputFilePath = inputFilePath.replace('input', 'output')
    run_upper_case_file(inputDataFolder, outputDataFolder)
    assert compare_files(F'{inputDataFolder}\\{inputFilePath}', F'{outputDataFolder}\\{outputFilePath}')
