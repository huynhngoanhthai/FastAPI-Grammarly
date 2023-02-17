# importing the package  
import language_tool_python  

# using the tool  
my_tool = language_tool_python.LanguageTool('en-US')  
  


def spellcheck(my_text):
    # getting the matches  
    my_matches = my_tool.check(my_text)  
    result = []
    for rules in my_matches:  
        item = dict()
        if len(rules.replacements) > 0:  
            item["ruleId"] = rules.ruleId
            item["message"] = rules.message
            item['replacements'] = rules.replacements[:3]
            item['offsetInContext'] = rules.offsetInContext
            item['context'] = rules.context
            item['offset'] = rules.offset
            item['errorLength'] = rules.errorLength
            item['category'] = rules.category
            item['ruleIssueType'] = rules.ruleIssueType
            item['sentence'] = rules.sentence
        result.append(item)
    return result
def addNewWord(word: str):
    file1 = open(my_tool._get_valid_spelling_file_path(),  "a")  # write mode
    file1.write("\n"+word)
    file1.close()

# a=my_tool._get_valid_spelling_file_path()?


print(spellcheck(""))
# print(addNewWord("hello"))