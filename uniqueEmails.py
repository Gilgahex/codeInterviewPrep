def numUniqueEmails(emails):
	for i,e in enumerate(emails):
		for c in range(len(e)):
			if e[c] == '@':
				pre = e[:c]
				post = e[c:]
		pre = pre.replace(".","")
		
		for c in range(len(pre)):
			if pre[c] == "+":
				pre = pre[:c]
				break
		e = pre+post
		emails[i] = e
	emails = set(emails)
	return len(emails)
	
test = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(test))

