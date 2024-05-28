FriendFinder360 (working title) is an app that strives to get to know you deeply, across a wide range of topic areas.
Once we get to know you, we search our database to find others in our ecosystem who may be an ideal friend match for you.
The intention of the app is to use the latest approaches to understanding the complete personality, to find the best matches.

We are aware that a potential use of the program may be for people to find romantic connections, and that's fine. We encourage that!
Our focus is on finding friendships primarily as we believe the basis of a solid romantic connection is well founded friendship

This app is coded in Python initially. Who knows where it may go from there or what technologies may be added to the stack as necessary?

INITIAL FEATURES v1.0
- ability for user to add full name which gets associated with a user ID and tied to their answers, for later retrieval
- user answers a series of questions, with each answer on a 4 answer NO MIDDLE POINT scale of STRONGLY AGREE, SOMEWHAT AGREE, SOMEWHAT DISAGREE, STRONGLY DISAGREE
- user may choose how many questions to answer per session. app keeps track of which questions they've answered in the database
- on future runs of the app, user may answer additional questions, but the app doesn't ask them questions they've already answered
- once user answers all the questions for that session, the app compares user's answers to other users in the database, and calculates ordered ranking of top 3 best friend matches
- friend matches for v1 are simple closest match percentages of same or similar answers. future versions of app will find more nuanced ways to make complementary matches. INTROVERT w/ EXTROVERT for example
- KEY FEATURE! app stores user profiles in JSON files, so app remembers users when they come back

VERSION 0.1
- Enter your first name. answer 10 questions. don't persist memory. compare to 5 pre-existing "fake" users. show final ordered match ranking at the end 28 May 2024