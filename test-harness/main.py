from harness import Harness

list_of_tools = ['snyk', 'pysa', 'codeql']

if __name__== '__main__':
    for tool in list_of_tools:
        tool_harness = Harness(tool)