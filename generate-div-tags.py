"""
    Write a function that takes in a positive integer
    numberOfTags and returns a list of all the valid strings that you
    can generate with that number of matched tags.

    A string is valid and contains matched <div></div> tags if for every opening tag
    <div>, there is a closing tag </div> that comes after the 
    opening tag and that isn't used as a closing tag for another opening 
    tag. Each output string should contain exactly numberOfTags opening 
    tags and numberOfTags closing tags.

    For example, given numberOfTags = 2, the valid strings to return
    would be:
    ["<div></div><div></div>",
        "<div><div></div></div>"].

    Note that the output strings don't need to be in any particular order.

    Example:
        numberOfTags = 3

        Output:
            [
                "<div><div><div></div></div></div>",
                "<div><div></div><div></div></div>",
                "<div><div></div></div><div></div>",
                "<div></div><div><div></div></div>",
                "<div></div><div></div><div></div>"
            ]
"""

def generateDivTags(numberOfTags):
	results = []
	tags_helper(numberOfTags, numberOfTags, "", results)
	return results

def tags_helper(startTags, endTags, currentTags, results):
	if endTags == 0:
		results.append(currentTags)
	
	if startTags > 0:
		tags_helper(startTags - 1, endTags, currentTags + "<div>", results)
	if endTags > startTags:
		tags_helper(startTags, endTags - 1, currentTags + "</div>", results)
		