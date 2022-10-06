import os


# check similar files
def duplicateFiles(path):
    fileDuplicates = {}
    result = []
    for dirPath, dirName, files in os.walk(path):
        for file in files:
            _, ext = os.path.splitext(file)
            if('.txt' in ext):
                with open(os.path.join(dirPath, file)) as reader:
                    if not (fileDuplicates.get(file)):
                        text = reader.read()
                        for item in fileDuplicates:
                            if fileDuplicates[item] == text:
                                result.append(file)
                                result.append(item)
                        fileDuplicates.update({file: text})
    return result

# Current working directory
search = os.getcwd()
# Returning duplicate files
print("\n List of duplicate text files: ", duplicateFiles(search))
