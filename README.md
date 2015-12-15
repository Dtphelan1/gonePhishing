# gonePhishing

A node server for a website to be used for educational phishing purposes, as well as the materials used to launch the phishing attack.

### toPhish

This is where all of the phishing materials are.
- Not included in the folder is the Social Engineering Toolkit, complementary with the Kali operating system.
- toEmail.py was used to turn names.txt (taken from the security website) into emails.txt.
- template.txt was used to store an html template of the email to be sent.
- em.txt was used to test the procedure before messing up the experiment. Included are the emails of two friends.
- More information:
    - The FROM NAME used in the attack was mchow@cs.tuft.edu (remarkably similar to the email of the instructor).
    - The gmail account was set up for the purpose of this attack -- mchow617@gmail.com, which could plausibly be link back to the professor since Boston's area code is (617)

### Everything else
- Used for the node server to display both information on phishing attack and the mode of confirmation for my research.

### Results
- Emails Sent: 42
- Emails Opened: 17
- Proportion: .40476

### Conclusions:
Within 15 minutes, seven people took the bait -- despite the fact that the email was sent at 11:30 at night. Even within 60 seconds someone person followed the hyperlink and fell for the attack; and these statistics were  produced from a population of people who just finished taking a security class at Tufts University. Seeing as the email took 4 minutes to compose, getting the email list took 1 hour to produce, and setting up the server took less than 2 hours, it's clear to me that phishing is still a remarkbly simple and powerful way to get individuals to download malware and open malicious links -- even after education. 

Moving forward from this one should launch similar attacks on individuals -- perhaps Tufts students again for consistency's sake -- and see how those proportions compare to students who have taken a security, seeing if education programs have any robust effects on diminishing these proportions.
