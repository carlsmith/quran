class Tell(object):

    def info(self, message): print "\033[94m[INFO]\033[0m " + highlight(message)
    def good(self, message): print "\033[93m[GOOD]\033[0m " + highlight(message)
    def warn(self, message): print "\033[95m[WARN]\033[0m " + highlight(message)
    def done(self, message): print "\033[92m[DONE]\033[0m " + highlight(message)
    def fail(self, message): print "\033[91m[FAIL]\033[0m " + highlight(message)

def highlight(message):

    output = ""
    highlighting = False

    for char in message:

        if char != "`": output += char
        elif highlighting: highlighting, output = False, output + "\033[0m"
        else: highlighting, output = True, output + "\033[1m"

    return output

tell = Tell()

